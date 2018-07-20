#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Enum,ForeignKey,DATE,Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
db_host="192.168.1.115"
db_user="yiruiduan"
db_password="yiruiduan"
db="oldboy"
engine=create_engine("mysql+pymysql://%s:%s@%s/%s?charset=utf8"%(db_user,db_password,db_host,db),encoding="utf-8")

Base=declarative_base()

book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books')

    def __repr__(self):
        return self.name,self.authors.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name

Base.metadata.create_all(engine)