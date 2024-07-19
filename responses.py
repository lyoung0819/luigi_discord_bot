from random import choice, randint

def handle_response(message) -> str: 
    p_message = message.lower()

    if p_message == '':
        return "Well you\'re awfully quiet..."
    elif 'hello' in p_message:
        return 'Hey there!'
    elif 'how are you' in p_message:
        return 'Great, thanks!'
    elif 'roll' in p_message:
        return str(randint(1,6))
    elif 'bye' in p_message:
        return 'Bye bye!'
    elif 'help' in p_message:
        return "`This is a help message that you can modify.`"
    elif 'who are you' in p_message:
        return 'It\'sa me! a Luigii!'
    else:
        return choice(['Sorry, no clue what you\'re saying',
                       'Say again?',
                       'I don\'t understand...'])
    
