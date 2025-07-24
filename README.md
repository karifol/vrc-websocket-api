# VRChat WebSocket API コネクタ

このスクリプトは、VRChat WebSocket API への基本的な接続を確立し、リアルタイムメッセージを受信するためのものです。VRChat のライブデータストリームを操作したい場合の出発点として活用できます。

## 機能

- **WebSocket 接続の確立:** VRChat パイプライン WebSocket エンドポイントへ接続します。
- **認証:** `.env` ファイルから読み込んだ認証トークンを用いて、安全にアクセスします。
- **リアルタイムメッセージの受信:** WebSocket からのメッセージを継続的にリッスンし、表示します。
- **JSON パース:** 受信メッセージを JSON として解析し、読みやすい形式で出力します。
- **エラー処理:** 接続の問題や JSON 以外のメッセージに対する基本的なエラーハンドリングを備えています。

## 前提条件

このスクリプトを実行する前に、以下のソフトウェアがインストールされていることを確認してください。

- **Python 3.x**

また、以下の Python ライブラリが必要です。これらは `requirements.txt` を使ってインストールできます。

```bash
pip install -r requirements.txt
```

---

## セットアップ

1.  **スクリプトの取得:** `vrchat_websocket_connector.py` (またはあなたの環境では `websocket-api.py`) および `requirements.txt` ファイルを入手します。

2.  **`.env` ファイルの作成:** スクリプトと同じディレクトリに、`.env` という名前のファイルを作成します。このファイルに VRChat の認証トークンを記述します。

    ```
    AUTH_TOKEN="あなたの_vrchat_auth_token_をここに"
    ```

    **重要:** `"あなたの_vrchat_auth_token_をここに"` の部分を、実際の VRChat 認証トークンに置き換えてください。通常、このトークンは VRChat ウェブサイトにログインしている際のブラウザの開発者ツールから取得できます。`AUTH_TOKEN` は VRChat アカウントへのアクセス権を与えるものなので、**絶対に他者と共有しないでください**。

---

## 実行方法

ターミナルからスクリプトを実行します。

```bash
python websocket-api.py
```

接続が成功すると、「WebSocket connection established.」と表示され、VRChat API からのメッセージが続けて表示されます。スクリプトは、手動で停止するまで（例: `Ctrl+C` を押す）、メッセージの受信と表示を続けます。

---

## 出力の理解

VRChat WebSocket API からのメッセージは、通常 JSON 形式です。スクリプトはこれらを解析し、整形して表示しようとします。受信した JSON の `content` フィールドは、さらに別の JSON 文字列である場合が多く、スクリプトはこれも解析してより読みやすく表示します。

パースされた出力の例：

```
Received at 2024-01-01 12:34:56: {
  "type": "someMessageType",
  "content": {
    "userId": "usr_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "message": "Hello from VRChat!",
    "timestamp": "2024-01-01T03:30:00.000Z"
  }
}
```

メッセージが有効な JSON でない場合は、「Received non-JSON message:」として生のデータが出力されます。

---

## 免責事項

このスクリプトは、VRChat WebSocket API への接続方法を理解するための**教育的およびデモンストレーション目的**で提供されています。VRChat の API 利用規約および利用ポリシーを常に確認し、遵守する責任は利用者自身にあります。

---

この README で、スクリプトのセットアップや使用方法がより明確になったでしょうか？
