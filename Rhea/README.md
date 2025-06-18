# Rhea 数据集

Rhea数据集包含用于生物化学反应预测的详细数据，主要关注生物酶催化反应。数据集包括反应物、产物和催化剂等信息

## 文件列表
```
.
├── README.md
├── small
    ├── test_raw.csv
    └── train_raw.csv
└── large
    ├── test_raw_large.csv
    └── train_raw_large.csv
```

## 数据详情
- 数据分割:
  - small: 包含较小规模的训练和测试数据集
    - `test_raw.csv`: 测试数据 ~9.4k
    - `train_raw.csv`: 训练数据 ~37.6k
  - large: 包含较大规模的训练和测试数据集
    - `test_raw_large.csv`: 测试数据 ~84.6k
    - `train_raw_large.csv`: 训练数据 ~338k
  
- 数据格式: CSV 文件，包含以下列
    | 列名            | 描述                                                                |
  |-----------------|----------------------------------------------------------------------|
  | `reactant` | 一般是这是多个反应物的 SMILES 表达式，中间用英文句点 `.` 分隔，表示这是一个分子集合（molgroup），对应多个反应物    |
  | `product`      | 同样是多个 产物 SMILES，也用 `.` 分隔                                             |
    | `enzyme`     | 酶的一级氨基酸序列（fasta 序列，不含标题行）                                       |

-实例：
```
reactant: O=C1C[C@@H](C2=CC=C(O)C=C2)OC2=CC(O)=CC(O)=C12.O=C1C=CN([C@@H]2O[C@H](COP(=O)([O-])OP(=O)([O-])O[C@H]3O[C@H](CO)[C@@H](O)[C@H](O)[C@H]3O)[C@@H](O)[C@H]2O)C(=O)N1

product: O=C1C=CN([C@@H]2O[C@H](COP(=O)([O-])OP(=O)([O-])[O-])[C@@H](O)[C@H]2O)C(=O)N1.O=C1C[C@@H](C2=CC=C(O)C=C2)OC2=C1C(O)=CC(O[C@@H]1O[C@H](CO)[C@@H](O)[C@H](O)[C@H]1O)=C2.[H+]

enzyme:MVQHRFLLVTFPAQGHINPSLQFAKRLIN...VLKDARH
```