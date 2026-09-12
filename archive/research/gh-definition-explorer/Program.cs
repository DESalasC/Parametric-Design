using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using GH_IO.Serialization;
using GH_IO.Types;

namespace GhDefinitionExplorer
{
    class Program
    {
        static void Main(string[] args)
        {
            // Uso esperado:
            // GhDefinitionExplorer <gh_file> <json_output>
            if (args.Length < 2)
            {
                Console.WriteLine("Usage: GhDefinitionExplorer <gh_file> <json_output>");
                return;
            }

            string ghFile = args[0];
            string jsonOutput = args[1];

            if (!File.Exists(ghFile))
            {
                Console.WriteLine($"GH file not found: {ghFile}");
                return;
            }

            try
            {
                Console.WriteLine("Creating GH_Archive...");
                var archive = new GH_Archive();

                Console.WriteLine($"Reading file: {ghFile}");
                bool readOk = archive.ReadFromFile(ghFile);
                if (!readOk)
                {
                    Console.WriteLine("Failed to read GH file via GH_Archive.");
                    return;
                }

                Console.WriteLine("Getting root node...");
                GH_IChunk root = archive.GetRootNode; // Note: property, not method
                if (root == null)
                {
                    Console.WriteLine("Root node is null.");
                    return;
                }

                Console.WriteLine("Building tree...");
                var rootNode = BuildTree(root, "");

                Console.WriteLine("Serializing to JSON...");
                var options = new JsonSerializerOptions { WriteIndented = true };
                string json = JsonSerializer.Serialize(rootNode, options);
                File.WriteAllText(jsonOutput, json);

                Console.WriteLine($"JSON written to {jsonOutput}");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
                Console.WriteLine("Stack trace: " + ex.StackTrace);
            }
        }

        static ChunkNode BuildTree(GH_IChunk chunk, string path)
        {
            var node = new ChunkNode { Path = path };

            // Items
            for (int i = 0; i < chunk.ItemCount; i++)
            {
                GH_Item item = chunk.Items[i];
                string name = item.Name ?? "";
                object value = item.InternalData;
                string valueStr = value?.ToString() ?? "null";
                node.Items.Add(new ItemInfo { Name = name, Value = valueStr });
            }

            // Children (sub-chunks)
            for (int i = 0; i < chunk.ChunkCount; i++)
            {
                var child = chunk.Chunks[i];
                string childName = child.Name ?? $"[{i}]";
                string childPath = string.IsNullOrEmpty(path) ? childName : $"{path}/{childName}";
                node.Children.Add(BuildTree(child, childPath));
            }

            return node;
        }
    }

    public class ChunkNode
    {
        public string Path { get; set; }
        public List<ItemInfo> Items { get; set; } = new List<ItemInfo>();
        public List<ChunkNode> Children { get; set; } = new List<ChunkNode>();
    }

    public class ItemInfo
    {
        public string Name { get; set; }
        public string Value { get; set; }
    }
}