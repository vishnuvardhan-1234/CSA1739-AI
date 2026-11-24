import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello", ["Hello!"]],
    [r"what is your name", ["I am a chatbot."]],
    [r"how are you", ["I am fine."]],
    [r"bye", ["Goodbye!"]]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
