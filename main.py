from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import TOKEN

async def get_chat_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

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

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("getinfo", get_chat_info))

app.run_polling()

