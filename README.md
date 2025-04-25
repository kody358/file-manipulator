# file-manipulator

## 概要
file-manipulatorは、コマンドラインからファイルの内容を操作するシンプルなPythonプログラムです。

## 機能
現在サポートされているコマンド：

### reverseコマンド
指定したファイルの内容を反転（逆順）にして、新しいファイルに保存します。

## 使い方

### 基本的な使い方
```
python file_manipulator.py [コマンド] [引数...]
```

### reverseコマンドの使い方
```
python file_manipulator.py reverse [入力ファイル] [出力ファイル]
```

#### 例
```
python file_manipulator.py reverse input.txt output.txt
```
この例では、`input.txt`の内容を反転させて`output.txt`に保存します。

## エラー処理
以下のような場合、エラーメッセージが表示されます：
- 入力ファイルが存在しない
- 出力ファイルに書き込めない（権限がない）
- その他の予期せぬエラー

## 実行例
入力ファイル（input.txt）の内容が「こんにちは、世界！」の場合、
出力ファイル（output.txt）の内容は「！界世、はちにんこ」になります。
