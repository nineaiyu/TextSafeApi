#!/usr/bin/env python
# -*- coding:utf-8 -*-
# project : TextSafeApi
# filename : test
# author : ly_13
# date : 8/9/2023
import asyncio

import aiohttp


class Response(object):
    status = 403
    data = {}

    def __init__(self, response, data):
        self.status = response.status
        self.data = data


class Request(object):

    async def post(self, url, data=None, json_data=None):
        async with aiohttp.ClientSession() as session:
            session.headers.add('xy-version', '999.999.999')
            count = 3
            while count > 0:
                try:
                    async with session.post(url, data=data, json=json_data) as response:
                        try:
                            json_result = await response.json(content_type=response.headers['content-type'])
                        except:
                            json_result = await response.text()
                        return Response(response, json_result)
                except Exception as e:
                    count -= 1
                    print(f"aiohttp error {url} {count} {e} try gagin")
            return Response(response, json_result)

    async def get(self, url, params):
        async with aiohttp.ClientSession() as session:
            count = 3
            while count > 0:
                try:
                    session.headers.add('xy-version', '999.999.999')

                    async with session.get(url, params=params) as response:
                        try:
                            json_data = await response.json(content_type=response.headers['content-type'])
                        except:
                            json_data = await response.text()
                        return Response(response, json_data)
                except Exception as e:
                    count -= 1
                    await asyncio.sleep(1)
                    print(f"aiohttp error {url} {count} {e} try gagin")
            return Response(response, json_data)


async def async_gather(gather_tasks, pool_num):
    r = []
    for i in range(0, len(gather_tasks), pool_num):
        r.extend(await asyncio.gather(*gather_tasks[i:i + pool_num]))
    return r


async def check():
    req = await Request().post('http://127.0.0.1:8000/check/message',
                               json_data={'text': '你是个大傻子谢谢谢谢', 'uid': '11111'})
    print(req.data)


async def run():
    task_list = []
    for i in range(300):
        task_list.append(check())
    await async_gather(task_list, 300)


if __name__ == '__main__':
    asyncio.run(run())
