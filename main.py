from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import TOKEN

async def get_chat_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    chat_id = update.message.chat.id

    reply_message = f"""
    Information about this chat:

Chat ID – "`{chat_id}`"
    """

    # await update.message.reply_text(f"Hello from python!")
    await update.message.reply_text(reply_message, parse_mode='MarkdownV2')

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("getinfo", get_chat_info))

app.run_polling()

