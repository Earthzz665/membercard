from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Channel access token ที่ได้จาก LINE Developers Console
LINE_ACCESS_TOKEN = 'Iff1ocURPUWY9f2TmB62jLMPH9pBrwVfHi3tM2pcAXDxXJIRdkjHjIHn4t9CgR0bu84IoghBreCEQcjzKGTBnj5sJpVawYs65cBhPfl2PY0NoJ5+vu5+Hy1ABCGHlj2XuV5Jj4soALDoeF/O5YZw3AdB04t89/1O/w1cDnyilFU='
LINE_API_URL = 'https://api.line.me/v2/bot/message/reply'

def reply_message(reply_token, text_message):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINE_ACCESS_TOKEN}'
    }
    data = {
        'replyToken': reply_token,
        'messages': [{'type': 'text', 'text': text_message}]
    }
    response = requests.post(LINE_API_URL, headers=headers, json=data)
    print(response.status_code, response.text)

@app.route('/webhook', methods=['POST'])
def webhook():
    body = request.json
    events = body.get('events', [])
    for event in events:
        if event['type'] == 'message' and event['message']['type'] == 'text':
            reply_token = event['replyToken']
            user_message = event['message']['text']
            reply_message(reply_token, f'You said: {user_message}')
    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5000)
