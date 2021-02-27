import numpy as np
from sqlalchemy import create_engine, DateTime, func, Boolean, Float, PickleType
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *

# расположение БД
engine = create_engine('sqlite:///bdMiner.db', echo=False)
Base = declarative_base()
meta = MetaData()


# Таблица авторов
class Authors(Base):
    __tablename__ = 'Authors'
    id = Column(Integer, primary_key=True)
    id_in_bd = Column(String)
    name = Column(String)
    org = Column(PickleType)


# Таблица публикаций
class Papers(Base):
    __tablename__ = 'Papers'
    id = Column(Integer, primary_key=True)
    id_in_bd = Column(String)
    title = Column(String)
    authors = Column(PickleType)
    venue_id = Column(String)
    venue_type = Column(String)
    venue_raw = Column(String)
    year = Column(String)
    keywords = Column(PickleType)
    references = Column(PickleType)
    n_citation = Column(Integer)
    doc_type = Column(String)
    lang = Column(String)
    publisher = Column(String)
    abstract = Column(String)
    indexed_abstract = Column(PickleType)
    issn = Column(String)
    isbn = Column(String)
    doi = Column(String)
    pdf = Column(String)
    url = Column(String)


# Таблица связей
class Authorships(Base):
    __tablename__ = 'Authorships'
    id = Column(Integer, primary_key=True)
    Author_id = Column(String, ForeignKey('Authors.id_in_bd'))
    Paper_id = Column(String, ForeignKey('Papers.id_in_bd'))


# Логика работы с БД
class DatabaseFuction(object):

    def checPaper(self, id):
        session = sessionmaker(bind=engine)()
        check = session.query(Papers).filter(Papers.id_in_bd == str(id)).all()

        resp = False
        if len(check) == 0:
            resp = True

        session.close()
        return resp


    def addPaper(self, paper):
        session = sessionmaker(bind=engine)()
        check = session.query(Papers).filter(Papers.id_in_bd == str(paper.id_in_bd)).all()

        resp = False
        if len(check) == 0:
            session.add(paper)
            session.commit()
            resp = True

        session.close()
        return resp

    def addAuthor(self, author):
        session = sessionmaker(bind=engine)()
        check = session.query(Authors).filter(Authors.id_in_bd == author.id_in_bd).all()

        resp = False
        if len(check) == 0:
            session.add(author)
            session.commit()
            resp = True

        session.close()
        return resp

    def addAuthorship(self, Author_id, Paper_id):
        session = sessionmaker(bind=engine)()
        check = session.query(Authorships).filter(Authorships.Author_id == Author_id, Authorships.Paper_id ==Paper_id).all()

        resp = False
        if len(check) == 0:
            Authorship = Authorships()
            Authorship.Author_id = Author_id
            Authorship.Paper_id = Paper_id
            session.add(Authorship)
            session.commit()
            resp = True

        session.close()
        return resp

    def getPaper (self, id):
        session = sessionmaker(bind=engine)()
        check = session.query(Papers).filter(Papers.id_in_bd == id).first()
        session.close()
        return check




# Создание обьекта для работы с БД
def createBd():
    Base.metadata.create_all(engine)
    return DatabaseFuction()


if __name__ == '__main__':
    db = createBd()
