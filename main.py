from flask import Flask, request, render_template
import csv
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def load_messages():
    k = {}
    csv_path = os.path.join(os.path.dirname(__file__), 'messages.csv')
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            k[row['phone']] = row['message']
    return k


@app.route('/df', methods=['POST'])
def handleWebhook1():

    req = request.get_json()

    responseText = ""
    intent = req["queryResult"]["intent"]["displayName"]

    if intent == "PhoneNumber":
        valueE = str(int(req["queryResult"]["parameters"]["number"]))

        k = load_messages()

        if valueE in k:
            responseText = k[valueE]
        else:
            responseText = "Hey, I am sorry. You are a good human but my chatbot is not able to identify you as of now. Please enter the last 4 digits of the phone number by which we have connected."

        res = {"fulfillmentMessages": [{"text": {"text": [responseText]}}]}

    else:
        responseText = f"There are no fulfillment responses defined for Intent {intent}"
        res = {"fulfillmentMessages": [{"text": {"text": [responseText]}}]}

    return res


@app.route('/')
def root():
    agent_id = os.getenv("DIALOGFLOW_AGENT_ID")
    return render_template('base.html', dialogflow_agent_id=agent_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)