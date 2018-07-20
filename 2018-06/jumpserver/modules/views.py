#!/usr/bin/python3
# -*- coding: utf-8 -*-
from models import models_db
from modules.db_connect import engine,session
from modules.utils import print_err,yaml_parser
from modules import common_filters
from modules import ssh_login

def auth():
    count=0
    while count<3:
        username=input("请输入您的用户名：")
        if len(username) ==0:continue
        password=input("请输入您的密码：")
        if len(password) ==0:continue
        user_obj=session.query(models_db.Jump_User).filter(
            models_db.Jump_User.username==username,
            models_db.Jump_User.password==password
        ).first()
        if user_obj:
            return user_obj
        else:
            print("wrong username or password, you have %s more chances." % (3 - count - 1))
            count += 1
    else:
        print("too many attempts")

def welcome_msg(user):
    WELCOME_MSG = '''\033[32;1m
    ------------- Welcome [%s] login jumpserver -------------
    \033[0m'''%  user.username
    print(WELCOME_MSG)

def log_recording(user_obj,bind_host_obj,logs):
    '''
    flush user operations on remote host into DB
    :param user_obj:
    :param bind_host_obj:
    :param logs: list format [logItem1,logItem2,...]
    :return:
    '''
    print("\033[41;1m--logs:\033[0m",logs)

    session.add_all(logs)
    session.commit()

def start_session(argvs):
    print('going to start sesssion ')
    user = auth()
    if user:
        welcome_msg(user)
        # print(user.bind_hosts)
        # print(user.host_groups)
        exit_flag = False
        while not exit_flag:
            if user.bind_hosts:
                print('\033[32;1mz.\tungroupped hosts (%s)\033[0m' %len(user.bind_hosts) )
            for index,group in enumerate(user.host_groups):
                print('\033[32;1m%s.\t%s (%s)\033[0m' %(index,group.name,  len(group.bind_hosts)) )

            choice = input("[%s]:" % user.username).strip()
            if len(choice) == 0:continue
            if choice == 'z':
                print("------ Group: ungroupped hosts ------" )
                for index,bind_host in enumerate(user.bind_hosts):
                    print("  %s.\t%s@%s(%s)"%(index,
                                              bind_host.sshusers.username,
                                              bind_host.hosts.hostname,
                                              bind_host.hosts.ip,
                                              ))
                print("----------- END -----------" )
            elif choice.isdigit():
                choice = int(choice)
                if choice < len(user.host_groups):
                    print("------ Group: %s ------"  % user.host_groups[choice].name )
                    for index,bind_host in enumerate(user.host_groups[choice].bind_hosts):
                        print("  %s.\t%s@%s(%s)"%(index,
                                                  bind_host.sshusers.username,
                                                  bind_host.hosts.hostname,
                                                  bind_host.hosts.ip,
                                                  ))
                    print("----------- END -----------" )

                    #host selection
                    while not exit_flag:
                        user_option = input("[(b)back, (q)quit, select host to login]:").strip()
                        if len(user_option)==0:continue
                        if user_option == 'b':break
                        if user_option == 'q':
                            exit_flag=True
                        if user_option.isdigit():
                            user_option = int(user_option)
                            if user_option < len(user.host_groups[choice].bind_hosts) :
                                print('host:',user.host_groups[choice].bind_hosts[user_option])
                                # print('audit log:',user.host_groups[choice].bind_hosts[user_option].audit_logs)
                                ssh_login.ssh_login(user,
                                                    user.host_groups[choice].bind_hosts[user_option],
                                                    session,
                                                    log_recording)
                else:
                    print("no this option..")


def create_hosts(argvs):
    '''
    create hosts
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        hosts_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new hosts file>",quit=True)
    source = yaml_parser(hosts_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models_db.Host(hostname=key,ip=val.get('ip_addr'), port=val.get('port') or 22)
            session.add(obj)
        session.commit()

def create_sshusers(argvs):
    '''
    create hosts
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        hosts_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new hosts file>",quit=True)
    source = yaml_parser(hosts_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models_db.Ssh_User(username=val.get("username"),password=val.get('password'), auth_type=val.get('auth_type') or 22)
            session.add(obj)
        session.commit()

def create_users(argvs):
    '''
    create little_finger access user
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        user_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreateusers -f <the new users file>",quit=True)

    source = yaml_parser(user_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models_db.Jump_User(username=key,password=val.get('password'))
            # if val.get('groups'):
            #     groups = session.query(models_db.Host_Group).filter(models_db.Host_Group.name.in_(val.get('groups'))).all()
            #     if not groups:
            #         print_err("none of [%s] exist in group table." % val.get('groups'),quit=True)
            #     obj.groups = groups
            # if val.get('bind_hosts'):
            #     bind_hosts = common_filters.bind_hosts_filter(val)
            #     obj.bind_hosts = bind_hosts
            # #print(obj)
            session.add(obj)
        session.commit()

def create_groups(argvs):
    '''
    create groups
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        group_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreategroups -f <the new groups file>",quit=True)
    source = yaml_parser(group_file)
    if source:
        for key,val in source.items():
            print(key,val)
            obj = models_db.Host_Group(name=key)
            if val.get('bind_hosts'):
                bind_hosts = common_filters.bind_hosts_filter(val)
                obj.bind_hosts = bind_hosts

            if val.get('jump_users'):
                user_profiles = common_filters.user_profiles_filter(val)
                obj.user_profiles = user_profiles
            session.add(obj)
        session.commit()

def create_bindhosts(argvs):
    '''
    create bind hosts
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        bindhosts_file  = argvs[argvs.index("-f") +1 ]
    else:
        print_err("invalid usage, should be:\ncreate_hosts -f <the new bindhosts file>",quit=True)
    source = yaml_parser(bindhosts_file)
    if source:
        for key,val in source.items():
            #print(key,val)
            host_obj = session.query(models_db.Host).filter(models_db.Host.hostname==val.get('hostname')).first()
            assert host_obj
            for item in val['ssh_users']:
                # print("******",item )
                assert item.get('auth_type')
                if item.get('auth_type') == 'ssh-password':
                    sshuser_obj = session.query(models_db.Ssh_User).filter(
                                                        models_db.Ssh_User.username==item.get('username'),
                                                        models_db.Ssh_User.password==item.get('password')
                                                    ).first()
                else:
                    sshuser_obj = session.query(models_db.Ssh_User).filter(
                                                        models_db.Ssh_User.username==item.get('username'),
                                                        models_db.Ssh_User.auth_type==item.get('auth_type'),
                                                    ).first()
                if not sshuser_obj:
                    print_err("RemoteUser obj %s does not exist." % item,quit=True )
                bindhost_obj = models_db.Bind_Host(host_id=host_obj.id,sshuser_id=sshuser_obj.id)
                session.add(bindhost_obj)

                #for groups this host binds to
                if source[key].get('groups'):
                    group_objs = session.query(models_db.Host_Group).filter(models_db.Host_Group.name.in_(source[key].get('groups') )).all()
                    assert group_objs
                    print('groups:', group_objs)
                    bindhost_obj.hostgroups = group_objs
                #for jump_users this host binds to
                if source[key].get('jump_users'):
                    jumpuser_objs = session.query(models_db.Jump_User).filter(models_db.Jump_User.username.in_(
                        source[key].get('jump_users')
                    )).all()
                    assert jumpuser_objs
                    print("jump_users:",jumpuser_objs)
                    bindhost_obj.jumpusers = jumpuser_objs
                #print(bindhost_obj)
        session.commit()

def syncdb(argvs):
    print("Syncing DB....")
    models_db.Base.metadata.create_all(engine) #创建所有表结构