impor# ВЕРСИЯ 2
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from handlers import stock, add


TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛞 Добро пожаловать!\n"
        "Это бот моего склада шин.\n\n"
        "Команды:\n"
        "/stock — посмотреть склад\n"
        "/add — добавить шины"
    


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stock", stock))
app.add_handler(CommandHandler("add", add))


app.run_polling()
