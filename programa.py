
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///programa.db")
Base = declarative_base()


class Programa(Base):
    __tablename__ = "Programa"
    id = Column(Integer, primary_key=True)
    pratimas = Column("Pratimas", String)
    serijos = Column("Serijos", Integer)
    pakartojimai = Column("Pakartojimai", Integer)

    def __init__(self, pratimas, serijos, pakartojimai):
        self.pratimas = pratimas
        self.serijos = serijos
        self.pakartojimai = pakartojimai

    def __repr__(self):
        return f"{self.pratimas}, {self.serijos}, {self.pakartojimai}"


class Istorija(Base):
    __tablename__ = "Istorija"
    id = Column(Integer, primary_key=True)
    pratimas = Column("Pratimas", String)
    serijos = Column("Serijos", Integer)
    pakartojimai = Column("Pakartojimai", Integer)
    data = Column("Data", DateTime)
    atlikta = Column("Atlikta", String)

    def __init__(self, pratimas, serijos, pakartojimai, data, atlikta):
        self.pratimas = pratimas
        self.serijos = serijos
        self.pakartojimai = pakartojimai
        self.data = data
        self.atlikta = atlikta

    def __repr__(self):
        return f"{self.pratimas}, {self.serijos}, {self.pakartojimai}, {self.data}, {self.atlikta}"


Base.metadata.create_all(engine)
