import os
import json
import zipfile

# 创建基础路径以写入 dimension_type 文件（模拟处理后的结构）
manual_base_path = "tt_dims1_dimtypes_only"
dimtype_dir = os.path.join(manual_base_path, "data", "tt_dims1", "dimension_type")
os.makedirs(dimtype_dir, exist_ok=True)

# 定义每个维度及其基于的默认类型
dimension_bases = {
    "ovw": "minecraft:overworld",
    "ovw_alignflat": "minecraft:overworld",
    "net": "minecraft:the_nether",
    "end": "minecraft:the_end",
    "void": "minecraft:overworld"
}

# 默认配置（不包含 height 和 logical_height）
defaults = {
    "minecraft:overworld": {
        "ultrawarm": False,
        "natural": True,
        "coordinate_scale": 1.0,
        "has_skylight": True,
        "has_ceiling": False,
        "ambient_light": 0.0,
        "piglin_safe": False,
        "bed_works": True,
        "respawn_anchor_works": False,
        "has_raids": True,
        "infiniburn": "minecraft:infiniburn_overworld",
        "effects": "minecraft:overworld",
        "min_y": -64,
        "monster_spawn_light_level": {
            "type": "minecraft:uniform",
            "value": {
                "min_inclusive": 0,
                "max_inclusive": 7
            }
        },
        "monster_spawn_block_light_limit": 0
    },
    "minecraft:the_nether": {
        "ultrawarm": True,
        "natural": False,
        "coordinate_scale": 8.0,
        "has_skylight": False,
        "has_ceiling": True,
        "ambient_light": 0.1,
        "piglin_safe": True,
        "bed_works": False,
        "respawn_anchor_works": True,
        "has_raids": False,
        "infiniburn": "minecraft:infiniburn_nether",
        "effects": "minecraft:the_nether",
        "min_y": 0,
        "monster_spawn_light_level": {
            "type": "minecraft:uniform",
            "value": {
                "min_inclusive": 0,
                "max_inclusive": 7
            }
        },
        "monster_spawn_block_light_limit": 15
    },
    "minecraft:the_end": {
        "ultrawarm": False,
        "natural": False,
        "coordinate_scale": 1.0,
        "has_skylight": False,
        "has_ceiling": False,
        "ambient_light": 0.0,
        "fixed_time": 18000,
        "piglin_safe": False,
        "bed_works": False,
        "respawn_anchor_works": False,
        "has_raids": False,
        "infiniburn": "minecraft:infiniburn_end",
        "effects": "minecraft:the_end",
        "min_y": 0,
        "monster_spawn_light_level": {
            "type": "minecraft:uniform",
            "value": {
                "min_inclusive": 0,
                "max_inclusive": 7
            }
        },
        "monster_spawn_block_light_limit": 0
    }
}

# 写入每个 dimension_type 文件
for dim, base in dimension_bases.items():
    base_settings = defaults[base].copy()
    base_settings["height"] = 1024
    base_settings["logical_height"] = 959
    if base_settings.get("fixed_time") is None:
        base_settings.pop("fixed_time", None)
    with open(os.path.join(dimtype_dir, f"{dim}.json"), "w") as f:
        json.dump(base_settings, f, indent=2)

# 打包生成的 dimension_type 文件夹
manual_zip_path = "tt_dims1_dimtypes_only.zip"
with zipfile.ZipFile(manual_zip_path, "w") as zipf:
    for root, _, files in os.walk(manual_base_path):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, manual_base_path)
            zipf.write(full_path, rel_path)

manual_zip_path
