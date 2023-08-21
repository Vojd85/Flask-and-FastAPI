import asyncio
import aiohttp
import time
import os

async def download(url):
    start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                file_name = url.rsplit('/', 1)[-1]
                file_name = os.path.join('images', file_name)
                print(file_name)
                with open(file_name, 'wb') as file:
                    file.write(content)
                end = time.time()
                print(f'Загружен файл {file_name} за {end - start:.2f} сек')
            else:
                print(f'Не удалось загрузить контент с сайта {url}')

async def download_by_async(url_list):
    tasks = []
    for url in url_list:
        task = asyncio.create_task(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)