from telegram import *
from telegram.ext import *
import model

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
"Доступные команды\n\n\
/help - этот текст\n\
/start - начать заново\n\
/playerX - игрок играет за X, бот за O\n\
/player0 - игрок играет за O, бот за X")

async def defstate(update: Update, context: CallbackContext) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=model.get_status(), reply_markup=model.get_table())

async def start(update: Update, context: CallbackContext) -> None:
    model.reset()
    await defstate(update, context)

async def playerX(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    model.set_playerX()
    await defstate(update, context)

async def player0(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    model.set_player0()
    await defstate(update, context)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global value
    global keyboard
    query = update.callback_query