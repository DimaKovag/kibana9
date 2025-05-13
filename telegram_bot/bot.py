import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = "7652736409:AAGJ7vyzgbdT_pDp6obZXbJ6j8iDnCzhYNU"
FLUENTD_URL = "http://localhost:8080" 

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message.text

    data = {
        "UserId": user.id,
        "UserName": user.username,
        "Text": message,
    }

    try:
        requests.post(FLUENTD_URL, json=data)
        logging.info("Лог у Fluentd")
    except Exception as e:
        logging.error(f"Помилка надсилання логу: {e}")

    await update.message.reply_text("Отримав повідомлення, перевірте логи!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Бот запущено.")
    app.run_polling()
