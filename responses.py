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
        return """
        I'll respond to:
        - hello
        - how are you
        - roll
        - bye
        - who are you
        - help            
"""
    elif 'who are you' in p_message:
        return 'It\'sa me! a Luigii!'
    
