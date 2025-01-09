# data_management/database.py
from sqlalchemy import create_engine, Column, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import Config

Base = declarative_base()

class Patent(Base):
    __tablename__ = 'patents'
    id = Column(String, primary_key=True)
    title = Column(String)
    abstract = Column(Text)
    claims = Column(Text)
    description = Column(Text)
    filing_date = Column(Date)
    inventor = Column(String)
    ipc_class = Column(String)
    embedding = Column(Text)  # 存储向量或引用向量数据库

def get_engine():
    return create_engine(Config.DATABASE_URI)

def create_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()
