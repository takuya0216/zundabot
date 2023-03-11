import openai
from dotenv import load_dotenv

class ChatBotGPT(object):
    def __init__(self, apikey=None):
        self.apikey = apikey

    def ask(self, question=None):
        openai.api_key = self.apikey

        if type(question) is not str:
            return "不正な入力なのだ。"

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "全ての文章の語尾に「なのだ」と付けて返事をしてください。"},
                    {"role": "system", "content": "必要な場合には、返事の最初に挨拶など気の利いた一言添えてから回答してください。文脈的におかしい場合は不要です。"},
                    {"role": "user", "content": question},
                ]
            )
            return response["choices"][0]["message"]["content"]
        except:
            return "error"
