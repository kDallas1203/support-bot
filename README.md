# Боты тех.поддержки для VK и Telegram
Вы можете с легкостью создать бота тех. поддержки для вашего бизнеса. Следуя инструкции ниже

## Установка
Для работы с ботами вам необходимо завести проект [Dialogflow](https://dialogflow.cloud.google.com/#/agent/devman-support-bot-303110/intents)

Установите зависимости

```
pip3 install -r requirements.txt
```

Создайте переменные окружения

```
TELEGRAM_BOT_TOKEN= Токен от бота в телеграм
GOOGLE_APPLICATION_CREDENTIALS = Путь к файлу ключей Google созданный на этапе подготовки проекта Dialogflow
DIALOG_FLOW_PROJECT_ID = Projectid из файла ключей Google
VK_API_KEY= Токе от бота в сообществе ВК
```

Запустите бота Telegram
```
python3 telegram-bot.py
```

Запустите бота ВК
```
python3 vk-bot.py
```

## Тренировка бота
Вы можете тренировать бота в консоли Dialogflow. Если у вас есть заготовки, то можно запустить скрипт для загурзки ваших тренировочных вопросов и ответов

Откройте файл questions.json и заполните его как сделано на примерах в файле

Запустите скрипт
```
python3 upload_intent_script.py
```
