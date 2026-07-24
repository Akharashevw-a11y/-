from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8899387636:AAE_lIm_sgpXkcwv8S5rbeTZlrOCiT73qJQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛞 Добро пожаловать!\n"
        "Это бот моего склада шин.\n\n"
        "Команды:\n"
        "/stock — посмотреть склад"
    )

async def stock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 Склад пока пуст.\n"
        "Скоро здесь появится список шин."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stock", stock))

app.run_polling()
