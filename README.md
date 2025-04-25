# file-manipulator

## 概要
file-manipulatorは、コマンドラインからファイルの内容を操作するシンプルなPythonプログラムです。

## 機能
現在サポートされているコマンド：

### reverseコマンド
指定したファイルの内容を反転（逆順）にして、新しいファイルに保存します。
使用方法： python3 file_manipulator.py reverse [ファイル名] [出力ファイル名]

### copyコマンド
指定したファイルの内容をそのまま別のファイルにコピーします。
使用方法： python3 file_manipulator.py copy [ファイル名] [出力ファイル名]

### duplicate-contentsコマンド
指定したファイルの内容を、指定した回数だけ同じファイルに追加します。
使用方法： python3 file_manipulator.py duplicate [ファイル名] [回数]

### replace-stringコマンド
指定したファイル内の特定の文字列を検索し、別の文字列に置き換えます。
使用方法： python3 file_manipulator.py replace-string [検索文字列] [置換文字列]
