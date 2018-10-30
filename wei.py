# coding: utf-8

from gensim.similarities import Similarity
import jieba
from gensim import corpora
from collections import defaultdict
import sqlalchemy
import  json
from sqlalchemy import Table, MetaData,Column, INTEGER, String, Text, text
from sqlalchemy.dialects.mysql.types import TINYINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import create_engine
def funcA():
    Base = declarative_base()

    engine = create_engine("mysql+pymysql://root:cwj@localhost/wei",
                           encoding='utf-8', echo=True, convert_unicode=True)

    class xin3(Base):

        __tablename__ = 'xin3'

        id = Column(INTEGER, primary_key=True)
        title = Column(Text, nullable=False)
        dele = Column(INTEGER)

        def __repr__(self):
            get_data = {"id": self.id, "title": self.title}
            get_data = json.dumps(get_data)
            return get_data


    Base.metadata.create_all(engine)
    Session_class = sessionmaker(bind=engine)
    Session = Session_class()
    #Session.execute('insert into xin3(title,dele) select data_ency.title,dele data_ency from data_ency;')

    my_user1 = Session.query(xin3).filter(xin3.dele == 0).all()
    my_user2 = json.loads(str(my_user1))
    raw_documents = []
    for i in range(1, 90):
        raw_documents.append(str(i-1) + (my_user2[i]['title']))
    print(raw_documents)
    corpora_documents = []
    for item_text in raw_documents:
        item_str = jieba.lcut(item_text)

        corpora_documents.append(item_str)
    dictionary = corpora.Dictionary(corpora_documents)
    corpus = [dictionary.doc2bow(text) for text in corpora_documents]
    similarity = Similarity('-Similarity-index', corpus, num_features=400)
    return dictionary ,similarity


if __name__ == '__main__':

    funcA()

