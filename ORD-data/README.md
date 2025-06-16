# ORD 数据集

ORD（Open Reaction Database）数据集包含用于化学反应预测的大规模训练和测试数据，包含了反应细节

## 文件列表
- **orderly_retro_train.parquet**（496.31 MB）：训练数据的 Parquet 格式，可以通过python.pandas转化格式
- **orderly_retro_test.parquet**（50.83 MB）：测试数据的 Parquet 格式

## 数据格式
- **CSV 格式**：UTF-8 编码，逗号分隔。
  - 每行表示一条反应实例，**重要**的字段包括：
    - `agent_##`：化学试剂（催化剂、添加剂等）
    - `procedure_details`：实验步骤的详细描述(提取文献的原文段落)，包括反应条件、溶剂、温度等
    - `rxn_str`：带有原子映射的Reaction SMILES
    - `solvent_##`：反应溶剂
    - `temperature` & `yield_000`：反应的温度和产率
- 示例 

```text
original_index: 1082916
reactant_000: Cc1sc(C(=O)O)cc1CC(C)C
reactant_001: CCc1cc(C(=N)NO)cc(C)c1CCC(=O)O
product_000: CCc1cc(-c2noc(-c3cc(CC(C)C)c(C)s3)n2)cc(C)c1CCC(=O)O
agent_000: CN(C)C(On1nnc2ccccc21)=[N+](C)C
agent_001: F[B-](F)(F)F
agent_002...agent_016: None
solvent_000: ClCCl
solvent_001: CCN(C(C)C)C(C)C
solvent_002...solvent_010: None
temperature: 25.0
rxn_time: 16.0
yield_000: 15.6
rxn_str: [CH2:1]([C:5]1[CH:6]=[C:7]([C:11]([OH:13])=O)[S:8][C:9]=1[CH3:10])[CH:2]([CH3:4])[CH3:3].CCN(C(C)C)C(C)C.CN(C(ON1N=NC2C=CC=CC1=2)=[N+](C)C)C.[B-](F)(F)(F)F.[CH2:45]([C:47]1[CH:52]=[C:51]([C:53](=[NH:56])[NH:54]O)[CH:50]=[C:49]([CH3:57])[C:48]=1[CH2:58][CH2:59][C:60]([OH:62])=[O:61])[CH3:46]>C(Cl)Cl>[CH2:45]([C:47]1[CH:52]=[C:51]([C:53]2[N:54]=[C:11]([C:7]3[S:8][C:9]([CH3:10])=[C:5]([CH2:1][CH:2]([CH3:3])[CH3:4])[CH:6]=3)[O:13][N:56]=2)[CH:50]=[C:49]([CH3:57])[C:48]=1[CH2:58][CH2:59][C:60]([OH:62])=[O:61])[CH3:46]
procedure_details: To a solution of 4-isobutyl-5-methyl-thiophene-2-carboxylic acid (126 mg, 637 μmol) in DCM (5 mL), DIPEA (249 mg, 1.93 mmol) is added followed TBTU (202 mg, 628 μmol)... (全文略)
date_of_experiment: 2011-01-01 00:08:00

```

- **具体每个列**：
  | 列名                  | 描述                                                                 |
  |-----------------------|----------------------------------------------------------------------|
  | original_index        | 数据记录的原始索引，用于追踪数据来源                                |
  | agent_000 至 agent_016| 化学试剂（催化剂、添加剂等） |
  | date_of_experiment    | 实验日期，格式为 `YYYY-MM-DD HH:MM:SS`                             |
  | extracted_from_file   | 数据提取的文件标识符。                                               |
  | grant_date            | 专利授权日期。                                                       |
  | is_mapped             | 是否包含原子映射                                      |
  | procedure_details     | 实验步骤的详细描述(提取文献的原文段落)，包括反应条件、溶剂、温度等                       |
  | product_000           | 主要产物，使用 SMILES 表示。                                          |
  | reactant_000, reactant_001 | 反应物，使用 SMILES 表示。                                       |
  | rxn_str               | 反应方程式，包含反应物、试剂和产物的 Reaction SMILES 格式           |
  | rxn_time              | 反应时间（小时）                                                   |
  | solvent_000 至 solvent_010 | 反应溶剂，如 `CCO`（乙醇）                   |
  | temperature           | 反应温度（摄氏度）                                                 |
  | yield_000             | 产率（百分比）