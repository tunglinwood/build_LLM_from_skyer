
import sentencepiece as spm

params = """
--input=text.txt
--model_type=bpe
--model_prefix=test_tokenizer 
--vocab_size=30000
--character_coverage=0.9995
--train_extremely_large_corpus=true
--pad_id=0
--unk_id=1
--bos_id=2
--eos_id=3
--unk_piece=<unk>
--bos_piece=<s>
--eos_piece=</s>
--pad_piece=<pad>
--max_sentence_length=100000000
--split_by_unicode_script=true
--split_by_number=true
--split_by_whitespace=true
--split_digits=true
--required_chars="\\n\\r\\t"
--normalization_rule_name=nmt_nfkc
""".replace("\n"," ")

spm.SentencePieceTrainer.Train(params)