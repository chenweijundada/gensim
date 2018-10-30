# coding: utf-8
from kaishi import wei
from gensim.similarities import Similarity
import jieba
from gensim import corpora
from collections import defaultdict
dictionary ,similarity = wei.funcA()
print('使用例子')
test_data_1 = '石油是什么'
test_cut_raw_1 = jieba.lcut(test_data_1)

print(test_cut_raw_1)
test_corpus_1 = dictionary.doc2bow(test_cut_raw_1)
similarity.num_best = 2
print(similarity[test_corpus_1])
test_data_2 = '地震和海啸原有'
test_cut_raw_2 = jieba.lcut(test_data_2)

print(test_cut_raw_2)
test_corpus_2 = dictionary.doc2bow(test_cut_raw_2)
similarity.num_best = 2
print(similarity[test_corpus_2])
test_data_3= '人类 威胁 海景 生存'
test_cut_raw_3 = jieba.lcut(test_data_3)

print(test_cut_raw_3)
test_corpus_3 = dictionary.doc2bow(test_cut_raw_3)
similarity.num_best = 2
print(similarity[test_corpus_3])
test_data_4= ' 石油 自然界 物质 '
test_cut_raw_4 = jieba.lcut(test_data_4 )

print(test_cut_raw_4)
test_corpus_4 = dictionary.doc2bow(test_cut_raw_4)
similarity.num_best = 2
print(similarity[test_corpus_4])
def funcB():
    str1 = str(input('输入'))
    test_cut_raw_1 = jieba.lcut(str1)
    test_corpus_1 = dictionary.doc2bow(test_cut_raw_1)
    similarity.num_best = 2
    print(similarity[test_corpus_1])
if __name__ == '__main__':

    funcB()



