# lambda/index.py
# このコードは、ngrokで公開された FastAPIチャットAPIにアクセスするPythonクライアントです

import urllib.request
import json
import time

class ChatClient:
    """FastAPIチャットAPI クライアントクラス"""
    
    def __init__(self, api_url):
        """
        初期化

        Args:
            api_url (str): API のベース URL(ngrok URL)
        """
        self.api_url = api_url.rstrip('/')
    
    def generate(self, message, conversation_history=None):
        """
        メッセージを送信して応答を受け取る

        Args:
            message (str): ユーザーからのメッセージ
            conversation_history (list, optional): 過去の会話履歴

        Returns:
            dict: 応答結果
        """
        url = f"{self.api_url}/chat"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "message": message,
            "conversationHistory": conversation_history or []
        }
        
        data = json.dumps(payload).encode('utf-8')
        
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        
        start_time = time.time()
        with urllib.request.urlopen(req) as res:
            body = res.read()
        total_time = time.time() - start_time

        result = json.loads(body.decode('utf-8'))
        result["total_request_time"] = total_time
        
        return result

# 使用例
if __name__ == "__main__":
    # ngrokで割り当てられたURLを設定（実際のngrok URLに変えてね）
    NGROK_URL = "https://729e-34-23-148-76.ngrok-free.app/"
    
    # クライアント初期化
    client = ChatClient(NGROK_URL)
    
    # 単一メッセージ送信
    print("Simple chat:")
    result = client.generate("AIについて100文字で教えてください。")
    print(f"Assistant's Response: {result['response']}")
    print(f"Total request time: {result['total_request_time']:.2f}s")
