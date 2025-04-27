import json
import os

class Loader:
    _data = None  # クラス変数としてデータを保持

    @classmethod
    def load_data(self):
        """JSON データをロードしてクラス変数に保存"""
        if self._data == None:  # データが未ロードの場合のみロード
            json_path = os.path.join(os.path.dirname(__file__), "../json/joke_list.json")
            try:
                with open(json_path, mode='r', encoding='UTF-8') as jsonfile:
                    self._data = json.load(jsonfile)
                    print("CONSOLE: database load successful")
            except FileNotFoundError:
                print(f"CONSOLE: [ERROR] {json_path} not found.")
                self._data = {}
        return self._data

    @classmethod
    def get_data(self):
        """ロード済みのデータを取得"""
        if self._data == None:
            self.load_data()
        return self._data