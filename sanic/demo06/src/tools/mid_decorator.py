# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   mid_decorator.py
# @Time    :   2022/6/20 9:56

#
from functools import wraps

from sanic.request import Request
from sanic import response

from ujson import loads as json_loads
from ujson import dumps as json_dumps

from src.config import CONFIG

def response_handle(request, dict_value,status=200):
    if isinstance(request,Request):
        return response.json(dict_value,status=status)
    else:
        return json_dumps(dict_value,ensure_ascii=False) # dict
    pass

# 有无request,有无func
def authenticator(key):
    """

    :param key:验证方式：Api-key:Magic Key
    :return:
    """
    def wrapper(func):
        @wraps(func)
        async def authenticate(request,*args,**kwargs):
            value = request.headers.get(key,None)
            if value and CONFIG.AUTH[key] == value:
                response = await func(request,*args,**kwargs)
                return response
            else:
                return response_handle(request,{'info':'failed:6'},status=401)

        return authenticator
    return wrapper


'''1.参数验证--------------------------------------'''
def auth_params(*keys): # type=tuple,长度可变
    """
    api请求参数验证
    :param keys: params
    :return:
    """

    def wrapper(func): # func是个啥玩意
        @wraps(func)
        async def auth_param(request=None,rpc_data=None,*args,**kwargs):
            request_params, params = {}, [] # 参数k-v，参数k
            if isinstance(request,Request):
                if request.method == 'POST':
                    try:
                        body_params = request.body.decode('UTF-8')
                        post_data = json_loads(body_params)
                    except Exception as e:
                        return response_handle(request,{'info':'error:2'})
                    else:
                        request_params.update(post_data)
                        # value非空则添加key
                        params = [key for key, value in post_data.items() if value]
                elif request.method == 'GET':
                    request_params.update(dict(request.args))
                    params = [key for key, value in request.args.items() if value]
                else:
                    return response_handle(request,{'info':'error:3'})
            else:
                pass

            if set(keys).issubset(set(params)): # a.issubset(b),判断a是否为b的子集
                kwargs['request_params'] = request_params
                return await dec_func(func,request,*args,**kwargs)
            else:
                return response_handle(request,{'info':'error:4'})

        return auth_param

    return wrapper

async def dec_func(func,request,*args,**kwargs):
    try:
        response = await func(request,*args,**kwargs)
        return response
    except Exception as e:
        return response_handle(request,{"info":"error:5"})
'''
auth_params():
    wrapper():
        auth_param():
            def_func()
        
dec_fun():
'''
'''--------------------------------------'''

