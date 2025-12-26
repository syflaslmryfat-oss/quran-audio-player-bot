import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

RECITERS = {
    "qatami": "Nasser Al Qatami",
    "mishary": "Mishary Rashid Alafasy",
    "raad": "Raad Mohammad Al Kurdi",
    "tariq": "Tariq Mohammed",
    "nufais": "Ahmed Al Nufais"
}

@bot.message_handler(commands=['start'])
def start(message):
    kb = InlineKeyboardMarkup(row_width=1)
    for k, v in RECITERS.items():
        kb.add(InlineKeyboardButton(v, callback_data=f"reciter_{k}"))
    bot.send_message(message.chat.id, "👳‍♂️ ক্বারী নির্বাচন করুন:", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data.startswith("reciter_"))
def reciter(c):
    key = c.data.split("_")[1]
    bot.answer_callback_query(c.id)
    bot.send_message(c.message.chat.id, f"আপনি বেছে নিয়েছেন: {RECITERS[key]}")

bot.infinity_polling()
