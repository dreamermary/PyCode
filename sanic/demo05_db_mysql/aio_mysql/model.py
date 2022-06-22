# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   model.py
# @Time    :   2022/6/18 9:42

# 表对象
import sqlalchemy as sa

metadata = sa.MetaData()
user = sa.Table(
    'user', # 表名
    metadata,
    sa.Column('id',sa.Integer,autoincrement=True,primary_key=True),
    sa.Column('user_name',sa.String(16),nullable=False),
    sa.Column('pwd',sa.String(32),nullable=False),
    sa.Column('real_name',sa.String(6),nullable=True),
)

