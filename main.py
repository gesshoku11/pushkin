import datetime

from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler

from util import send_text, send_image


# Функция для обработки сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # context.user_data [''] - хранить данные
    print(f'{text}, - {update.effective_user.full_name} | {datetime.datetime.now()}')
    await context.bot.send_message(update.effective_chat.id, f'Вы написали: {text}')


async def default_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_image(update, context, 'gpt')
    await send_text(update, context, 'Привет и добро пожаловать 😎')



token = '7714966043:AAHoLDGuylx7uClhr6FcJ_AIWVjuvTzve2M' # TODO Убрать из кода !
app = Application.builder().token(token).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
app.add_handler(CommandHandler('start', default_command_handler))

app.run_polling()
