from pathlib import Path
import json

path = Path(__file__).parent 
jsonfile = path / 'map_data.json'

# 读取文件
try:
    with open(jsonfile,'r') as f:
         json_content= json.load(f)
         for layer in json_content['layers']:
             for key,item in layer.items():
                 print(key,item)
except FileNotFoundError:
     print("File not found")


raw_datafile =  path / 'json_row.txt'
new_contents = ""
def raw_method():
    try:    
        with open(raw_datafile,'r') as f:
            for line in f:
                new_contents += line
    except FileNotFoundError:
        print("文件未找到！")


try:
    with open(jsonfile,'w') as f:
        json.dump(new_contents,f,indent=4)
        print("写入成功")
except FileNotFoundError:
    print("File not found")