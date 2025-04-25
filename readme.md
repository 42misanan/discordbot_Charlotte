# !!!WORK IN PROGRESS!!!
このbotは， discord 上でなんかよくわからんダジャレを連発するために構築されている最中のものです．

## やりたいこと
- スラッシュコマンドの実装
- json で db の追加／削除／参照
- class を使用した保守性の高いコード
- 複数サーバー間でダジャレファイトを誘発

## 実装する必要があるもの
- vote システムの実装
    - 評価スパムできるとダメなので、各ダジャレに対して各ユーザにつき1日に1票しか入れれないようにする？
    - アトランダムな出力の確保
- json での db 構築＋操作
    - 各ダジャレごとに，「内容」「作成日」「作者」「評価」を格納
    - ダジャレ総覧のページ化
- スラッシュコマンドの実装による簡単追加

## 納期
特に決めない（気持ちがある時に作る） 


### ファイル構造
- projectCharlotte
1. .gitignore: 何も言わなくても良いでしょう
2. bot.py: botの起動処理を行う．Charlotte クラス．
3. config.py: .envからTOKENとPREFIXを拾う．
4. main.py: bot インスタンスを作成し，スラッシュコマンドを読み込み，botを立ち上げる．
    - slash:
        1. NO_DATA!/ joke.py: このbotの中核となるコマンド．jsonファイルからアトランダムに吐き出す．
        2. NO_DATA!/ add.py: ダジャレを追加する．「作成日」「作者」を取得し，「内容」を入力させる．
        3. NO_DATA!/ help.py: 各コマンドから取得したdescriptionを出力させる．引数なしならコマンド一覧を表示．
        4. NO_DATA!/ reload.py: 【管理者用】json/joke_list.jsonをリロードする．
        5. NO_DATA!/ remove.py: 【管理者用】json/joke_list.jsonの中から何かしらのデータを削除する．
    - json:
        1. NO_DATA!/ joke_list.json: データを格納する．各データは「内容」「作成日」「作者」「評価」を持つ．
    - sys:
        1. NO_DATA!/ vote.py: vote システムをここに格納する． joke.pyで表示する出力結果に対して添える感じで使うことになりそう．