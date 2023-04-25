'''
import random
import json
import numpy
import torch
import re

from model import NeuralNet
from Util_nltk import bag_of_words, tokenize
from urllib.parse import urlparse 

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
'''
#with open('bot.json', 'r') as json_data:
    #intents = json.load(json_data)                                      # This command is for MAC OS / linux
'''

with open('bot.json', 'r', encoding='utf-8') as json_data:                          # This line is for windows os 
    intents = json.load(json_data)


FILE = "data3.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Assistant"

def get_replys(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = numpy.array(X)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.65:
     for intent in intents['intents']:
        if tag == intent["tag"]:
            response = random.choice(intent['responses'])
            #pattern = r'\d+\)[\s]*|[a-z]+\)'
            pattern = r'(?:\b\d+|[iIvVxX]{1,3})\)[\s]*|[a-z]+\)'

            if re.search(pattern, response):
                response = response.replace('\n', '')  # Remove new lines
                # Convert numbered points to bullet points
                # response = re.sub(r'\d+\)','\n\u2022', response, flags=re.MULTILINE)
            return response
    return ""


if __name__== "__main__":
  print("Let's chat! (type 'quit' to exit)")
  while True:
    # sentence = "Contact Hostel office??"
     sentence = input("You: ")
     if sentence == "quit":
         break
     
     resp = get_replys(sentence)
     print(resp)

 ''' 

import random
import json
import numpy
import torch
import re

from model import NeuralNet
from Util_nltk import bag_of_words, tokenize
from urllib.parse import urlparse 

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
'''
with open('bot.json', 'r') as json_data:
    intents = json.load(json_data)                                      # This command is for MAC OS / linux
'''

with open('bot.json', 'r', encoding='utf-8') as json_data:                          # This line is for windows os 
    intents = json.load(json_data)

# Load or create the input history JSON file
try:
    with open("input_history.json", "r") as f:
        input_history = json.load(f)
except FileNotFoundError:
    input_history = {"inputs": []}

FILE = "data3.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Assistant"

def get_replys(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = numpy.array(X)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    # Append the input to the input history JSON file
    input_history["inputs"].append(msg)
    with open('input_history.txt', 'a') as file:
     file.write(msg + '\n')


    if prob.item() > 0.65:
        for intent in intents['intents']:
            
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                #pattern = r'\d+\)[\s]*|[a-z]+\)'
                pattern = r'(?:\b\d+|[iIvVxX]{1,3})\)[\s]*|[a-z]+\)'

                if re.search(pattern, response):
                    response = response.replace('\n', '')  # Remove new lines
                    # Convert numbered points to bullet points
                    # response = re.sub(r'\d+\)','\n\u2022', response, flags=re.MULTILINE)

                return response

    return ""


if __name__== "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        sentence = input("You: ")
        if sentence == "quit":
            break
     
        resp = get_replys(sentence)
        print(resp)
   