import os
import zipfile

# 基础路径
base_path = "tt_dims1_datapack"
functions_path = os.path.join(base_path, "data", "tt_dims1", "functions")
os.makedirs(functions_path, exist_ok=True)

# 为每个维度创建单独的传送函数
tp_coords = "0 70 0"
dimension_keys = ["ovw", "ovw_alignflat", "net", "end", "void"]

for key in dimension_keys:
    func_path = os.path.join(functions_path, f"tp_{key}.mcfunction")
    with open(func_path, "w") as f:
        f.write(f"tp @p {tp_coords} tt_dims1:{key}")

# 重新打包数据包
zip_path = "tt_dims1_datapack_tp_functions.zip"
with zipfile.ZipFile(zip_path, "w") as zipf:
    for root, _, files in os.walk(base_path):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_path)
            zipf.write(full_path, rel_path)

zip_path
