from pathlib import Path
import json 
from utils import read_file,read_json_file,rwite_file   


root_path = Path(__file__).parent

raw_datafile =  root_path / 'json_row.txt'
new_file = root_path / 'json_new.json'
def test():

    text =  read_file(raw_datafile)
    text = json.dumps(text)
    message = rwite_file(new_file,text)
    print(message)

def main():
   json_content =  read_json_file(new_file)
   for item in json_content:
       print(item)


if __name__ == '__main__':
    main()

