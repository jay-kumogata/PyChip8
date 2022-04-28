## PyChip8開発記

### 2006-09-23

Perlも時代遅れなので，新しいスクリプト言語でも勉強しようかなと思いました．
Pythonか，Rubyかと思ったのですが，PythonがLispに似ているという話を聞いて，断然Pythonをおぼえる気になりました．
Lispは，ずっと昔，言語処理系を作るのに使っていたので，結構愛着ありなのです．

ということで，Pythonのチュートリアル（日本語）を読みました．
暇なときにぱらぱら見るだけで，すぐに理解できました．やっぱり，こういうの得意かもしれません．

それから，言語仕様も大体理解できたので，何か作ってみようと思いました．

- UPnPスタック
- JavaVM

などの候補も出たのですが，Chip-8エミュレータ（InfoChip8）を移植してみることにしました．
言語的に，変数に型がなかったり，いろいろと心配なことがありましたが，だめでも，課題抽出ってことで，やってみましょう．

このシリーズでは，その模様を随時報告します．
Pythonでエミュレータを作るのは，世界初かもしれません．

### 2006-09-24

準備

プログラミングには，Meadow（emacsのこと）を利用しています．
python-modeが使えないので，この[サイト](http://sourceforge.net/project/showfiles.php?group_id=86916&package_id=90384&release_id=375396)から，ダウンロード，インストール（c:\Meadow\site-lisp等）します．

そして，.emacsに以下を追加します．

	(autoload 'python-mode "python-mode" nil t)
	(add-to-list 'auto-mode-alist '("\\.py\\'" . python-mode))
	(add-hook 'python-mode-hook
	          '(lambda()
	             (require 'pycomplete)
	             (setq indent-tabs-mode nil)))


進捗

CPU部から移植を開始しました．以下をコーディングしました．

- CPU.py
  - CPU_Init()：初期化
  - CPU_Fin()：終了化
  - CPU_Step()：N命令を実行するメソッド
    - 1NNN命令
    - 2NNN命令

参考

以下は，「[P/ECE研究室](http://www.piece-me.org/chip8-20040328.txt)」より引用しました．

	1NNN	アドレスNNNへ分岐します．
	2NNN	アドレスNNNに配置されたCHIP-8サブルーチンを呼び出します．
		サブルーチン呼び出しは，16階層まで入れ子にできます．

### 2006-09-29

進捗

平日の暇なときに，作業を実施しました．CPU部から移植を再開しました．以下をコーディングしました．

- CPU.py
  - CPU_Step()：N命令を実行するメソッド
    - 3XKK命令
    - 4XKK命令
    - 5XY0命令
    - 6XKK命令
    - 7XKK命令

参考

以下は，「[P/ECE研究室](http://www.piece-me.org/chip8-20040328.txt)」より引用しました．

	3XKK	VXレジスタの値が即値KKに等しければ，直後の命令の実行をスキップします．
	4XKK	VXレジスタの値が即値KKに等しくなければ，直後の命令の実行をスキップします．
	5XY0	VXレジスタとVYレジスタの値が等しければ，直後の命令の実行をスキップします．
	6XKK	VXレジスタに即値KKを代入します．
	7XKK	VXレジスタに即値KKを加算します．
		(訳注:キャリー検出なしです．VFレジスタは変化しません．)

### 2006-10-02

進捗

CPU部から移植を再開しました．以下をコーディングしました．

- CPU.py
  - CPU_Step()：N命令を実行するメソッド
    - 8XY0命令
    - 8XY1命令
    - 8XY2命令
    - 8XY3命令
    - 8XY4命令
    - 8XY5命令
    - 8XY6命令
    - 8XY7命令
    - 8XYE命令

参考

以下は，「[P/ECE研究室](http://www.piece-me.org/chip8-20040328.txt)」より引用しました．

	8XY0	VXレジスタにVYレジスタの値を代入します．
	8XY1	VXレジスタとVYレジスタの論理和を求め，VXレジスタに格納します．
	8XY2	VXレジスタとVYレジスタの論理積を求め，VXレジスタに格納します．
	8XY3	VXレジスタとVYレジスタの排他論理和を求め，VXレジスタに格納します．(*)

### 2006-10-07

進捗

CPU部から移植を再開しました．以下をコーディングしました．

- CPU.py
  - CPU_Step()：N命令を実行するメソッド
    - 9XY0命令
    - ANNN命令
    - BNNN命令
    - CXKK命令
    - FX1E命令
    - FX33命令
    - FX55命令
    - FX65命令
  - CPU_Read()，CPU_ReadW()：メモリへの読込み
  - CPU_Write()：メモリへの書込み
- System.py : ファイルI/O，グラフィック，サウンド
  - LoadRom()：ROMイメージをRAMへ格納 

### 2006-10-14

進捗

それぞれのクラス（CPU，PPU，等）を統合するクラスSystemを修正しました．
PPUクラスを新規にコーディング開始しました．
CPUクラスは，一部追加しました．

- PPU.py
  - PPU_Init()：初期化処理
  - PPU_Fin()：終了処理
- CPU.py
  - CPU_Step()：N命令を実行するメソッド
    - FX29命令

今後の作業

グラフィックス系をTkinterで実装することを意識しつつ，PPUクラスの処理を実施します．

### 2006-10-15

進捗

PPUクラスを修正開始しました．

- PPU.py
  - PPU_Erase()：画面消去
  - PPU_Draw()：スプライトを表示
  - PPU_*Pixel()：ピクセル表示，等

### 2006-10-21

スクリーンショット

<img src="https://github.com/jay-kumogata/PyChip8/blob/master/screenshots/pychip8_061021_1.PNG" width="320px"/>

tkinterによるグラフィック描画が未完成のため，暫定でVRAMの中身をアスキーアートで表示する処理を作成しました．
Pongを実行して，20クロック目のスクリーンショットです．
Pythonでも，効率が悪いというだけで，エミュレータが書けないというわけじゃないみたいです．

進捗

PPUクラス，CPUクラスを修正しました．

- PPU.py
  - PPU_Dump()：画面ダンプ
- CPU.py
  - CPU_Step()：N命令を実行するメソッド
  - CPU_Read()，CPU_ReadW()：メモリへの読込み
  - CPU_Write()：メモリへの書込み

### 2006-10-24

概要

IOクラスに，Delayタイマ，Soundタイマを実装しました．
それにあわせて，Delayタイマ，Soundタイマ関連の命令を実装しました．
pongの30クロックまで，動作を確認しました．

進捗

IOクラスを新規作成しました．CPUクラスを修正しました．

IO.py
  - IO_Init()：初期化処理
  - IO_Fin()：終了処理

CPU.py
  - CPU_Step()：N命令を実行するメソッド

### 2006-10-29

スクリーンショット

<img src="https://github.com/jay-kumogata/PyChip8/blob/master/screenshots/pychip8_061029_1.PNG" width="320px"/>

前回のスクリーンショットと同じに見えますが、ボールが移動しているのが見えます．
Pongの400クロック目ぐらいのショットです．
もしかして、ポンについて知らない人がいるかもしれないので、以下、参照です．

- [ポン（ゲーム） wikipedia](http://ja.wikipedia.org/wiki/%E3%83%9D%E3%83%B3_(%E3%82%B2%E3%83%BC%E3%83%A0))

進捗

- System.py
  - Init()
    - 暫定で記述しているDelayタイマとCPUとのタイミング修正
- CPU.py
  - CPU_Step()：N命令を実行するメソッド
    - キーを押している/押していない時の分岐命令を追加

余談

これが終わったら，Javaで作っていたUPnPスタックを，Pythonに移植しようかな．
それから，昨日，OSC2006を見学しました．

### 2006-11-05

スクリーンショット

tkinterによる画面描画ルーチンを実装したので，ウィンドウに表示されるようになりました．

<img src="https://github.com/jay-kumogata/PyChip8/blob/master/screenshots/pychip8_061105_1.PNG" width="320px"/>

進捗状況

本当は，スレッドを使って，エミュレーションとウィンドウ処理を並列に処理するのだと思うのですが，pythonのスレッドがよく分かってないので，うまくいきませんでした．多分，ロックを掛ければいいと思います．これは，また来週かな．

- PyChip8.py
  - Init()
  - button1()
    - ウィンドウを生成して，マウスイベントにフックして，エミュレーションを進め，画面描画する処理を追加

### 2006-11-12

スクリーンショット

<img src="https://github.com/jay-kumogata/PyChip8/blob/master/screenshots/pychip8_061105_1.PNG" width="320px"/>

性能測定

先週実装した画面描画部は，DXYN命令が呼ばれるたびに，tkinterのキャンバスに，点を打つ方法です．この方法で，クロックを進めていくと，メモリ使用量がどんどん増えていって，400MBぐらいでハングアップになりました．

この方法は，ちょっと現実的じゃないことが分かったので，画面描画部を書き直すかもしれないです．

### 2006-12-09

スクリーンショット

<img src="https://github.com/jay-kumogata/PyChip8/blob/master/screenshots/pychip8_061216_0.PNG" width="320px"/>

進捗状況

tkinterで実装していたグラフィック処理は，性能的に破綻していたので，代替案を探していました．最近，PyGameという，Python/SDLのようなライブラリを発見したので，それを使って，書き直しました．threadとの相性もよく，そこそこの速度で，Chip8エミュレータが動き出しました．

PyGameインストール方法

- (a) Python2.4系（python-2.4.3.msi）のインストール
- (b) PyGame（pygame-1.7.1release.win32-py2.4.exe）のインストール
  - [PyGame](http://www.pygame.org/)
  - [初心者のためのpygameガイド](http://www.unixuser.org/~euske/doc/pygame/newbieguide-j.html)

### 2006-12-17

スクリーンショット

<img src="https://github.com/jay-kumogata/PyChip8/blob/master/screenshots/pychip8_061216_0.PNG" width="320px"/>

進捗状況

本日は，特に進捗なしです．スクリーンショットを載せておきます．性能測定をやりましたが，デバッグメッセージ等を表示させないと，そこそこの速度で動くことが分かりました（1/3 fpsぐらい）．

あとは，PyGameをhookして，キー処理をエミュレーションする等を実装する予定です．ただ，基本的に，このプロジェクトも終了かなという気もしています．次は，UPnPスタックとかに，挑戦しようかなぁ．

### 2006-12-23

スクリーンショット

<img src="https://github.com/jay-kumogata/PyChip8/blob/master/screenshots/pychip8_061223_0.PNG" width="320px"/>

（パドルが動いているのが進捗）

進捗状況

PyGameのキー処理をhookして，キーボードエミュレーションを実装しました．PyGameの場合も，エミュレーションスレッドとウィンドウ制御スレッドは，別々になります．今回は，ウィンドウ制御スレッドで，KEYDOWN，KEYUPイベントを拾って，キー情報を更新し，エミュレーションスレッドで，そのキー情報を読み取るように，実装しました．

- PyChip8.py
  - KEYDOWN，KEYUPイベントにしたがい，キー情報を更新

### 2006-12-29

スクリーンショット

<img src="https://github.com/jay-kumogata/PyChip8/blob/master/screenshots/pychip8_061223_0.PNG" width="320px"/>

（再掲）

進捗状況

最後に，コマンドライン引数で，ROMイメージを指定できるようにしたり，タイミングを調整したりして，ほぼリリースできる状態になりました．あとは，ドキュメントを整備したり，デバッグメッセージを出さないようにすれば，リリースかなと思ってます．

問題は，リリースしても，反響がなさそうなことぐらいでしょうか．


### 2007-01-02

スクリーンショット

<img src="https://github.com/jay-kumogata/PyChip8/blob/master/screenshots/pychip8_070102_0.PNG" width="320px"/>

進捗状況

スクリプト言語PythonによるCHIP8エミュレータ（PyChip8 v0.1J）をリリースしました．Pythonによるゲーム機エミュレータは，（たぶん）世界初です．

- [PyChip8 v0.1J](https://github.com/jay-kumogata/PyChip8)

概要

[README](https://github.com/jay-kumogata/PyChip8/blob/master/README.txt)から概要を転載します．

以上