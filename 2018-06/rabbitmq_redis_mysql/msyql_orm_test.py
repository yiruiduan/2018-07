#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,Column,String,DATE,TIMESTAMP,Enum
from sqlalchemy.orm import sessionmaker
engine=create_engine("mysql+pymysql://yiruiduan:yiruiduan@192.168.1.115/oldboy",encoding="utf-8",echo=True)
BASE=declarative_base()

class Student(BASE):
    __tablename__= "student"
    stu_id=Column(Integer,primary_key=True)
    name=Column(String(32),nullable=False)
    age=Column(Integer,nullable=False)
    register_date=Column(DATE,nullable=False)
    time_stamp=Column(TIMESTAMP,nullable=False)
    sex=Column(Enum('M','F'),nullable=False,default="M")

    def __repr__(self):
        return "<%s name:%s>"%(self.stu_id,self.name)

class USER(BASE):
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    name=Column(String(32))
    password=Column(String(64))

    def __repr__(self):
        return "<%s name:%s>"%(self.id,self.name)

BASE.metadata.create_all(engine)
session_class=sessionmaker(bind=engine)
session=session_class()
# user_obj=Student(name="hehe",age=99,register_date="2031-11-11")
# session.add(user_obj)
# session.commit()
print(session.query(USER,Student).filter(Student.stu_id==USER.id).filter(Student.name==USER.name).all())
# myuser=session.query(USER).filter_by().first()
# myuser.name="zhangye"
# session.commit()
# print(myuser)
# print(session.query(USER).join(Student,).all())
