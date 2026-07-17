
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

from config import TELEGRAM_TOKEN
from news import get_positive_news


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome!\n\n"
        "/news - Positive NSE News\n"
    )


async def news_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    news = get_positive_news()

    text = "📰 Positive NSE Announcements\n\n"

    for item in news:
        text += (
            f"📈 {item['stock']}\n"
            f"News: {item['news']}\n"
            f"Impact: {item['impact']}\n\n"
        )

    await update.message.reply_text(text)


def main():

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news_command))

    print("Garuda AI Trader Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
