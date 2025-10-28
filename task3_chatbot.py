import random
import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello there! 👋", "Hi!", "Hey! How can I help you?"]],
    [r"how are you(.*)", ["I'm doing great, thank you! How about you?"]],
    [r"(.*) your name", ["I'm CodTechBot, your virtual assistant!"]],
    [r"(.*) help (.*)", ["Sure! I can assist you with your internship tasks or Python queries."]],
    [r"(.*) weather(.*)", ["Please check OpenWeatherMap API for real-time weather updates."]],
    [r"(.*) bye|quit|exit", ["Goodbye! Have a great day 😊"]],
    [r"(.*)", ["I'm sorry, I didn’t quite understand that. Could you please rephrase?"]],
]

# Create and start the chatbot
def chatbot():
    print("🤖 CodTech Chatbot: (type 'quit' to exit)")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run chatbot
if __name__ == "__main__":
    chatbot()
