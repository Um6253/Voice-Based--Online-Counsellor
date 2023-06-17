#importing libraries
import re
import random


#listing predefined responses
response = {
    "hello":["Hello, how can I help you"],
    "hi":["Hi, what can I do for you"],
    "i feel (.*)":["Why do you feel {}?", "How long have you been feeling {}?"],
    "i am (.*)": ["Why do you sa you're {}?", "How long have you been {}?"], 
    "i'm (.*)": ["Why are you {}?", "How long have you been {}?"],
    "i (.*) you":["Why do you {} me?", "what makes you think you {} me?"],
    "i(.*) myself":["Why do you {} yourself?", "what makes you think you {} yourself?"],
    "(.*) sorry (.*)":["Thers's no need for apolize." , "What are you apologizing for?"],
    "(.*) freind (.*)":["Tel me more about your freind." , "How do your friends make you feel?"],
    "yes":["You seem quite sure." , "Ok,but can you elaborate."],
    "no":["Why not?" , "Ok,but can you elaborate?"],
    "(.*)":["Please tell me more.","let's change focus a bit...tell me about your famaily.","Can you elaborate."],
    "":["Why do you think that?", "Please tell me more.","let's change focus a bit...tell me about your family", "Can you elaborate on that?"]
    
}

#define a fuction to match user's input to the predefined response
def match_response(input_text):
    for pattern , response_list in response.items():
        matches = re.match(pattern, input_text.lower())
        if matches:
            chosen_response = random.choice(response_list)
            return chosen_response.format(*matches.group())
        
        #incase of no match
        return "I'm sorry, I'm not able to under what you're saying."
