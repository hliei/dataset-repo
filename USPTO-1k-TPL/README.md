# USPTO-1k-TPL

USPTO-1K-TPL，提取自美国专利商标局（USPTO）公开数据，并且提取最常见的 1,000 个反应模板作为分类标签，专注于反应模板（Template）研究

## 数据明细
- 数据规模：约 445,000 条反应记录

- 类别数量：1,000 个模板标签（Template）

- 数据集切割
  - 训练集：约 400,000 条反应记录
  - 测试集：约 45,000 条反应记录

  
### 文件
```
.
├── README.md
├── raw
    ├── uspto_1k_TPL_test.tsv
    └── uspto_1k_TPL_train.tsv
├── label_template.json
├── test.json
└── train.json
```
### 数据格式
- [uspto_1k_TPL_train.tsv](USPTO-1k-TPL/raw/uspto_1k_TPL_train.tsv) 和 [uspto_1k_TPL_test.tsv](USPTO-1k-TPL/raw/uspto_1k_TPL_test.tsv)：原始数据文件，包含大量字段
  - 核心化学信息：
    - `mapped_rxn`, `canonical_rxn`, `reactants`, `products`: 提供反应物、产物和试剂的 SMILES 表示，带原子映射
    - `original_rxn`, `canonical_rxn_with_fragment_info`: 提供原始反应和标准化后的 SMILES 表示
    - `retro_template`, `template_hash`：定义逆合成模板，是 USPTO-1K-TPL 的重点，适合模板分类和预测
    - `fragments`：标识反应中心，辅助分析键变化
  - 元数据：
    - `source`, `year`, `ID`：追踪专利来源和时间。
    - `reaction_hash`：确保反应唯一性。
    - `confidence`, `selectivity`, `outcomes`：评估数据质量和反应特性
  
- [train.json](USPTO-1k-TPL/train.json) 和 [test.json](USPTO-1k-TPL/test.json)：通过提取raw里面的原始数据生成的 JSON 格式数据文件，仅仅包含训练和测试集的 Reaction SMILES (canonical_rxn)和模板标签

- [label_template.json](USPTO-1k-TPL/label_template.json)：通过提取raw里面的 `retro_template` 和 `label` 的映射关系
  - 包含 1,000 个模板的 SMILES 模式 与 label数字的映射
