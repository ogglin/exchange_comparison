import asyncio
import datetime
import concurrent.futures

from asgiref.sync import sync_to_async

urls = ['www.google.com', 'www.youtube.com', 'www.aol.com']


# @sync_to_async
async def fetch(url):
    await asyncio.sleep(1)
    return '1' + url


async def init(urls):
    tasks = []
    for url in urls:
        tasks.append(fetch(url))
    # results = await asyncio.gather(map(fetch, urls))
    results = await asyncio.gather(*tasks)
    # results = await asyncio.gather(*async_tasks)
    return results


def start():
    print('start: ' + str(datetime.datetime.now()))
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.set_default_executor(concurrent.futures.ThreadPoolExecutor(max_workers=20))
    init_result = loop.run_until_complete(init(urls))
    print(init_result)
    loop.close()
    print('end: ' + str(datetime.datetime.now()))


# start()
