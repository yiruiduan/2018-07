from sqlalchemy.ext.declarative import declarative_base, declared_attr
from collections.abc import Mapping

def combine_args(argss):
    '''first has priority'''
    l = []
    d = {}
    for a in argss:
        if callable(a):
            a = a()
        if len(a) and isinstance(a[-1], Mapping):
            for k,v in a[-1].items():
                d.setdefault(k, v)
            l.extend(a[:-1])
        else:
            l.extend(a)
    if d: l.append(d)
    return tuple(l)

def combine_args_helper(cls, name, localname):
    def aiter():
        mro = cls.mro()
        yield getattr(cls, localname)
        for c in mro:
            for k in (localname, name):
                sc = super(c, cls)
                v = getattr(sc, k, None)
                if v is not None:
                    yield v
                    break
    return combine_args(aiter())

def compute_table_args(cls):
    return combine_args_helper(cls, '__table_args__' , '__partial_table_args__')

def compute_mapper_args(cls):
    return combine_args_helper(cls, '__table_mapper__' , '__partial_mapper_args__')

def make_combine_args_class(base):

    class CombineArgs(base):
        __abstract__ = True
        __partial_table_args__  = ()
        __partial_mapper_args__ = ()

        @declared_attr
        def __table_args__(cls):
            return compute_table_args(cls)

        @declared_attr
        def __mapper_args__(cls):
            return compute_mapper_args(cls)

    return CombineArgs

