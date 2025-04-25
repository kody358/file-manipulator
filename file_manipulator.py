import sys

# ファイルを逆順にする関数
def handle_reverse(input_file, output_file):
    # 引数語りているか確認
    if len(sys.argv) != 4:
        print("使用方法： python3 file_manipulator.py reverse [ファイル名] [出力ファイル名]")
        sys.exit(1)
    
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        
        #内容を反転
        reversed_content = content[::-1]

        # 出力ファイルに反転内容を書き出す
        with open(output_file, 'w') as file:
            file.write(reversed_content)
        
        print(f"ファイル内容を反転し、{output_file}に保存しました。")
    
    except FileNotFoundError:
        print(f"エラー： ファイル{input_file}が見つかりません。")
        sys.exit(1)
    except PermissionError:
        print(f"エラー： ファイル{input_file}に書き込み権限がありません。")
        sys.exit(1)
    except Exception as e:
        print(f"エラー： 予期せぬエラーが発生しました。{e}")
        sys.exit(1)

# ファイルのコピーを作成する関数
def handle_copy(input_file, output_file):
    # 引数語りているか確認
    if len(sys.argv) != 4:
        print("使用方法： python3 file_manipulator.py copy [ファイル名] [出力ファイル名]")
        sys.exit(1)
    
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        # 読み込んだ内容を書き出す
        with open(output_file, 'w') as file:
            file.write(content)
        
        print(f"ファイル内容を{output_file}にコピーしました。")
    
    except FileNotFoundError:
        print(f"エラー： ファイル{input_file}が見つかりません。")
        sys.exit(1)
    except PermissionError:
        print(f"エラー： ファイル{input_file}に書き込み権限がありません。")
        sys.exit(1)
    except Exception as e:
        print(f"エラー： 予期せぬエラーが発生しました。{e}")
        sys.exit(1)

# ファイルの内容をn回同ファイルに書き出す
def handle_duplicate(input_file, n):
    # 引数語りているか確認
    if len(sys.argv) != 4:
        print("使用方法： python3 file_manipulator.py duplicate [ファイル名] [回数]")
        sys.exit(1)
    
    try:
        n = int(n)
        with open(input_file, 'r') as file:
            content = file.read()
        
        for i in range(n):
            with open(input_file, 'a') as file:
                file.write(content)
        
        print(f"ファイル内容を{n}回繰り返し、{input_file}に保存しました。")
    
    except FileNotFoundError:
        print(f"エラー： ファイル{input_file}が見つかりません。")
        
# ファイルから第2引数の文字列を検索し、全て第3引数に置き換える
def handle_replace_string(input_file, search_string, replace_string):
    # 引数語りているか確認
    if len(sys.argv) != 5:
        print("使用方法： python3 file_manipulator.py replace-string [検索文字列] [置換文字列]")
        sys.exit(1)
    
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        
        # 検索文字列を置換文字列に置き換える
        replaced_content = content.replace(search_string, replace_string)

        # 置換後の内容をファイルに書き出す
        with open(input_file, 'w') as file:
            file.write(replaced_content)
        
        print(f"ファイル内容を{search_string}を{replace_string}に置換しました。")
    
    except FileNotFoundError:
        print(f"エラー： ファイル{input_file}が見つかりません。")
        sys.exit(1)
    except PermissionError:
        print(f"エラー： ファイル{input_file}に書き込み権限がありません。")
        sys.exit(1)
    
def main():
    # 対応しているコマンドのリスト
    COMMANDS = {
        "reverse": handle_reverse,
        "copy": handle_copy,
        "duplicate-contents": handle_duplicate,
        "replace-string": handle_replace_string,
    }

    #コマンドライン引数の確認
    # sys.argv[0]はプログラム名
    # sys.argv[1]はファイル名
    # sys.argv[2]はオプション
    # sys.argv[3]~はオプションの値
    if len(sys.argv) < 2:
        print("使用方法： python filemanipulator.py [コマンド名] [引数...]")
        sys.exit(1)
    
    # 最初の引数からコマンドを取得
    command = sys.argv[1]

    # 対応するコマンドかを確認
    if command not in COMMANDS:
        print(f"エラー： コマンド{command}は対応していません。")
        sys.exit(1)

    #コマンドに応じた関数を呼び出す
    COMMANDS[command](*sys.argv[2:])

# このファイルが直接実行された場合のみmain関数を実行
if __name__ == "__main__":
    main()
