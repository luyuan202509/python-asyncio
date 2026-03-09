from pathlib import Path
import json 

#path = Path(__file__).parent
# 读取json文件
def read_json_file(file_path):
    try:
        with open(file_path,'r') as f:
             json_content= json.load(f)
             return json_content
    except FileNotFoundError:
         print("File not found")


# 读取普通文件
def read_file(file_path):
    try:
        with open(file_path,'r') as f:
             contents = f.read()
             return contents
    except FileNotFoundError:
         print("File not found")

def rwite_file(file_path,contents):
    message = ""
    try:
        with open(file_path,'w') as f:
             f.write(contents)
             message = "write success"
    except FileNotFoundError:
         print("File not found")
         message = "write fail"
    
    return message