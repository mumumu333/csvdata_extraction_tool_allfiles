import csv
import io, sys
import pandas as pd
import os
import pathlib

# 出力時の文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 引数の数が合っていなければエラーを出力
if len(sys.argv) != 4:
    sys.stderr.write("引数の数が違います。下記の引数を入れてください\n[第１引数：csvdata_extraction_tool_allfiles.py] [第２引数：検索対象CSVファイルの親ディレクトリ] [第３引数：検索対象列のアルファベット] [第４引数：検索値]\n")
    sys.exit()

# 検索対象CSVファイルの親ディレクトリ
search_target_csvfile_directry = sys.argv[1]
# 抽出対象列のアルファベット
search_result_column_alp       = sys.argv[2]
# 検索値
search_value                   = int(sys.argv[3])
# CSV格納用の配列
csv_list = []

# 親ディレクトリからcsvファイルを抽出
for file in sorted(pathlib.Path(search_target_csvfile_directry).glob("*.csv")):
    csvpath  = file.parent
    csvname  = file.name
    try:
        csv_data = pd.read_csv(file)

    # パスが長すぎる場合はエラーを出力
    except FileNotFoundError:
        sys.stderr.write("検索対象のファイルが見つかりません。ディレクトリ、ファイル名が正しいか確認してください")
        sys.exit()
    
    csv_file_data = [csvpath, csvname, csv_data]
    csv_list.append(csv_file_data)

# 抽出対象列のアルファベットの値を取得する
search_result_column_alp = search_result_column_alp.upper()
col_num = 0
for char in search_result_column_alp:
    col_num = col_num * 26 + (ord(char) - 64)
col_num = col_num - 1

# 生成したCSVのリストから指定された列番号の値を取得
for csv_file in csv_list:
    path       = csv_file[0]
    name       = csv_file[1]
    file_data  = csv_file[2]

    if col_num < len(file_data.columns):
        # フレームと検索対象列のデータを取得
        selected_data = file_data.iloc[:, [0, col_num]]

        # 検索条件に一致する列の値をフィルタリング
        filtered_data = selected_data[selected_data.apply(lambda row: row.iloc[1] == search_value, axis=1)]

        if not filtered_data.empty:
            filtered_data.apply(lambda row: print(f"ファイルパス: {path}\nファイル名: {name}\nフレーム: {row.iloc[0]}\n{search_result_column_alp}列の値: {row.iloc[1]}\n\n"), axis=1)