import pandas as pd

# 读取 parquet 文件
df = pd.read_parquet("file_name.parquet")

# 查看内容结构
print(df.head())

# 保存为 JSONL
df.to_json("file_name.jsonl", orient="records", lines=True)

# 或保存为 CSV
df.to_csv("file_name.csv", index=False)