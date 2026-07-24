from telegram import Update
from telegram.ext import ContextTypes
from database import add_tire, get_stock


async def stock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tires = get_stock()

    if not tires:
        await update.message.reply_text("📦 Склад пока пуст.")
        return

    text = "🛞 Склад шин:\n\n"

    for tire in tires:
        text += (
            f"🚗 {tire['brand']}\n"
            f"📏 Размер: {tire['size']}\n"
            f"☀️/❄️ Сезон: {tire['season']}\n"
            f"Количество: {tire['quantity']} шт.\n\n"
        )

    await update.message.reply_text(text)


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Пример добавления:\n"
        "/add Michelin 225/45R17 зима 4"
    )
