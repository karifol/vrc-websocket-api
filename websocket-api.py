# -*- coding:utf-8 -*-
from websocket import create_connection
from datetime import datetime
import json
import os
import dotenv

dotenv.load_dotenv()
auth_token = os.getenv('AUTH_TOKEN')

ws = None
try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
    }

    ws = create_connection(
        f"wss://pipeline.vrchat.cloud/?authToken={auth_token}",
        header=list(f"{k}: {v}" for k, v in headers.items())
    )
    print("WebSocket connection established.")

    #受信したメッセージを表示
    while True:
        recv = ws.recv()
        try:
            # JSONとしてパースを試みる
            data = json.loads(recv)
            data['content'] = json.loads(data['content']) if isinstance(data.get('content'), str) else data.get('content', {})
            print(f"Received at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {json.dumps(data, indent=2, ensure_ascii=False)}")
        except json.JSONDecodeError:
            print(f"Received non-JSON message: {recv}")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    if ws is not None:
        ws.close()
    print("connection close")
