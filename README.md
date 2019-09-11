# ミニマリストを丸裸にする 100 の質問

## 質問集を入手する
view リンクで中身を覗いてみたり、raw リンクで直接ファイルをダウンロードしたりできます。

- Markdown形式
  - [view](markdown_output.md) [raw](https://raw.githubusercontent.com/stakiran/100q-minimalist/master/markdown_output.md)
- ■区切り形式
  - [view](plain_square_output.md) [raw](https://raw.githubusercontent.com/stakiran/100q-minimalist/master/plain_square_output.md)

## 質問集を使う
以下の条件をすべて守れる場合のみ営利/非営利を問わず、改変の有無も問わず、また再配布の有無も問わず無料で利用できます。

- 出典として ★このサイトへのリンク と ★作者名 を記してください
- この質問集には何の保証もありません。この質問集を利用したことで生じた、いかなる問題についても作者は一切の責任を負いません

## (開発者向け) 質問集を作成する
番号の採番や質問集フォーマットの変更を簡単にするため、スクリプトを使用しています。

- (1) [ソースファイル](100q_source.md) を編集する
- (2) builder.py を実行するためのコマンドラインを組み立てる
  - サンプル: [Markdown形式生成時のコマンドライン](build_markdown.bat)
- (3) コマンドラインを実行する

builder.py の実行には Python が必要です。

builder.py の詳しい使い方は `python builder.py -h` で Usage を見るか(あまり充実していません)、ソースを直接読んでください。

## LICENSE
- py ファイルと bat ファイルは [MIT License](LICENSE)
- md ファイルは上記「質問集を使う」に従ってください
