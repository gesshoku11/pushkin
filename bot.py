from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, ContextTypes, CommandHandler

from credentials import ChatGPT_TOKEN, BOT_TOKEN
from gpt import ChatGptService
from util import (load_message, send_text, send_image, show_main_menu,
                  default_callback_handler, load_prompt, send_text_buttons)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = load_message('main')
    await send_image(update, context, 'main')
    await send_text(update, context, text)
    await show_main_menu(update, context, {
        'start': 'Главное меню',
        'random': 'Узнать случайный интересный факт 🧠',
        'gpt': 'Задать вопрос чату GPT 🤖',
        'talk': 'Поговорить с известной личностью 👤',
        'quiz': 'Поучаствовать в квизе ❓'
        # Добавить команду в меню можно так:
        # 'command': 'button text'

    })

stop_markup = InlineKeyboardMarkup([[InlineKeyboardButton('Закончить', callback_data='stop')]])

async def random(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_image(update, context, 'random')
    messege = await send_text(update, context, 'Вспоминаю интересный факт...🫠')
    prompt = load_prompt('random')
    answer = await chat_gpt.send_question(prompt, '')

    await send_text_buttons(update, context, answer, {
        'random_more' : 'Еще факт 😈',
        'stop': 'Закончить'
    })
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await start(update, context)

async def random_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await random(update, context)

chat_gpt = ChatGptService(ChatGPT_TOKEN)
app = ApplicationBuilder().token(BOT_TOKEN).build()


app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('random', random))


# Зарегистрировать обработчик команды можно так:
# app.add_handler(CommandHandler('command', handler_func))

# Зарегистрировать обработчик коллбэка можно так:
# app.add_handler(CallbackQueryHandler(app_button, pattern='^app_.*'))
app.add_handler(CallbackQueryHandler(stop, 'stop'))
app.add_handler(CallbackQueryHandler(random_button, '^random_.*'))
app.add_handler(CallbackQueryHandler(default_callback_handler))
app.run_polling()
