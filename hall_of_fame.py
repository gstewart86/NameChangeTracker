from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt import App
from typing import Any
from pydantic import BaseSettings

settings = BaseSettings(_env_file=".env")
client = WebClient(token=settings.SLACK_BOT_TOKEN)
app = App(token=settings.SLACK_BOT_TOKEN)


@app.command("/hello")
def hello_command(ack, respond, command):
    # Acknowledge command request
    ack()

    try:
        # Call the chat.postMessage method using the WebClient
        response = client.chat_postMessage(channel="#general", text="Hello World!")
        print(response)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        # (caused by an error returned by the Slack API)
        print("Error: {}".format(e))


@app.command("/feature_request show")
def show_feature_requests(ack, respond, command):
    # Acknowledge command request
    ack()

    with open("feature_request", "r") as req_list:
        feat_list = req_list.read()

    try:
        # Call the chat.postMessage method using the WebClient
        response = client.chat_postMessage(channel="#general", text=feat_list)
        print(response)
    except SlackApiError as e:
        print("Error: {}".format(e))


@app.command("/feature_request")
def submit_feature_request(ack, respond, command):
    # Acknowledge command request
    ack()

    req = command.text.replace("/feature_request", "")
    req = req.replace(" ", "")

    with open("feature_request", "a") as feat_req:
        feat_req.write(req + "\n")

    try:
        # Call the chat.postMessage method using the WebClient
        response = client.chat_postMessage(
            channel="#general", text="feature request submitted: " + req
        )
        print(response)
    except SlackApiError as e:
        print("Error: {}".format(e))


@app.command("/halloffame show")
def show_hall_of_fame(ack, respond, command):
    # Acknowledge command request
    ack()

    with open("hall_of_fame_names", "r") as fame_list:
        names = fame_list.read()

    try:
        # Call the chat.postMessage method using the WebClient
        response = client.chat_postMessage(channel="#general", text=names)
        print(response)
    except SlackApiError as e:
        print("Error: {}".format(e))


@app.command("/halloffame")
def add_to_hall_of_fame(ack, respond, command):
    # Acknowledge command request
    ack()

    name = command.text.replace("/halloffame", "")
    name = name.replace(" ", "")

    with open("hall_of_fame_names", "a") as fame_list:
        fame_list.write(name + "\n")

    try:
        # Call the chat.postMessage method using the WebClient
        response = client.chat_postMessage(
            channel="#general",
            text=name
            + " has been added to the Hall of Fame. To see the hall of fame list, say /hall_of_fame show'",
        )
    except SlackApiError as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    app.start()
