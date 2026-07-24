from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8899387636:AAE_lIm_sgpXkcwv8S5rbeTZlrOCiT73qJQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Бот работает.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
