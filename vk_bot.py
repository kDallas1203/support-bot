import os
import random
import logging
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dialogflow_service import DialogFlowService


class VkBot:
    def __init__(self):
        vk_session = vk_api.VkApi(token=os.environ['VK_API_KEY'])
        self.vk_api = vk_session.get_api()
        self.longpoll = VkLongPoll(vk_session)
        self.df_service = DialogFlowService()

    def start_bot(self):
        logging.info('VK bot started longpoll')
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                self._echo(event)

    def _echo(self, event):
        logging.info('VK bot receive echo message from {}'.format(
            event.user_id))
        df_response = self.df_service.detect_intent_texts(
            session_id=event.user_id, text=event.text)

        if  "is_fallback" not in df_response.intent:
            self.vk_api.messages.send(user_id=event.user_id,
                                      message=df_response.fulfillment_text,
                                      random_id=random.randint(1, 1000))
