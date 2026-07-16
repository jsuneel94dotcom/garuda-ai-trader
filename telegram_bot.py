
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

from config import TELEGRAM_TOKEN
from news import get_positive_news


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🤖 Garuda AI Trader

Welcome!

Commands:

/scan - Swing scan
/ news - Positive NSE announcements
/ help - Help
"""
    await update.message.reply_text(text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Garuda AI Trader is under development."
    )


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔍 Scanning stocks...\n\nFeature coming in next step."
    )


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):

    items = get_positive_news()

    text = "📰 Positive NSE Announcements\n\n"

    for item in items:
        text += (
            f"Stock: {item['stock']}\n"
            f"News: {item['news']}\n"
            f"Impact: {item['impact']}\n\n"
        )

    await update.message.reply_text(text)


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("scan", scan))
    app.add_handler(CommandHandler("news", news))

    print("Garuda AI Trader Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
