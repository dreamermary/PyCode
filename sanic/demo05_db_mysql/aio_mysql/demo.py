# -*- coding: utf-8 -*-
# @Author  :   clumba
# @File    :   demo.py
# @Time    :   2022/6/18 9:59

import asyncio

from aiomysql.sa import create_engine

from model import user

async def go(loop):

    # 1.创建数据库引擎
    engine = await create_engine(
        user='root',password='root',
        host='127.0.0.1',db='test_mysql',
        loop=loop,
    )

    # 2.获取连接
    async with engine.acquire() as conn:
        # 执行sql+执行提交,执行写时需要commit
        for i in range(5):
            await conn.execute(
                user.insert().values(user_name=f'n-{i}',pwd='a1',real_name='rn1')
            )
        await conn.execute('commit')

        # 查询 & 输出
        # ls = await conn.execute(user.select())
        # for i,li in enumerate(ls):
        #     print(f"ROW {i}:{li.user_name},{li.id},{li.pwd},{li.real_name}")
        async for row in conn.execute(user.select()):
            print(row.user_name, row.pwd)

    # 3.关闭引擎
    engine.close()
    await engine.wait_closed()

loop = asyncio.get_event_loop()
loop.run_until_complete(go(loop))
