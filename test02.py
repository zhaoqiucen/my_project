from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

# Uncomment the following line to enable verbose logging

# logging.basicConfig(level=logging.INFO)

# Create a new ChatBot instance

chatbot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',

    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],

    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    trainer='chatterbot.trainers.ListTrainer',
    database="xbt",
    database_uri="mongodb://127.0.0.1:27017/",
    read_only=True
)


while True:
    try:
        print(chatbot.get_response(input("user:")))
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
