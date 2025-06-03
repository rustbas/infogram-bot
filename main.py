import os

from sys import stderr

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import logging
logging.basicConfig(level=logging.INFO, stream=stderr,
                        format="%(asctime)s %(levelname)s %(message)s")

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    raise Exception("You need to provide telegram token. Set \'TELEGRAM_TOKEN\' variable.")

async def get_chat_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user_name = update.message.chat.username
    logging.info(f"User:{user_name} ran command \'getinfo\'")

    chat_id = update.message.chat.id
    chat_type = update.message.chat.type

    if chat_type == 'supergroup':
        thread_id = update.message.message_thread_id
        if thread_id is None:
            thread_id = 0
        thread_message = f"Thread ID – \"`{thread_id}`\""
    else:
        thread_message = f"There is no threads here"

    reply_message = f"""
    Information about this chat:

Chat type – "`{chat_type}`"
Chat ID – "`{chat_id}`"
{thread_message}
    """

    await update.message.reply_text(reply_message, parse_mode='MarkdownV2')

async def get_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user_name = update.message.chat.username
    logging.info(f"User:{user_name} ran command \'help\'")

    help_message = """
This bot return chat info, that may be useful in different services \\(zabbix, uptime\\-kuma, etc\\)\\.

Usage: `/getinfo`
    """

    await update.message.reply_text(help_message, parse_mode='MarkdownV2')


app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("getinfo", get_chat_info))
app.add_handler(CommandHandler("help", get_help))

app.run_polling()

