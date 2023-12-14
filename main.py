from flask import Flask, request, jsonify
import telegram
from telebot.credentials import bot_token

bot = telegram.Bot(token=bot_token)

app = Flask(__name__)


@app.route('/test')
async def index():
    async with bot:
        await bot.sendMessage(text='Hi', chat_id='1665734870')
        await bot.sendMessage(text='Hi', chat_id='286058740')
        await bot.sendMessage(text='Hi', chat_id='194362579')
    return 'Hello!!!'


@app.route('/coin/pump/notification', methods=['POST'])
async def coin_notification():
    api_key = request.headers.get('API-Key')
    if not api_key or not api_key == 'c0981f8c-3e25-4697-9b75-07a0595b75ec':
        return jsonify({'error': 'Unauthorized'}), 401
    async with bot:
        await bot.sendMessage(text=request.json, chat_id='1665734870')
        await bot.sendMessage(text=request.json, chat_id='286058740')
        await bot.sendMessage(text=request.json, chat_id='194362579')
    return 200


if __name__ == '__main__':
    app.run(port=8000, debug=True, threaded=True)
