import logging
from telegram_bot import TelegramBot
from vk_bot import VkBot

logging.basicConfig(level=logging.INFO)

def main():
    telegram_bot = TelegramBot()
    vk_bot = VkBot()
    vk_bot.start_bot()
    telegram_bot.start_bot()
    telegram_bot.stop_bot()


if __name__ == '__main__':
    main()
