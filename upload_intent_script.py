import os
import json
import logging
from google.cloud import dialogflow


def upload_intent(project_id, intent):
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)

    response = intents_client.create_intent(request={
        'parent': parent,
        'intent': intent
    })

    logging.info('Intent created: {}'.format(response))


def serialize_questions(question):
    training_phrases = []
    for question in question:
        part = dialogflow.Intent.TrainingPhrase.Part(text=question)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)
    return training_phrases


def get_intent_message(answer):
    return dialogflow.Intent.Message(text=text)


def get_intents(questions):
    intents = []

    for display_name, question_data in questions.items():

        training_phrases = serialize_questions(question_data['questions'])
        messages = [get_intent_message(question_data['answer'])]

        intents.append(
            dialogflow.Intent(display_name=display_name,
                              messages=messages,
                              training_phrases=training_phrases))

    return intents


def main():
    PROJECT_ID = os.environ.get('DIALOG_FLOW_PROJECT_ID')
    logging.basicConfig(level=logging.INFO)
    try:
        with open("questions.json", "r") as question_json:
            questions = json.load(question_json)

        intents = get_intents(questions)

        for intent in intents:
            upload_intent(PROJECT_ID, intent)

    except FileNotFoundError:
        logging.error('File not found', exc_info=True)


if __name__ == '__main__':
    main()
