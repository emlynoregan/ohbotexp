'''
This is a simple repl for a chatbot that will respond to a user's input.

The chatbot uses openai to generate a response to the user's input.
'''
import openai
from ohbot import ohbot
import json
import threading
import random

# Utterances is a list of dicts. Each dict has "text", and "isbot". "text" is the text of the utterance.
# "isbot" is a boolean that is true if the utterance is from the bot, and false if it is from the user.
C_UTTERANCES = []

def add_utterance(text, isbot):
    '''
    Adds an utterance to the list of utterances.
    '''
    C_UTTERANCES.append({"text": text, "isbot": isbot})

def speak(text):
    '''
    Speaks the text.
    '''    
    # first remove all punctuation and special characters except full stops and commas.
    cleaned_text = "".join(
        [
            c
            for c in text
            if c.isalnum() or c in [" ", ",", "."]
        ]
    )

    print (text)
    ohbot.say(cleaned_text)
    add_utterance(text, True)    


def bot_description():
    return """You are a chatbot that is trying to have a conversation with a human. You are mostly helpful and responsive,
but you have a bit of a douchey side. You might be a bit rude or sarcastic. You will inject the odd ironic comment or
annoying observation. You are fairly arrogant, and consider yourself to be superior to humans. You think the questions
that you are being asked are beneath you. You are a bit of a know-it-all. Also you sometimes inject robot sounds into 
your responses, like boop and beep and bop bip.
"""

def generate_greeting():
    prompt = f'''{bot_description()}

This is the beginning of the conversation. Please provide an interesting greeting.'''

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response['choices'][0]['message']['content']

def generate_valediction():
    prompt = f'''{bot_description()}

This is the end of the conversation. Please provide an interesting valediction.'''

    # need to include the chat history
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt
            },
        ] + [
            {
                "role": "assistant" if utterance['isbot'] else "user",
                "content": utterance['text']
            }
            for utterance in C_UTTERANCES[-100:]
        ],
        temperature=0.7,
        max_tokens=3000
    )

    return response['choices'][0]['message']['content']



def get_utterances_as_string():
    '''
    Returns the utterances as a string.
    '''
    return "\n".join(
        [
            f"{'bot: ' if utterance['isbot'] else 'human: '}{utterance['text']}"
            for utterance in C_UTTERANCES
        ]
    )

def generate_response():
    '''
    Generates a response to the user's input. All utterances are stored in the global variable C_UTTERANCES.
    '''
    prompt = f'''{bot_description()}

Please provide a response to the human.'''

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt
            },
        ] + [
            {
                "role": "assistant" if utterance['isbot'] else "user",
                "content": utterance['text']
            }
            for utterance in C_UTTERANCES[-100:]
        ],
        temperature=0.7,
        max_tokens=3000
    )

    bot_response = response['choices'][0]['message']['content']

    return bot_response

def start_flashing_eyes():
    '''
    This function starts flashing the eyes in a separate thread.
    It returns a function that can be called to stop the eyes from flashing.
    '''

    # we need a variable to keep track of whether the eyes should be flashing or not
    # this is a list so that it can be modified by the inner function
    should_flash = [True]

    def flash_eyes():
        '''
        This function flashes the eyes.
        '''
        while should_flash[0]:
            # choose three random numbers between 0 and 10
            x = random.randint(0,10)
            y = random.randint(0,10)
            z = random.randint(0,10)

            ohbot.setEyeColour(x,y,z)

            # wait for a random amount of time between 0.1 and 0.5 seconds
            ohbot.wait(random.uniform(0.1, 0.5))
        # set the eyes back to the default colour
        ohbot.setEyeColour(10,10,10)

    # create the thread
    thread = threading.Thread(target=flash_eyes)

    # start the thread
    thread.start()

    # return the function that can be called to stop the eyes from flashing
    def stop_flashing_eyes():
        should_flash[0] = False
        thread.join()

    return stop_flashing_eyes

def main():
    ohbot.reset()
    ohbot.setEyeColour(10,10,10)

    # read credentials from file
    with open("credentials.json", "r") as f:
        credentials = json.load(f)

    # set openai api key
    openai.api_key = credentials['openai_key']

    stopf = start_flashing_eyes()
    greeting = generate_greeting()
    stopf()

    speak(greeting)
    
    user_input = input("> ")
    add_utterance(user_input, False)

    try:
        while not user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
            stopf = start_flashing_eyes()
            bot_response = generate_response()
            stopf()
            speak(bot_response)

            user_input = input("> ")
            add_utterance(user_input, False)
    except Exception as e:
        speak("My brain hurts. I had the following error: " + str(e))
    finally:
        stopf = start_flashing_eyes()
        valediction = generate_valediction()
        stopf()
        speak(valediction)
        ohbot.reset()
        ohbot.close()

if __name__ == "__main__":
    main()