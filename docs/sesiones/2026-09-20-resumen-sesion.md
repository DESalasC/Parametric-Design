# Resumen de sesión 2026-09-20

**Tema:** Seguridad de credenciales (Bitwarden) — transversal. Incluye cambio de teclado a ENG INTL.

## Qué se hizo
- Teclado `en-US`: **US → ENG INTL** (`0409:00020409`), `es-CO` intacto.
- **Triaje HIBP** de 5 correos: yahoo 11 (8), hotmail 7 (6), gmail 5 (5), omcedesc 2 (1), outlook 0.
- **Bitwarden CLI v2026.8.0** instalado; login OK (OTP de dispositivo nuevo); operación con `BW_SESSION`.
- **Dropbox**: limpieza 9→6 y contraseñas únicas de 20 caracteres en las 5 cuentas.
- **28 entradas yzarq.com** → 27 en carpeta *"REVISAR - yzarq.com (dominio extinto)"*.

## Decisiones
- Bitwarden como gestor desde AutoClaw; una contraseña única por cuenta (ADR-018).
- No introducir credenciales en el navegador automatizado remoto.
- Conservar `passwordHistory`; carpetas `REVISAR` para dominios extintos; no borrar respaldos antes de terminar.

## Pendientes
- Cuenta 5 Dropbox (`salas.preciado.arquitectos@gmail.com`).
- Revisar 27 entradas yzarq.com.
- Continuar con el resto de servicios filtrados.
- `bw lock`.

## Documentos
- Informe: `D:\Users\Work\.openclaw-autoclaw\workspace\brechas\informe-filtraciones.md`
- Vault: `10-arquitectura/resumen-sesion-2026-09-20.md`, `50-lecciones/2026-09-20-leccion-*.md`, `10-arquitectura/decisiones-adr/adr-018-gestion-credenciales-bitwarden.md`
- Memoria: `D:\Work\PROJECTS\DiseñoParametrico\memory\sesion-2026-09-20.md`

## Etiquetas
#seguridad #contrasenas #bitwarden #hibp #dropbox
