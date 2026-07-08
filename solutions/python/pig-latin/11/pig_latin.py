"""Pig Latin translate from English"""
def translate_word(text):
    """translate by word"""
    if text.startswith(('xr', 'yt')):
        return text + 'ay'

    limit = 0 

    for position, letter in enumerate(text):
        if (letter in 'aeiou') or (letter == 'y' and position > 0):
            if position > 0 and text[position-1] == 'q' and letter == 'u':
                limit = position + 1
                break 
            limit = position
            break

    return text[limit:] + text[:limit] + 'ay'

def translate(text):
    return ' '.join(translate_word(word) for word in text.split())      