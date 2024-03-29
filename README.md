# ミニマリストを丸裸にする 100 の質問

## 質問集を入手する
直接ファイルをダウンロードしてご利用ください。

- ■区切り形式
  - [ダウンロード](https://raw.githubusercontent.com/stakiran/100q-minimalist/master/plain_square_output.md)
- Markdown形式(リスト)
  - 質問文が `- 1. ……` の形式です
  - [ダウンロード](https://raw.githubusercontent.com/stakiran/100q-minimalist/master/markdown_output.md)
- Markdown形式(太字)
  - 質問文が `- **Q1.** ……` の形式です
  - [ダウンロード](https://raw.githubusercontent.com/stakiran/100q-minimalist/master/markdown_boldnumber_output.md)

## 質問集を使う
以下の条件をすべて守れる場合のみ、営利/非営利、改変の有無、再配布の有無を問わず、無料で利用できます。

- 出典としてウェブサイト [https://stakiran.github.io/100q-minimalist/](https://stakiran.github.io/100q-minimalist/) へのリンクと作者名「吉良野すた」を記していただけると嬉しいです（強制ではない）
- この質問集には何の保証もありません。この質問集を利用したことで生じた、いかなる問題についても作者は一切の責任を負いません

## (開発者向け) 質問集を作成する
番号の採番や質問集フォーマットの変更を簡単にするため、スクリプトを使用しています。

- (0) [リポジトリ](https://github.com/stakiran/100q-minimalist) からファイル一式を入手する
- (1) [ソースファイル](100q_source.md) を編集する
- (2) builder.py を実行するためのコマンドラインを組み立てる
  - サンプル: [Markdown形式生成時のコマンドライン](build_markdown.bat)
- (3) コマンドラインを実行する

builder.py の実行には Python が必要です。

builder.py の詳しい使い方は `python builder.py -h` で Usage を見るか(あまり充実していません)、ソースを直接読んでください。

## ライセンス
- py ファイルと bat ファイルは [MIT License](LICENSE)
- md ファイルは上記「質問集を使う」に従ってください
