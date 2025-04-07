import csv
import io, sys
import pandas as pd
import os
import pathlib

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 引数の数が合っていなければエラーを出力
if len(sys.argv) != 3:
    sys.stderr.write("引数の数が違います。下記の引数を入れてください\n[第１引数：csvdata_extraction_tool_allfiles.py] [第２引数：検索対象CSVファイルの親ディレクトリ] [第３引数：検索値]\n")
    sys.exit()

# 検索対象CSVファイルの親ディレクトリ
search_target_csvfile_directry = sys.argv[1]
# 検索値
search_value                   = sys.argv[2]
# CSV格納用の配列
csv_list = []

# 数値かどうかをチェックして適切な型を設定
try:
    search_value = int(search_value)
except ValueError:  
    pass  

# 親ディレクトリからcsvファイルを抽出
for file in sorted(pathlib.Path(search_target_csvfile_directry).glob("*.csv")):  
    csvpath  = file.parent
    csvname  = file.name
    try:
        csv_data = pd.read_csv(file, encoding='shift_jis')

    # パスが長すぎる場合はエラーを出力
    except FileNotFoundError:
        sys.stderr.write("検索対象のファイルが見つかりません。ディレクトリ、ファイル名が正しいか確認してください")
        sys.exit()
    
    csv_file_data = [csvpath, csvname, csv_data]
    csv_list.append(csv_file_data)

# 列インデックスをアルファベットに変換する
def index_to_column(index):
    letters = ''
    while index >= 0:
        letters = chr(ord('A') + index % 26) + letters
        index = index // 26 - 1
    return letters

# 生成したCSVのリストからすべての列をチェックして検索値に合致する行を取得
for csv_file in csv_list:
    path       = csv_file[0]
    name       = csv_file[1]
    file_data  = csv_file[2]

    # 検索条件に一致する行の値をフィルタリング
    for idx, row in file_data.iterrows():
        if search_value in row.values:
            match_cells = [f"{index_to_column(i)}{idx + 2}" for i, val in enumerate(row) if val == search_value]
            print(f"ファイルパス: {path}\nファイル名: {name}\n一致したセル: {match_cells}\n一致した値: {search_value}\n")