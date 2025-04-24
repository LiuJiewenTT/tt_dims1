import zipfile
import os
import json

# 基础路径
base_path = "tt_dims2_datapack"
data_path = os.path.join(base_path, "data", "tt_dims2", "dimension")
os.makedirs(data_path, exist_ok=True)

# 维度配置字典：文件名 -> JSON 内容
dimensions = {
    "ovw.json": {
        "type": "minecraft:overworld",
        "generator": {
            "type": "minecraft:noise",
            "settings": "minecraft:overworld"
        }
    },
    "ovw_alignflat.json": {
        "type": "minecraft:overworld",
        "generator": {
            "type": "minecraft:flat",
            "settings": {
                "layers": [
                    { "block": "minecraft:bedrock", "height": 1 },
                    { "block": "minecraft:deepslate", "height": 30 },
                    { "block": "minecraft:stone", "height": 86 },
                    { "block": "minecraft:dirt", "height": 10 },
                    { "block": "minecraft:grass_block", "height": 1 }
                ],
                "biome": "minecraft:plains",
                "structures": {
                    "stronghold": {},
                    "village": { "type": "minecraft:village" }
                }
            }
        }
    },
    "void.json": {
        "type": "minecraft:overworld",
        "generator": {
            "type": "minecraft:flat",
            "settings": {
                "layers": [],
                "biome": "minecraft:void",
                "structures": {}
            }
        }
    }
}

# 写入所有维度 JSON 文件
for filename, content in dimensions.items():
    with open(os.path.join(data_path, filename), "w") as f:
        json.dump(content, f, indent=2)

# pack.mcmeta 内容
mcmeta = {
    "pack": {
        "pack_format": 26,  # 对应 Minecraft 1.20.4，向下兼容 1.18+
        "description": "tt_dims2: Custom dimensions including aligned flat world"
    }
}

# 写入 pack.mcmeta
with open(os.path.join(base_path, "pack.mcmeta"), "w") as f:
    json.dump(mcmeta, f, indent=2)

# 打包为 ZIP
zip_path = "tt_dims2_datapack.zip"
with zipfile.ZipFile(zip_path, "w") as zipf:
    for root, _, files in os.walk(base_path):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_path)
            zipf.write(full_path, rel_path)

zip_path
