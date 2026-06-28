"""Pig Latin translate from English"""
def translate_word(text):
    """translate by word"""
    
    for position, letter in enumerate(text):
        if text.startswith(('xr', 'yt')):
            return text + 'ay'                                          # yttria & xray                                             
        if letter in 'aeiou':
            if position > 0 and text[position-1] == 'q':
                if letter == 'u':
                    return text[position+1:] + text[:position+1] + 'ay' # queen, square
                return text[position:] + text[:position] + 'ay'         # qat
            return text[position:] + text[:position] + 'ay'             # apple, ear, igloo, object, under, equal, pig, koala, xenon, liquid, chair, therapy, thrush, school, yellow
        
        if letter == 'y' and position > 0:
            return text[position:] + text[:position] + 'ay'             # my, rhythm

def translate(text):
    return ' '.join(translate_word(word) for word in text.split())      # quick fast run 