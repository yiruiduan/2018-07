#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,DATE,String,Integer,Enum,union,TIMESTAMP,ForeignKey
from  sqlalchemy.orm import sessionmaker,relationship

engine=create_engine("mysql+pymysql://yiruiduan:yiruiduan@192.168.1.115/oldboy",encoding="utf-8")
Base=declarative_base()

# class Family(Base):
#     __tablename__="family"
#     fm_id=Column(Integer,primary_key=True)
#     name=Column(String(40),nullable=False,unique=True)
#     sex=Column(Enum("M","F"),default="M",nullable=False)
#     age=Column(Integer,nullable=False)
#     birthday=Column(DATE,nullable=False,default="2018-07-12")
#
#     def __repr__(self):
#         return "<%s name:%s>"%(self.fm_id,self.name)

class Student(Base):
    __tablename__= "student"
    stu_id=Column(Integer,primary_key=True)
    name=Column(String(32),nullable=False)
    # age=Column(Integer,nullable=False)
    register_date=Column(DATE,nullable=False)
    # time_stamp=Column(TIMESTAMP,nullable=False)
    # sex=Column(Enum('M','F'),nullable=False,default="M")

    def __repr__(self):
        return "<%s name:%s>"%(self.stu_id,self.name)

class StudyRecord(Base):
    __tablename__="study_record"
    id=Column(Integer,primary_key=True)
    day=Column(Integer,nullable=False)
    status=Column(String(32),nullable=False)
    stu_id=Column(Integer,ForeignKey("student.stu_id"))

    student=relationship("Student",backref="my_study_record")

    def __repr__(self):
        return "<name:%s %sday status:%s>"%(self.student.name,self.day,self.status)


Base.metadata.create_all(engine)
session_class=sessionmaker(bind=engine)
session=session_class()
# s1=Student(name="yiruiduan",register_date="2018-07-13")
# s2=Student(name="yinuo",register_date="2018-07-14")
# s3=Student(name="zhangye",register_date="2018-07-10")
# s4=Student(name="yijinchen",register_date="2018-07-10")
# study_record1=StudyRecord(day=1,status="yes",stu_id=1)
# study_record2=StudyRecord(day=2,status="no",stu_id=1)
# study_record3=StudyRecord(day=3,status="yes",stu_id=1)
# study_record4=StudyRecord(day=4,status="yes",stu_id=1)
# study_record5=StudyRecord(day=1,status="yes",stu_id=2)
# study_record6=StudyRecord(day=2,status="yes",stu_id=2)
# study_record7=StudyRecord(day=1,status="yes",stu_id=3)
# study_record8=StudyRecord(day=1,status="yes",stu_id=4)
#
# session.add_all([s1,s2,s3,s4,study_record1,study_record2,study_record3,study_record4,study_record5,study_record6,study_record7,study_record8])
# session.commit()

# # user_obj=Family(name="zhangye",sex="F",age="29",birthday="1989-04-21")
# # user_obj1=Family(name="yinuo",sex="F",age="5",birthday="2013-09-24")
# # session.add(user_obj)
# # session.add(user_obj1)
# # session.commit()
# data=session.query(Family,Student).filter(Family.name==Student.name).all()
# print(data)
data=session.query(Student).filter_by(name="zhangye").first().my_study_record
print(data[0].status)
print(data)
