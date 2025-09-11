from logging import root
from  pathlib import Path
import requests

''' io 密集型 '''
root_path = Path(__file__).cwd()

#parent_path= Path(__file__).resolve().parent
url = 'http://localhost:19990/region/region/gihub/repos'

# I/O 密集型 Web 请求
response = requests.get(url)


items = response.headers.items()
#print(f'类型：{type(items)}')
#print(items)

headers = [f'{key}:{header}' for key, header in items]

formatter_headers = '\n'.join(headers)

file_path = root_path / 'common/files/'
with open(file_path / 'headers.txt', 'w', encoding='utf-8') as f:
    f.write(formatter_headers)

