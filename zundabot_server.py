import os

from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from zundabot import Zundabot

load_dotenv("./.env")
slack_token = os.environ.get("SLACK_AUTH_TOKEN")
slack_app_token = os.environ.get("SLACK_APP_TOKEN")
openai_api_key = os.environ.get("OPENAI_API_KEY")

chatbot = Zundabot(openai_api_key)

app = App(token=slack_token)

@app.message("")
def response(message, say):
    response = chatbot.ask(question=message['text'], userid=message['user'])
    say(response)

@app.event({
    "type": "message",
    "subtype": "file_share"
})
def file_response(message, say):
    say("ファイルを送信されても困るのだ。何もお答えできないのだ。")

@app.command("/zundabot")
def online(ack, respond, command):
    ack()
    respond("はいなのだ、何かごようなのだ？")

if __name__ == "__main__":
    SocketModeHandler(app, slack_app_token).start()
