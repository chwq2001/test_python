#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import time


async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print('Read {} from {}'.format(resp.content_length, url))


async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites] # from Python 3.7, support  create_task， 代替asyncio.ensure_future
    await asyncio.gather(*tasks)


def main():
    sites = [
        'http://c.biancheng.net',
        'http://c.biancheng.net/c',
        'http://c.biancheng.net/python'
    ]
    start_time = time.perf_counter()

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(download_all(sites))
    finally:
        loop.close()
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()
