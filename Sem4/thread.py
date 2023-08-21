import requests
import threading
import os
import time

def download(url):
    start = time.time()
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        file_name = url.rsplit('/', 1)[-1]
        file_name = os.path.join('images', file_name)
        print(file_name)
        with open(file_name, 'wb') as file:
            file.write(content)
        end = time.time()
        print(f'Загружен файл {file_name} за {end - start:.2f} сек')
    else:
        print(f'Не удалось загрузить контент с сайта {url}')

def download_by_threads(url_list):
    threads = []
    for url in url_list:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()