import json
import random
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

with open("intents.json", "r") as file:
    data = json.load(file)

def chatbot_response(user_input):
    words = nltk.word_tokenize(user_input.lower())
    words = [lemmatizer.lemmatize(word) for word in words]

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_words = nltk.word_tokenize(pattern.lower())
            pattern_words = [lemmatizer.lemmatize(word) for word in pattern_words]

            if all(word in words for word in pattern_words):
                return random.choice(intent["responses"])

    return "Sorry, I don't understand."

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response)