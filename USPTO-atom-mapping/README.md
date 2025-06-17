# USPTO-atom_mapping
从美国专利文本中自动化提取的原始反应记录
- 种类：
  - uspto-50k: ～50k 条记录
  - uspto-full: ～1.1M 条记录

## 文件
    - raw_USPTO_50k: ～50k 条包含了原子映射Reaction SMILES的记录
    - raw_USPTO_FUll:～1.1M 条包含了原子映射Reaction SMILES的记录

## 数据格式
- **CSV 格式**：UTF-8 编码，逗号分隔。
- 实例：
    ```text
    remmaped_reaction: Cl[c:1]1[n:11][c:12](-[c:13]2[cH:14][cH:15][n:16][o:17]2)[n:18][c:19]2[s:20][cH:21][c:22]([CH3:23])[c:24]12.[NH2:2][CH2:3][c:4]1[cH:10][cH:9][c:7]([F:8])[cH:6][cH:5]1>>[c:1]1([NH:2][CH2:3][c:4]2[cH:5][cH:6][c:7]([F:8])[cH:9][cH:10]2)[n:11][c:12](-[c:13]2[cH:14][cH:15][n:16][o:17]2)[n:18][c:19]2[s:20][cH:21][c:22]([CH3:23])[c:24]12,
    confidence: TRUE
    ```
- **列说明**：
    | 列名            | 描述                                                                |
  |-----------------|----------------------------------------------------------------------|
  | mapped_reaction | 化学反应的 Reaction SMILES 表示，格式为 `reactants>>product`，包含原子映射    |
  | confidence    | 原子映射的可信度，布尔值             |