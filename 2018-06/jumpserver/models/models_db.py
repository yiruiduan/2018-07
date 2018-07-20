#!/usr/bin/python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column,String,Enum,ForeignKey,DATE,Integer,UniqueConstraint,Table,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import ChoiceType,PasswordType

Base=declarative_base()

# Host_m2m_SshUser=Table("host_m2m_sshuser",Base.metadata,
#                        Column("host_id",Integer,ForeignKey("host.id")),
#                        Column("sshuser_id",Integer,ForeignKey("ssh_user.id"))
#                               )

Jumpuser_m2m_Bind=Table("jumpuser_m2m_bind",Base.metadata,
                       Column("jumpuser_id",Integer,ForeignKey("jump_user.id")),
                       Column("bindhost_id",Integer,ForeignKey("bind_host.id"))
                              )
Bind_m2m_Group=Table("bind_m2m_group",Base.metadata,
                       Column("bindhost_id",Integer,ForeignKey("bind_host.id")),
                       Column("group_id",Integer,ForeignKey("host_group.id"))
                              )
Jumpuser_m2m_Group=Table("jumpuser_m2m_group",Base.metadata,
                       Column("jumpuser_id",Integer,ForeignKey("jump_user.id")),
                       Column("group_id",Integer,ForeignKey("host_group.id"))
                              )

class Host(Base):
    __tablename__="host"
    id=Column(Integer,primary_key=True)
    hostname=Column(String(64),unique=True)
    ip=Column(String(64),unique=True)
    port=Column(Integer,default=22)
    # ssh_users=relationship("Ssh_User",secondary=Host_m2m_SshUser,backref="hosts")
    def __repr__(self):
        return "<Host(id='%s',hostname='%s')>" % (self.id,self.hostname)

class Host_Group(Base):
    __tablename__="host_group"
    id = Column(Integer, primary_key=True)
    name=Column(String(64),unique=True)
    bind_hosts=relationship("Bind_Host",secondary="bind_m2m_group",backref="hostgroups")
    def __repr__(self):
        return "<Host_Group(id='%s',name='%s')>" % (self.id,self.name)


class Ssh_User(Base):
    __tablename__="ssh_user"
    __table_args__ =(UniqueConstraint("username","password","auth_type",name="_user_password_uc"),)
    # AuthType=[
    #     ("ssh-password","SSH/Password"),
    #     ("ssh-key","SSH/KEY")
    # ]
    id = Column(Integer, primary_key=True)
    username=Column(String(32))
    password=Column(String(128))
    # auth_type=Column(ChoiceType(AuthType))
    auth_type=Column(String(255))


    def __repr__(self):
        return "<Ssh_User(id='%s',auth_type='%s',user='%s',password='%s')>" % (self.id,self.auth_type,self.username,self.password)

class Bind_Host(Base):
    """实现远程主机用户关联到了远程主机和主机主
    192.168.1.2  web bj_group"""
    __tablename__="bind_host"
    __table_args__ = (UniqueConstraint("host_id", "sshuser_id", name="_HUG_uc"),)

    id=Column(Integer,primary_key=True)
    host_id=Column(Integer,ForeignKey("host.id"))
    sshuser_id=Column(Integer,ForeignKey("ssh_user.id"))
    # hostgroup_id=Column(Integer,ForeignKey("host_group.id"))

    hosts=relationship("Host",backref="bindhosts")
    sshusers=relationship("Ssh_User",backref="bindhosts")
    # hostgroup=relationship("Host_Group",backref="bindhosts")

    def __repr__(self):
        return "<%s-*-%s-*-%s>"%(self.id,self.hosts.ip,self.sshusers.username)


class  Jump_User(Base):
    __tablename__="jump_user"
    id = Column(Integer, primary_key=True)
    username=Column(String(32),unique=True)
    password=Column(String(128))
    bind_hosts=relationship("Bind_Host",secondary="jumpuser_m2m_bind",backref="jumpusers")
    host_groups=relationship("Host_Group",secondary="jumpuser_m2m_group",backref="jumpusers")
    def __repr__(self):
        return "<Jump_User(id='%s',username='%s')>" % (self.id, self.username)

class AuditLog(Base):
    __tablename__ = 'audit_log'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('ssh_user.id'))
    bind_host_id = Column(Integer,ForeignKey('bind_host.id'))
    action_choices = [
        (0,'CMD'),
        (1,'Login'),
        (2,'Logout'),
        (3,'GetFile'),
        (4,'SendFile'),
        (5,'Exception'),
    ]
    action_choices2 = [
        (u'cmd',u'CMD'),
        (u'login',u'Login'),
        (u'logout',u'Logout'),
        #(3,'GetFile'),
        #(4,'SendFile'),
        #(5,'Exception'),
    ]
    action_type = Column(ChoiceType(action_choices2))
    #action_type = Column(String(64))
    cmd = Column(String(255))
    date = Column(DateTime)

    user_profile = relationship("Ssh_User")
    bind_host = relationship("Bind_Host")
    '''def __repr__(self):
        return "<user=%s,host=%s,action=%s,cmd=%s,date=%s>" %(self.user_profile.username,
                                                      self.bind_host.host.hostname,
                                                              self.action_type,
                                                              self.date)
    '''
'''
class AuditLog(models.Model):
    session = models.ForeignKey(SessionTrack)
    user = models.ForeignKey('UserProfile')
    host = models.ForeignKey('BindHosts')
    action_choices = (
        (0,'CMD'),
        (1,'Login'),
        (2,'Logout'),
        (3,'GetFile'),
        (4,'SendFile'),
        (5,'exception'),
    )
    action_type = models.IntegerField(choices=action_choices,default=0)
    cmd = models.TextField()
    memo = models.CharField(max_length=128,blank=True,null=True)
    date = models.DateTimeField()


    def __unicode__(self):
        return '%s-->%s@%s:%s' %(self.user.user.username,self.host.host_user.username,self.host.host.ip_addr,self.cmd)
    class Meta:
        verbose_name = u'审计日志'
        verbose_name_plural = u'审计日志'

'''



# class AuditLog(Base):
#     __tablename__="audit_log"
#     id = Column(Integer, primary_key=True)
#     pass


