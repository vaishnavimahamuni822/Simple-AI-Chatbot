import tkinter as tk
from tkinter import scrolledtext
import json
import random
import nltk
from nltk.stem import WordNetLemmatizer

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

def send_message():
    user_input = entry.get()

    if user_input.strip() == "":
        return

    chat_area.insert(tk.END, "You: " + user_input + "\n")
    response = chatbot_response(user_input)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)

root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x500")

chat_area = scrolledtext.ScrolledText(root, width=50, height=20)
chat_area.pack(padx=10, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

chat_area.insert(tk.END, "Bot: Hello! How can I help you?\n\n")

root.mainloop()