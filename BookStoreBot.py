from flask import Flask, render_template, request


import telegram

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def webhook():
     key_token = "1672147288:AAF1IvWC2MmCBZ-XpqaOdCuHbN64XwezZO0"
     bot = Bot(key_token)
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id     = update.effective_chat.id
        text        = update.message.text
        first_name  = update.effective_chat.first_name
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text=f"{text} {first_name}")
        return 'ok'
    return 'error'

def index():
    return webhook()
