import sys

def reverse_file(input_file, output_file):
    # 入力ファイルを読み込んで内容を反転させて出力ファイルに書き出す
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

def main():
    #コマンドライン引数の確認
    # sys.argv[0]はプログラム名
    # sys.argv[1]はファイル名
    # sys.argv[2]はオプション
    # sys.argv[3]はオプションの値
    # sys.argv[4]はオプションの値
    # sys.argv[5]はオプションの値
    # sys.argv[6]はオプションの値
    if len(sys.argv) < 2:
        print("使用方法： python filemanipulator.py [コマンド名] [引数...]")
        sys.exit(1)
    
    # 最初の引数からコマンドを取得
    command = sys.argv[1]

    #コマンドに応じた処理を実行
    if command == "reverse":
        # reverseコマンドに必要な引数があるか検証
        if len(sys.argv) != 4:
            print("使用方法： python file_manipulator.py reverse [ファイル名] [出力ファイル名]")
            sys.exit(1)
        
        # ファイルを逆順にする
        reverse_file(sys.argv[2], sys.argv[3])

# このファイルが直接実行された場合のみmain関数を実行
if __name__ == "__main__":
    main()
