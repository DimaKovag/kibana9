import logging
import requests
import threading
from prometheus_client import start_http_server, Counter
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

messages_counter = Counter("received_messages_total", "Кількість отриманих повідомлень")

def start_metrics_server():
    start_http_server(9091)

metrics_thread = threading.Thread(target=start_metrics_server)
metrics_thread.daemon = True
metrics_thread.start()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
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
        logging.info("Лог надіслано у Fluentd")
    except Exception as e:
        logging.error(f"Не вдалося надіслати лог: {e}")

    messages_counter.inc()
    await update.message.reply_text("Виконано отримання та логування повідомлення")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущено. Дякую)")
    app.run_polling()