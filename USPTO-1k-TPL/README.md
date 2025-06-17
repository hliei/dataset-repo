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
  - 实例：
    ```
    {"reaction_smiles":"C1CCOC1.CC(C)(C)OC(=O)NCC(=O)NCC(=O)O.CCCCCCCC\/C=C\\CCCCCCCC(=O)N(CCCCCCCCCCCCCC)[C@]1(N)O[C@H](CO)[C@@H](O)[C@H](O)[C@H]1C(=O)[C@@H](N)CC(C)C>>CCCCCCCC\/C=C\\CCCCCCCC(=O)N(CCCCCCCCCCCCCC)[C@]1(N)O[C@H](CO)[C@@H](O)[C@H](O)[C@H]1C(=O)[C@H](CC(C)C)NC(=O)CNC(=O)CNC(=O)OC(C)(C)C","labels":645}
    {"reaction_smiles":"CCN(CC)CCOc1ccc(Cn2c3ccc(OC)cc3c3oc4cc(OCc5ccccc5)ccc4c32)cc1.CCO.[Pd]>>CCN(CC)CCOc1ccc(Cn2c3ccc(OC)cc3c3oc4cc(O)ccc4c32)cc1","labels":23}
    {"reaction_smiles":"CCN(C(C)C)C(C)C.CS(=O)(=O)Cl.C[C@@H]1CCC[C@H](C)N1c1nnc2ccc(O[C@@H]3CC[C@H](NC(=O)Nc4cc(C(C)(C)C)nn4-c4cncc(OCCO)c4)c4ccccc43)cn12.ClCCl>>C[C@@H]1CCC[C@H](C)N1c1nnc2ccc(O[C@@H]3CC[C@H](NC(=O)Nc4cc(C(C)(C)C)nn4-c4cncc(OCCOS(C)(=O)=O)c4)c4ccccc43)cn12","labels":0}
    {"reaction_smiles":"CC(C)(C)[Si](C)(C)OCCn1ccc(N)n1.Cc1cccc(C)n1.ClCCl.O=C(Cl)C(=O)Cl.O=C1CC[C@H](C[C@@H](C(=O)O)c2cccc(C(F)(F)F)c2)C1>>CC(C)(C)[Si](C)(C)OCCn1ccc(NC(=O)[C@H](C[C@H]2CCC(=O)C2)c2cccc(C(F)(F)F)c2)n1","labels":795}
    {"reaction_smiles":"CCOC(C)=O.CO.COc1cc(C(=O)O)c(Cl)cc1Br.C[Si](C)(C)C=[N+]=[N-]>>COC(=O)c1cc(OC)c(Br)cc1Cl","labels":195}
    ```

- [label_template.json](USPTO-1k-TPL/label_template.json)：通过提取raw里面的 `retro_template` 和 `label` 的映射关系
  - 包含 1,000 个模板的 SMILES 模式 与 label数字的映射
  - eg.
    ```
    {
    "0": "(Cl-[S;H0;D4;+0:1](-[C;D1;H3:2])(=[O;D1;H0:3])=[O;D1;H0:4]).([C:5]-[OH;D1;+0:6])>>([C:5]-[O;H0;D2;+0:6]-[S;H0;D4;+0:1](-[C;D1;H3:2])(=[O;D1;H0:3])=[O;D1;H0:4])",
    "1": "(O=[N+;H0;D3:1](-[O-])-[c:2])>>([NH2;D1;+0:1]-[c:2])",
    ... ... 
    ```
