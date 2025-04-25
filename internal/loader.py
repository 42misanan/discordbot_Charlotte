import json

class dbInitialize():
    def __init__(self):
        with open("json/joke_list.json", mode='r', encoding='UTF-8') as jsonfile:
            self._data = json.load(jsonfile)
            print("CONSOLE: database load successful")
            jsonfile.close