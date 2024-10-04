# 分词表Tokenizer

我们透过Google的分词器模块[sentencepiece](https://github.com/google/sentencepiece/tree/master)自定义了一个拥有30000个词汇量的分词表。

分词表使用示例[test_sp.ipynb](test_sp.ipynb)

```python
import sentencepiece as sp

spm = sp.SentencePieceProcessor()
spm.Load("tokenizer.model")

ids = spm.Encode("我爱北京天安门")
print(ids)
spm.Decode(ids)
```

```bash
>>>[12211, 25691, 916, 25343, 25347, 25478]
>>>'我爱北京天安门'
```


