import os

from dotenv import load_dotenv

#from slackbot import SlackBot
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from chatbotgpt import ChatBotGPT

load_dotenv("./.env")
slack_token = os.environ.get("SLACK_AUTH_TOKEN")
slack_app_token = os.environ.get("SLACK_APP_TOKEN")
slack_channel_id = os.environ.get("SLACK_APP_CHANNEL_ID")
openai_api_key = os.environ.get("OPENAI_API_KEY")

chatbot = ChatBotGPT(openai_api_key)

app = App(token=slack_token)

@app.message("")
def response(message, say):
    response = chatbot.ask(message['text'])
    say(response)

@app.event({
    "type": "message",
    "subtype": "file_share"
})
def file_response(message, say):
    say("ファイルを送信されても困るのだ。何もお答えできないのだ。")

if __name__ == "__main__":
    SocketModeHandler(app, slack_app_token).start()
