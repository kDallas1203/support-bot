import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from dialogflow_service import DialogFlowService

logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self):
        self.updater = Updater(os.environ['TELEGRAM_BOT_TOKEN'])

        self.df_service = DialogFlowService('tg')

        self.updater.dispatcher.add_handler(
            CommandHandler('start', self._start_handler))
        self.updater.dispatcher.add_handler(
            MessageHandler(Filters.text, self._send_answer))

    def _start_handler(self, bot, update):
        chat_id = update.message.chat_id
        logger.info('Bot was started by {}'.format(chat_id))
        bot.send_message(chat_id=chat_id, text='Здрвствуйте!')

    def _send_answer(self, bot, update):
        logger.info('Telegram bot receive echo message from {}'.format(
            update.message.chat_id))
        df_response = self.df_service.detect_intent_texts(
            session_id=update.message.chat_id, text=update.message.text)
        update.message.reply_text(df_response.fulfillment_text)

    def start_bot(self):
        self.updater.start_polling()
        logger.info('Telegram bot started')

    def stop_bot(self):
        self.updater.idle()
        logger.info('Telegram bot stopped')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger.setLevel(logging.INFO)

    telegram_bot = TelegramBot()
    telegram_bot.start_bot()
    telegram_bot.stop_bot()
