
````markdown
# 📡 Моніторинг із Prometheus + Grafana + Telegram Bot

Цей репозиторій демонструє, як запустити моніторинг системи за допомогою **Prometheus**, **Grafana** та **Telegram-бота**, який видає метрики на `/metrics`.

---

## 🔧 1. Запуск Prometheus + Grafana

1. Перейдіть у директорію з `docker-compose.yml`:

   ```bash
   cd ./prometheus-lab/PrometheusLab
````

2. Запустіть контейнери:

   ```bash
   docker compose up
   

3. Переконайтесь, що сервіси доступні:

   * 🔗 Prometheus: [http://127.0.0.1:9090](http://127.0.0.1:9090)
   * 📊 Grafana: [http://127.0.0.1:3000](http://127.0.0.1:3000)

---

## 🤖 2. Запуск Telegram-бота з метриками

1. Перейдіть у директорію бота:

   
Bash

   cd ./telegram_bot
   

2. Якщо ще немає віртуального середовища, створіть і активуйте його:

   
Bash

   python -m venv venv
   source venv/Scripts/activate  # або source venv/bin/activate на Linux/macOS
   pip install -r requirements.txt
   

3. Запустіть бота:

   
Bash

   python bot.py
   

4. Перевірте метрики:

   * 📈 Відкрий у браузері: [http://127.0.0.1:9091/metrics](http://127.0.0.1:9091/metrics)
   * Ви побачите щось на кшталт:

     

     # HELP received_messages_total Total number of received Telegram messages
     # TYPE received_messages_total counter
     received_messages_total 5.0
     

---

## 📊 3. Налаштування Grafana

1. Відкрий Grafana: [http://127.0.0.1:3000](http://127.0.0.1:3000)

   * Логін: admin
   * Пароль: admin

2. Додай джерело даних (Data Source):

   * Натисни: ☰ → Connections → Data Sources

   * Обери: Add data source

   * Тип: Prometheus

   * URL:

     

     http://prometheus:9090
     

   * Натисни: Save & test

---

## 📈 4. Створення Dashboard у Grafana

1. У Grafana натисни: Dashboards → New → Explore

2. У полі Metrics введи:

   

   received_messages_total
   

3. Натисни Run Query, після цього:

   * Add to dashboard → New panel
   * Дай назву панелі
   * Збережи Dashboard

---

## 🛑 5. Зупинка всіх сервісів

### Зупинити Prometheus + Grafana

Bash

cd ./prometheus-lab/PrometheusLab
docker compose down

### Зупинити Telegram-бота

* Натисни Ctrl + C у терміналі
* Деактивуй середовище:

  
Bash

  deactivate
  

---

## 📎 Корисні посилання

* 🔍 Prometheus: [http://127.0.0.1:9090](http://127.0.0.1:9090)
* 📊 Grafana: [http://127.0.0.1:3000](http://127.0.0.1:3000)
* 📈 Метрики бота: [http://127.0.0.1:9091/metrics](http://127.0.0.1:9091/metrics)
