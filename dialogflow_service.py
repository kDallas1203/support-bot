import os
import logging
from google.cloud import dialogflow


class DialogFlowService:
    __GOOGLE_LANGUAGE_CODE = 'ru'
    __PROJECT_ID = os.environ.get('DIALOG_FLOW_PROJECT_ID')

    def __init__(self, session_prefix):
        self.session_client = dialogflow.SessionsClient()
	self.session_prefix = session_prefix

    def __get_session(self, session_id):
        return self.session_client.session_path(
            self.__PROJECT_ID, session_id)

    def detect_intent_texts(self, session_id, text):
        session = self.__get_session("{}_{}".format(self.session_prefix, session_id))

        text_input = dialogflow.TextInput(
            text=text, language_code=self.__GOOGLE_LANGUAGE_CODE)

        query_input = dialogflow.QueryInput(text=text_input)

        response = self.session_client.detect_intent(request={
            'session': session,
            'query_input': query_input
        })

        query_result = response.query_result

        logging.info('response: {}'.format(response))

        if query_result.intent.is_fallback:
            logging.warn('DialogFlowService return fallback')

        return query_result
