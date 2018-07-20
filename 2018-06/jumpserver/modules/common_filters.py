#_*_coding:utf-8_*_
__author__ = 'Alex Li'
from  models import models_db
from modules.db_connect import engine,session
from modules.utils import print_err

def bind_hosts_filter(vals):
    print('**>',vals.get('bind_hosts') )
    bind_hosts = session.query(models_db.Bind_Host).filter(models_db.Host.hostname.in_(vals.get('bind_hosts'))).all()
    if not bind_hosts:
        print_err("none of [%s] exist in bind_host table." % vals.get('bind_hosts'),quit=True)
    return bind_hosts

def user_profiles_filter(vals):
    jump_users = session.query(models_db.Jump_User).filter(models_db.Jump_User.username.in_(vals.get('jump_users'))
                                                             ).all()
    if not jump_users:
        print_err("none of [%s] exist in user_profile table." % vals.get('jump_users'),quit=True)
    return  jump_users