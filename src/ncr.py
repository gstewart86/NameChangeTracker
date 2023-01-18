import requests
from slack_bolt import App
from slack_sdk.errors import SlackApiError

from settings import app_settings

app = App(token=app_settings.SLACK_APP_TOKEN)


def subscribe_to_name_change_event():
    headers = {
        "Authorization": f"Bearer {app_settings.SLACK_APP_TOKEN}",
        "Content-type": "application/json",
    }

    data = {
        "event_types": ["users_info"],
        "url": "https://your-server.com/name_change_event",
    }

    requests.post(
        "https://slack.com/api/events.subscriptions.add", json=data, headers=headers
    )


def name_change_event(event_data):
    user_id = event_data["user_id"]
    response = requests.get(
        f"https://slack.com/api/users.info?user={user_id}&token={SLACK_APP_TOKEN}"
    )
    user_info = response.json()
    old_name = user_info["user"]["name"]
    new_name = event_data["username"]
    if old_name != new_name:
        # perform desired actions, such as posting a message to a channel
        message = f"User <@{user_id}> has changed their display name from {old_name} to {new_name}."
        ack(message)


@app.command("/nc show")
def ncr(ack, respond, command):
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


if __name__ == "__main__":
    app.start()
