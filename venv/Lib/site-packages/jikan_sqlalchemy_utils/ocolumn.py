from sqlalchemy import Column

def OColumn(*args, _order, **kwargs):
    '''manually-ordered column'''
    col = Column(*args, **kwargs)
    col._creation_order = _order
    return col

