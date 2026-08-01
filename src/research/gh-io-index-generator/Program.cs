using System;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;

class GhIoIndexGenerator
{
    static void Main(string[] args)
    {
        // Ruta al GH_IO.dll (ajústala según tu instalación real)
        var ghIoPath = @"C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll";

        if (!File.Exists(ghIoPath))
        {
            Console.Error.WriteLine($"[ERROR] No se encontró GH_IO.dll en: {ghIoPath}");
            return;
        }

        Assembly ghIoAssembly;
        try
        {
            ghIoAssembly = Assembly.LoadFrom(ghIoPath); // carga directa en el contexto de ejecución
        }
        catch (Exception ex)
        {
            Console.Error.WriteLine($"[ERROR] No se pudo cargar GH_IO.dll: {ex.Message}");
            return;
        }

        Type[] allTypes;
        try
        {
            allTypes = ghIoAssembly.GetTypes(); // obtiene todos los tipos definidos en la asamblea
        }
        catch (ReflectionTypeLoadException ex)
        {
            // Nos quedamos con los tipos que sí se pueden cargar
            allTypes = ex.Types.Where(t => t != null).ToArray();
        }

        var types = allTypes
            .Where(t => t.IsPublic)
            .OrderBy(t => t.Namespace)
            .ThenBy(t => t.Name)
            .ToList();

        var byNamespace = types
            .GroupBy(t => t.Namespace ?? string.Empty)
            .OrderBy(g => g.Key)
            .ToList();

        var sb = new StringBuilder();
        sb.AppendLine("# GH_IO – Mapa textual de clases (generado automáticamente)");
        sb.AppendLine();
        sb.AppendLine($"Fuente: `{Path.GetFileName(ghIoPath)}`");
        sb.AppendLine();

        foreach (var nsGroup in byNamespace)
        {
            string ns = string.IsNullOrEmpty(nsGroup.Key) ? "(sin namespace)" : nsGroup.Key;
            sb.AppendLine($"## {ns}");
            sb.AppendLine();

            foreach (var t in nsGroup)
            {
                string kind = GetKind(t);
                string noteHint = GetNoteHint(t);

                sb.AppendLine($"- {kind} `{t.Name}` – {noteHint}");
            }

            sb.AppendLine();
        }

        // Ruta de salida (ajusta a tu proyecto/bóveda)
        var outputPath = @"C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\output\markdown\GH_IO-index.md";

        try
        {
            File.WriteAllText(outputPath, sb.ToString(), Encoding.UTF8);
            Console.WriteLine($"[OK] Índice GH_IO generado en: {outputPath}");
        }
        catch (Exception ex)
        {
            Console.Error.WriteLine($"[ERROR] No se pudo escribir GH_IO-index.md: {ex.Message}");
        }
    }

    static string GetKind(Type t)
    {
        if (t.IsClass && !t.IsAbstract) return "Class";
        if (t.IsClass && t.IsAbstract) return "Abstract class";
        if (t.IsInterface) return "Interface";
        if (t.IsEnum) return "Enum";
        if (t.IsValueType && !t.IsEnum) return "Struct";
        return "Type";
    }

    static string GetNoteHint(Type t)
    {
        var name = t.Name;

        return name switch
        {
            "GH_Archive" => "nota esperada: [[GH_Archive]]",
            "GH_Chunk"   => "nota esperada: [[GH_Chunk]]",
            "GH_Message" => "nota esperada: [[GH_Message]]",
            _            => "pendiente de nota"
        };
    }
}