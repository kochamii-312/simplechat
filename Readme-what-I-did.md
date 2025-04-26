index.pyを編集

## Google Colab
1. GitHubクローン
2. .envファイル（トークン）読み込み
3. 03ディレクトリに移動
4. requirements.txtを使用して必要なパッケージをインストール
5. トークンの認証
6. python app.py -> FastAPIが起動 -> public_urlを取得

## simplechat
1. public_urlを```lambda/index.py```に組み込む
2. commitする

## CloudShell
1. リポジトリのクローン
2. npm install
3. デプロイ
4. アプリケーションにアクセス

### 実行したコマンド
```
mkdir /tmp/testdir
```
```
cd /tmp/testdir/
```
```
export npm_config_cache=/tmp/npm-cache
```
```
export npm_config_cache=/tmp/npm-global
```
```
sudo npm install -g aws-cdk@latest
```
```
git clone https://github.com/kochamii-312/simplechat.git
```
```
cd simplechat
```
```
npm install
```
```
cdk bootstrap
```
```
cdk deploy
```
