from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Функция для обработки сообщений
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(text)

token = '7714966043:AAHoLDGuylx7uClhr6FcJ_AIWVjuvTzve2M' # TODO Убрать из кода !

app = Application.builder().token(token).build()
app.add_handler(MessageHandler(filters.TEXT, start))

app.run_polling()
