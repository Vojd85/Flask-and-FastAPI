# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. 
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.

import argparse
import asyncio
import time
from thread import download_by_threads
from multiproc import download_by_multiproc
from asyn import download_by_async


async def main():
    parser = argparse.ArgumentParser(description='Скачивание изображений с url адресов')
    parser.add_argument('-m', '--mode', choices=['a', 't', 'm'], help='Режимы работы (asyncio, treading, multiprocessing)')
    parser.add_argument('-u', '--urls', help='Список адресов через запятую')

    args = parser.parse_args()
    url_list = args.urls.split(',')

    if args.mode == 'a':
        await download_by_async(url_list)
    elif args.mode == 't':
        download_by_threads(url_list)
    elif args.mode == 'm':
        download_by_multiproc(url_list)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Время загрузки изображений {end - start:.2f} сек')