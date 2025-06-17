# 提取
import pandas as pd

# 输入和输出文件路径
input_file = "USPTO-1k-TPL/raw/uspto_1k_TPL_train_valid.tsv"  # 替换为您的实际文件路径
output_file = "USPTO-1k-TPL/train.json"  # 输出文件路径

try:
    # 读取 TSV 文件，仅加载需要的列
    df = pd.read_csv(input_file, sep='\t', usecols=['canonical_rxn', 'labels'])

    # 重命名列（规范化输出）
    df = df.rename(columns={'canonical_rxn': 'reaction_smiles'})

    # 保存到新的 JSON 文件
    df.to_json(output_file, orient="records", lines=True)
    print(f"成功提取 'reaction_smiles' 和 'labels'，保存到 {output_file}")

    # 显示前几行结果
    print("\n提取结果的前 5 行：")
    print(df.head())

except FileNotFoundError:
    print(f"错误：文件 {input_file} 不存在，请检查路径。")
except KeyError as e:
    print(f"错误：缺少列 {e}，请检查 TSV 文件是否包含 'canonical_rxn' 和 'labels'。")
except Exception as e:
    print(f"发生错误：{e}")