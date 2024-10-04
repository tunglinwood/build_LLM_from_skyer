# Preprocess 预处理

在预训练之前，我们需要对数据集(或称**文料corpus**)进行预处理，将文料中的文字透过[**分词器tokenizer**](tokenizer)进行编码，最后输出成能够投入预训练的数据集。

以下为[preprocess_demo.ipynb](preprocess_demo.ipynb)中的示例。
```python
from preprocess import Preprocess

prep = Preprocess(tokenizer="../tokenizer/tokenizer.model",dst_dir="../dataset/token")
prep("../dataset/2021-43_zh_head_0001.jsonl")
```
```
>>> 2021-43_zh_head_0001 is being processed...
1088812it [13:12, 1373.73it/s]
../dataset/token/2021-43_zh_head_0001 is saved...
```
