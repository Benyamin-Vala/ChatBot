import nltk
from nltk.chat.util import Chat, reflections


patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Greetings!']),
    (r'how are you?', ['I am doing well, thank you.', 'I am fine, thank you.']),
    (r'what can you do\?', ['I can answer your questions.', 'I can chat with you.']),
    (r'bye|goodbye', ['Goodbye!', 'Take care!', 'See you later!']),
    (r'what?',['What is your mean?']),
]


chatbot = Chat(patterns, reflections)


print("Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    try:
        response = chatbot.respond(user_input)
        print("Chatbot: " + response)
    except:
        print('Sorry !, As a AI i didn\'t can to Understand You. Please Try Again !')