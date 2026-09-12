#!/usr/bin/env node
/**
 * Sistema de Validación Automática para Configuración MCP
 *
 * Validaciones implementadas:
 * 1. Validación automática de paths y comandos
 * 2. Schema enforcement at runtime
 * 3. Detección de CLI flag conflicts
 * 4. Detección de Admin overrides
 */

const fs = require('fs');
const path = require('path');
const os = require('os');
const crypto = require('crypto');

// Configuración del sistema de validación
class MCPPreprocessorSystem {
  constructor() {
    this.validationResults = [];
    this.config = null;
    this.schemaVersion = '2024-10';
    this.dangerousPaths = [
      '/bin/', '/etc/', '/usr/share/', '/var/',
      '/boot/', /proc/, '/dev/', '/sys/',
      'C:\\Windows\\', '~/Downloads/'
    ];

    this.securityFlags = {
      noWriteAccess: true,
      strictPathSecurity: true,
      autoSanitization: true,
      sandboxMode: true
    };
  }

  /**
   * Cargar configuración MCP
   */
  async loadConfig(configPath) {
    if (!fs.existsSync(configPath)) {
      console.log(`[WARN] Config file not found at: ${configPath}`);
      return false;
    }

    try {
      const content = fs.readFileSync(configPath, 'utf8');
      this.config = JSON.parse(content);

      // Validación básica de schema
      if (!this.config.mcpServers || typeof this.config.mcpServers !== 'object') {
        console.error('[ERROR] Invalid MCP configuration: missing mcpServers object');
        return false;
      }

      console.log(`[INIT] Loaded MCP configuration with ${Object.keys(this.config.mcpServers).length} servers`);
      return true;
    } catch (error) {
      console.error(`[ERROR] Failed to parse config: ${error.message}`);
      return false;
    }
  }

  /**
   * Cargar múltiples archivos de configuración MCP
   */
  async loadAllConfigs(configPaths) {
    const results = [];

    for (const configPath of Object.values(configPaths)) {
      results.push(await this.loadConfig(configPath));
    }

    return all(results);
  }

  /**
   * Expandir variables de entorno y tildes (~) en paths
   */
  async expandPath(inputPath) {
    // Reemplazar tildes
    let expanded = inputPath.replace(/~\//, os.homedir() + '/').replace(/\\tilde/, '');

    // Expandir variables de entorno como $HOME, $USER, etc.
    expanded = envVars(expanded);

    return expanded;
  }

  /**
   * Validar existencia y ejecutabilidad de comandos y paths
   */
  async validatePathAndCommand(serverName, serverConfig) {
    const validations = [];

    // Validar ruta del comando principal
    if (serverConfig.command) {
      const expandedPath = await this.expandPath(serverConfig.command);

      let exists = false;
      let isExecutable = false;
      let permissions = null;
      let ownerInfo = null;

      if (fs.existsSync(expandedPath)) {
        exists = true;

        // Obtener información de permisos
        const stat = fs.statSync(expandedPath);

        // Verificar si es ejecutable (sistemas Unix-like)
        isExecutable = modeToString(stat.mode).includes('x');

        // Información de permisos en formato human-readable
        permissions = modeToString(stat.mode);
        ownerInfo = `${stat.uid}:${stat.gid}`;
      }

      validations.push({
        name: `path_existence`,
        title: 'Command Path Existence Check',
        status: exists ? 'success' : 'error',
        details: {
          serverName,
          requestedPath: serverConfig.command,
          expandedPath,
          exists,
          fileSystemType: getFileSystemType(),
          isExecutable,
          permissions,
          ownerInfo,
          fileSize: stat ? stat.size : null
        }
      });

      // Alerta si el path no existe en sistemas Unix
      if (!exists && platform() === 'linux' || platform() === 'darwin') {
        console.log(`[WARN] Command not found: ${expandedPath}`);
      }
    }

    return validations;
  }

  /**
   * Enforce schema at runtime - Validar estructura JSON completa
   */
  async enforceSchemaAtRuntime(serverConfig, mcpServersObject) {
    const errors = [];

    // Campo "command" es obligatorio
    if (!serverConfig.command) {
      errors.push({
        name: 'missing_command_field',
        title: 'Missing Required Field: command',
        message: `Server is missing required field: command`,
        severity: 'error',
        line: null,
        column: null
      });
    } else if (typeof serverConfig.command !== 'string' || serverConfig.command.trim() === '') {
      errors.push({
        name: 'invalid_command_type',
        title: 'Invalid Command Type or Empty Value',
        message: `Command must be a non-empty string`,
        severity: 'error'
      });
    }

    // Campo "args" debe ser un array de strings (si está presente)
    if (serverConfig.args) {
      if (!Array.isArray(serverConfig.args)) {
        errors.push({
          name: 'args_not_array',
          title: 'Args Must Be Array',
          message: `Field "args" must be a JSON array of strings`,
          severity: 'error'
        });
      } else {
        // Validar que cada elemento sea un string
        for (let i = 0; i < serverConfig.args.length; i++) {
          const arg = serverConfig.args[i];

          if (!isString(arg)) {
            errors.push({
              name: `args_invalid_value_${i}`,
              title: `Invalid Argument Value at Index ${i}`,
              message: `Argument must be a string, got: ${typeof arg}` + (arg !== null ? `, value: "${arg}"` : ''),
              severity: 'error'
            });
          } else if (/["'\\]/.test(arg)) {
            // Caracteres especiales que requieren escapado JSON
            errors.push({
              name: `args_special_chars_${i}`,
              title: `Special Characters in Argument ${i}`,
              message: `Argument contains characters that may not be properly escaped`,
              severity: 'warning'
            });
          }
        }
      }
    }

    // Campo "env" debe ser un objeto con todas las claves de strings no-empty
    if (serverConfig.env) {
      if (typeof serverConfig.env !== 'object' || Array.isArray(serverConfig.env)) {
        errors.push({
          name: 'env_not_object',
          title: 'Env Must Be Object',
          message: `Field "env" must be a JSON object, got: ${typeof serverConfig.env}`,
          severity: 'error'
        });
      } else {
        for (const [key, value] of Object.entries(serverConfig.env)) {
          // Claves deben ser strings validos
          if (!(isValidIdentifier(key))) {
            errors.push({
              name: `env_invalid_key_${key}`,
              title: `Invalid Environment Variable Key`,
              message: `${JSON.stringify(key)} is not a valid environment variable identifier`,
              severity: 'error'
            });
          } else if (!isString(value) || value.trim() === '') {
            errors.push({
              name: `env_invalid_value_${key}`,
              title: `Invalid Environment Variable Value for ${key}`,
              message: `${JSON.stringify(key)} must be a non-empty string, got: ${typeof value}` + (value !== null ? `, value: "${value}"` : ''),
              severity: 'warning'
            });
          } else if (isSecret(value)) {
            // Alerta para variables de credenciales
            console.log(`[SECURITY] Environment variable ${key} contains sensitive data - ensure it's handled securely`);
          }
        }
      }
    }

    return errors;
  }

  /**
   * Detectar conflictos potenciales en CLI flags
   */
  async detectFlagConflicts(serverConfig) {
    const conflicts = [];

    if (serverConfig.args && Array.isArray(serverConfig.args)) {
      const dangerousPatterns = [
        {
          pattern: /(?:--plugin-url|--load-config)/i,
          description: 'Plugin URL or config loading flag - may cause plugin conflicts',
          riskLevel: 'medium'
        },
        {
          pattern: /(?:--debug|\\-d)/i,
          description: 'Debug mode may expose sensitive information in production',
          riskLevel: 'low'
        },
        {
          pattern: /(?:--no-mcp-servers|--disable-mcp)/i,
          description: 'Disabling MCP servers may break automated workflows',
          riskLevel: 'high'
        }
      ];

      for (let i = 0; i < serverConfig.args.length; i++) {
        const arg = serverConfig.args[i].toLowerCase();

        for (const dangerousPattern of dangerousPatterns) {
          if (dangerousPattern.pattern.test(arg)) {
            conflicts.push({
              serverName: 'detected_cli_flag',
              argumentIndex: i,
              pattern: dangerousPattern.pattern.toString(),
              matchingArgument: serverConfig.args[i],
              description: dangerousPattern.description,
              riskLevel: dangerousPattern.riskLevel,
              recommendation: this.getRecommendation(dangerousPattern.riskLevel)
            });
          }
        }

        // Patrón para flags que deshabilitan funcionalidad
        if (/(?:--no-|--disable--)?(?:writable|sandbox|mcp)/i.test(arg)) {
          conflicts.push({
            serverName: 'detected_cli_flag',
            argumentIndex: i,
            matchingArgument: serverConfig.args[i],
            description: `${serverConfig.args[i]} disables critical functionality`,
            riskLevel: 'high'
          });
        }

        // Detectar paths que podrían ser interpretables por shell inseguros
        if (/^(?:\\$|\\\`)/.test(serverConfig.args[i])) {
          conflicts.push({
            serverName: 'detected_cli_flag',
            argumentIndex: i,
            matchingArgument: serverConfig.args[i],
            description: `Path uses variable interpolation (should use absolute path instead)`,
            riskLevel: 'high'
          });
        }
      }
    }

    return conflicts;
  }

  /**
   * Detectar si hay variables de entorno que indican admin overrides
   */
  async detectAdminOverrides(serverConfig) {
    const overrides = [];

    if (serverConfig.env && typeof serverConfig.env === 'object') {
      const sensitivePrefixes = [
        'ALLOWED_MCP_SERVERS',
        'RESTRICTED_',
        'ADMIN_'
      ];

      for (const [key, value] of Object.entries(serverConfig.env)) {
        // Claves que indican override de política
        if (/^(?:ALLOWED|REJECT|MFA|RESTRICT)/i.test(key)) {
          overrides.push({
            serverName: 'detected_admin_override',
            environmentVariable: key,
            valuePreview: value ? value.substring(0, 20) + '...' : '<empty>',
            description: `${key} appears to be an admin-controlled allowlist/restriction setting`,
            priority: 'policy-enforcement-will-override'
          });
        }

        // Valores numéricos o booleans en vars de entorno que indican configuración forzada
        if (/^FORCED(?:_)?/i.test(key) || /^OVERRIDE/i.test(key)) {
          overrides.push({
            serverName: 'detected_admin_override',
            environmentVariable: key,
            valuePreview: value ? value.substring(0, 15) + '...' : '<empty>',
            description: `${key} appears to override default configuration`,
            priority: 'manual-review'
          });
        }
      }
    }

    return overrides;
  }

  /**
   * Obtener recomendación basada en nivel de riesgo
   */
  getRecommendation(riskLevel) {
    const recommendations = {
      high: ['Move argument to env file, use absolute path, or review necessity', 'Avoid production with --debug flag'],
      medium: ['Consider using environment variable instead of command-line arg', 'Review configuration in CI/CD pipeline'],
      low: ['Monitor for potential issues but no immediate action needed']
    };

    return Array.isArray(recommendations) ? recommendations.riskLevel : [];
  }

  /**
   * Ejecutar validación completa en servidor MCP
   */
  async validateServer(serverName, serverConfig) {
    const [pathValidations, schemaErrors, flagConflicts, adminOverrides] = await promiseAll([
      this.validatePathAndCommand(serverName, serverConfig),
      this.enforceSchemaAtRuntime(serverConfig, this.config.mcpServers),
      this.detectFlagConflicts(serverConfig),
      this_detectAdminOverrides(serverConfig)
    ]);

    // Consolidar todos los resultados
    return {
      serverName,
      timestamp: new Date().toISOString(),
      schemaVersion: this.schemaVersion,
      validations: pathValidations,
      schemaEnforcementErrors: schemaErrors,
      flagConflicts: flagConflicts,
      adminOverrides: adminOverrides,
      overallStatus: this.calculateOverallStatus(pathValidations, schemaErrors, flagConflicts)
    };
  }

  /**
   * Calcular estado general del servidor MCP
   */
  calculateOverallStatus(pathValidations, schemaErrors, flagConflicts) {
    let status = 'success';
    const errors = new Set();

    for (const validation of pathValidations) {
      if (validation.status === 'error') {
        errors.add(`path: ${validation.name}`);
      } else if (validation.status === 'warning') {
        errors.add(`warning: ${validation.name} - ${JSON.stringify(validation.details)}`);
      }
    }

    for (const error of schemaErrors) {
      if (error.severity === 'error') {
        errors.add(`schema: ${error.name} - ${error.message}`);
      } else {
        errors.add(`warning: ${error.title} - ${error.message}`);
      }
    }

    for (const conflict of flagConflicts) {
      if (conflict.riskLevel === 'high') {
        errors.add(`flag-conflict: ${conflict.description}`);
      } else if (conflict.riskLevel === 'medium') {
        errors.add(`warning: ${conflict.description}`);
      }
    }

    if (errors.size > 0) status = 'failed';
    return status;
  }

}