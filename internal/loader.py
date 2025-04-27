import json
import os
import time

class Loader:
    _data = None  # クラス変数としてデータを保持
    _last_modified = None  # ファイルの最終更新時刻を記録

    @classmethod
    def load_data(cls):
        """JSON データをロードしてクラス変数に保存"""
        json_path = os.path.join(os.path.dirname(__file__), "../json/joke_list.json")
        try:
            # ファイルの最終更新時刻を取得
            last_modified = os.path.getmtime(json_path)
            # ファイルが変更されている場合、またはデータが未ロードの場合に再読み込み
            if cls._data == None or cls._last_modified != last_modified:
                with open(json_path, mode='r', encoding='UTF-8') as jsonfile:
                    cls._data = json.load(jsonfile)
                    cls._last_modified = last_modified  # 更新時刻を記録
                    print("CONSOLE: database load successful")
        except FileNotFoundError:
            print(f"CONSOLE: [ERROR] {json_path} not found.")
            cls._data = {}
            cls._last_modified = None
        return cls._data

    @classmethod
    def get_data(cls):
        """ロード済みのデータを取得"""
        return cls.load_data()