import os
import zipfile

# 基础路径
base_path = "tt_dims1_datapack"
functions_path = os.path.join(base_path, "data", "tt_dims1", "functions")
os.makedirs(functions_path, exist_ok=True)
vanilla_functions_path = os.path.join(functions_path, "mc");
os.makedirs(vanilla_functions_path, exist_ok=True)

# 为每个维度创建单独的传送函数
tp_coords = "~ ~ ~"
dimension_keys = ["ovw", "ovw_alignflat", "net", "end", "void"]
vanilla_dimension_key_values = {
    "ovw": "overworld", 
    "net": "the_nether", 
    "end": "the_end"
}

for key in dimension_keys:
    func_path = os.path.join(functions_path, f"tp_{key}.mcfunction")
    with open(func_path, "w") as f:
        f.write(f"execute in tt_dims1:{key} run tp @p {tp_coords}")

for key in vanilla_dimension_key_values.keys():
    func_path = os.path.join(vanilla_functions_path, f"tp_{key}.mcfunction")
    with open(func_path, "w") as f:
        f.write(f"execute in minecraft:{vanilla_dimension_key_values[key]} run tp @p {tp_coords}")

# 重新打包数据包
zip_path = "tt_dims1_datapack_tp_functions.zip"
with zipfile.ZipFile(zip_path, "w") as zipf:
    for root, _, files in os.walk(base_path):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_path)
            zipf.write(full_path, rel_path)

zip_path
