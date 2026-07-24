from telegram import Update
from telegram.ext import ContextTypes


async def stock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 Склад пока пуст.\n"
        "Скоро здесь появится список шин."
    )


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛞 Добавление шин.\n\n"
        "Пример:\n"
        "/add Michelin 225/45R17 зима 4"
    )
