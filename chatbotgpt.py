import openai

class ChatBotGPT(object):
    #How many contexs are remenbered.
    MAXMEMORY = 10

    def __init__(self, apikey=None, sys_conf=None):
        self.apikey = apikey
        self.system = []
        for sys in sys_conf:
            self.system.append({"role": "system", "content": sys})
        self.assistant = {}
        self.user = {}

    def clear_memory(self, userid):
        self.assistant[userid].clear()
        self.user[userid].clear()

    def ask(self, question=None, userid=None):
        openai.api_key = self.apikey

        if type(question) is not str:
            return "invalid value error."

        try:
            querys=[]
            #system
            for sys in self.system:
                querys.append(sys)
            #context
            self.user.setdefault(userid, [])
            self.assistant.setdefault(userid, [])
            for user, ass in zip(self.user[userid], self.assistant[userid]):
                querys.append(user)
                querys.append(ass)
            #question
            user_query = {"role": "user", "content": question}
            querys.append(user_query)

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=querys,
            )

            response_message = response["choices"][0]["message"]["content"]
            assistant_query = {"role": "assistant", "content": response_message}

            if((len(self.user[userid]) > self.MAXMEMORY) and
               (len(self.assistant[userid]) > self.MAXMEMORY)):
                self.clear_memory(userid)

            self.user[userid].append(user_query)
            self.assistant[userid].append(assistant_query)

            return response_message
        except:
            return "error"
