＜ツール概要＞
run.batで検索値を指定。検索値が含まれるcsvファイルを特定し、result.txtに出力する。

＜インストール編＞
　■Python インストール
　　https://www.python.org/downloads/

＜事前準備編＞
　①仮想環境作成
　　参考URL：https://qiita.com/nosniklim/items/1d4c480e3accd3eb8c0f
　　
　　・仮想環境作成
　　　py -m venv csvdata_extraction_tool_allfiles
　
　　・仮想環境を有効にする
　　　cd csvdata_extraction_tool_allfiles
　　　Scripts\activate

　②ライブラリのインストール
　　・pipの最新化（ライブラリインストール用コマンドを最新にする）
　　　python -m pip install

　　・pandasのインストール（エクセル操作のライブラリ）
　　　pip install pandas

　③csvdata_extraction_tool_allfiles.pyを①で作成した仮想環境配下に持っていく

　④run.batファイルの中身を編集。下記の引数で実行されるため抽出したいデータに応じて変更する
　　py csvdata_extraction_tool_allfiles.py 検索対象CSVファイルの親ディレクトリ　 検索値　>> result.txt

　　(例.)137、459、Brandon、Jackの単語を含むファイルを抽出したい場合
　　　　set file_path="C:\Users\~\csvdata_extraction_tool_allfiles\testfolder"

　　　　py csvdata_extraction_tool_allfiles.py %file_path% 137 >> result.txt
　　　　py csvdata_extraction_tool_allfiles.py %file_path% 459 >> result.txt
　　　　py csvdata_extraction_tool_allfiles.py %file_path% Brandon >> result.txt
　　　　py csvdata_extraction_tool_allfiles.py %file_path% Jack >> result.txt

　⑤コマンドプロンプトにてrun.batファイルを実行。結果がresult.txtに出力される。
　　run.bat

＜毎回：コマンドライン落としたら＞
　・仮想環境を有効にする
　　cd csvdata_extraction_tool_allfiles
　　Scripts\activate

＜run.batファイル実行時に文字化けしているとき、ディレクトリ指定でエラーが出る場合＞
　chcp 65001
　を入力して再度実行
