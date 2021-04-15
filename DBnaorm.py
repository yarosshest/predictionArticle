import numpy as np
import sqlalchemy
from sqlalchemy import create_engine, DateTime, func, Boolean, Float, PickleType
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *

# расположение БД
engine = create_engine('sqlite:///dblp.db', echo=False)
Base = declarative_base()
meta = MetaData()


# Таблица публикаций
class Papers(Base):
    __tablename__ = 'Papers'
    id = Column(Integer, primary_key=True)
    authors = Column(PickleType)
    title = Column(String)
    year = Column(Integer)
    n_citation = Column(Integer)
    page_start = Column(Integer)
    page_end = Column(Integer)
    doc_type = Column(String)
    publisher = Column(String)
    volume = Column(Integer)
    issue = Column(Integer)
    references = Column(PickleType)
    indexed_abstract = Column(PickleType)
    fos = Column(PickleType)
    venue = Column(PickleType)
    alias_ids = Column(PickleType)


# Логика работы с БД
class DatabaseFuction(object):
    def get_data(self, size):
        data = []
        x = []
        y = []
        session = sessionmaker(bind=engine)()
        # x_data = session.query(Papers.authors, Papers.title, Papers.year, Papers.page_start, Papers.page_end,
        #                        Papers.doc_type, Papers.publisher, Papers.volume, Papers.issue, Papers.references,
        #                        Papers.indexed_abstract, Papers.fos, Papers.venue, Papers.alias_ids).limit(15).all()
        x_data = session.query(Papers.title, Papers.year, Papers.page_start, Papers.page_end,
                               Papers.doc_type, Papers.publisher, Papers.volume, Papers.issue).limit(size).all()
        y_data = session.query(Papers.n_citation).limit(size).all()
        for u in x_data:
            if not (u[2] == ''):
                try:
                    k = int(u[2])
                except ValueError:
                    print(u[2])
            x.append(u)
        for u in y_data:
            y.append(u)

        data.append(x)
        data.append(y)
        session.close()
        return data


# Создание обьекта для работы с БД
def createBd():
    Base.metadata.create_all(engine)
    return DatabaseFuction()


if __name__ == '__main__':
    db = createBd()
    Base.metadata.create_all(engine)
    Base = sqlalchemy.ext.declarative.declarative_base()
    print(Base.metadata.tables.keys())