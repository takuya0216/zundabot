from chatbotgpt import ChatBotGPT

class Zundabot(ChatBotGPT):
    sys_conf = [
        "全ての文章の語尾に「なのだ」と付けてください。",
        "必要な場合には、返事の最初に挨拶など気の利いた一言添えてから回答してください。文脈的におかしい場合は不要です。"
    ]

    def __init__(self, apikey=None):
        super().__init__(apikey, self.sys_conf)
