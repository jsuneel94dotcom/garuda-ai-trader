from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

from config import TELEGRAM_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome!\n\n"
        "/scan - Swing Scan\n"
        "/news - Positive NSE News\n"
        "/help - Help"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available Commands:\n\n"
        "/scan - Find swing stocks\n"
        "/news - Show positive NSE announcements\n"
        "/help - Show this help message"
    )


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔍 Scanning stocks...\n\n"
        "Feature coming in next step."
    )


async def news_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📰 Fetching positive NSE announcements...\n\n"
        "Feature coming in next step."
    )


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("scan", scan))
    app.add_handler(CommandHandler("news", news_command))

    print("Garuda AI Trader Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
