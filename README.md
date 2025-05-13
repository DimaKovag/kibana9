# 📊 Як запустити та зупинити EFK-стек і Telegram-бота

## 🚀 1. Як запустити EFK-стек

1. Перейдіть у директорію з конфігурацією `docker-compose.yml`:

   ```bash
   cd ./EFK-stack
   ```

2. Запустіть усі сервіси у фоновому режимі:

   ```bash
   docker compose up
   ```

3. Відкрийте Kibana у браузері:

   ```
   http://localhost:5601
   ```

4. **(Після кожного перезапуску)** потрібно додати шаблон індексу (index pattern) у Kibana:

   * Перейдіть до **Stack Management → Index Patterns**

   * Натисніть **Create index pattern**

   * У полі шаблону (pattern) введіть:

     ```
     fluentd-*
     ```

   * Натисніть **Next step**

   * У полі вибору часу оберіть:

     ```
     @timestamp
     ```

   * Натисніть **Create index pattern**

---

## 🤖 2. Як запустити Telegram-бота

1. Перейдіть у директорію з ботом:

   ```bash
   cd telegram_bot
   ```

2. Активуйте віртуальне середовище:

   ```bash
   source venv/Scripts/activate
   ```

   > Якщо середовище ще не створене, виконайте:

   ```bash
   python -m venv venv
   source venv/Scripts/activate
   pip install -r requirements.txt
   ```

3. Запустіть бота:

   ```bash
   python bot.py
   ```

4. Надішліть повідомлення боту в Telegram, щоб протестувати його.

---

## ✅ 3. Перевірка логів у Kibana

1. Відкрийте Kibana:

   ```
   http://localhost:5601
   ```

2. Переконайтесь, що після відправки повідомлення боту, у Kibana з'являються нові логи (на вкладці **Discover**).

---

## 🛑 4. Як зупинити Telegram-бота

1. У терміналі, де працює бот, натисніть `Ctrl + C`.
2. Деактивуйте віртуальне середовище:

   ```bash
   deactivate
   ```

---

## 🧯 5. Як безпечно зупинити EFK-стек

1. Перейдіть у директорію з `docker-compose.yml`:

   ```bash
   cd ./EFK-stack
   ```

2. Зупиніть усі сервіси:

   ```bash
   docker compose down
   ```

   > Це безпечно завершить роботу всіх компонентів (Elasticsearch, Fluentd, Kibana) і видалить контейнери, зберігаючи при цьому дані у volume-ах.

---
