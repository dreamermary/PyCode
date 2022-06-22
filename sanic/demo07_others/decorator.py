# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   decorator.py
# @Time    :   2022/6/22 14:48

from functools import wraps

'''
装饰器/注解
    1.定义装饰器
    2.使用装饰器
'''

def decorator2(*param):
    print(param)
    def wrapper2(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f'before:{func.__name__}:decorator')
            func(*args, **kwargs)
            print(f'after:{func.__name__}:decorator')
        return wrapper
    return wrapper2

def decorator1(func,):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'before:{func.__name__}:decorator')
        func(*args, **kwargs)
        print(f'after:{func.__name__}:decorator')
    return wrapper

# @decorator(params),参数为param
# @decorator,默认参数为func
@decorator1
def hello1(name='hello word'):
    print(name)

@decorator2("param")
def hello2(name='hello word'):
    print(name)

hello2()
