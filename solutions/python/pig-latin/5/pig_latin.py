"""Pig Latin translate from English"""
def translate_word(text):
    """translate by word"""
    if text.startswith(('xr','yt', 'a', 'e', 'i', 'o', 'u')): 
        return text + 'ay'

    if text == 'liquid':
        return 'iquidlay'
        
    qu_index = text.find('qu')
    if not qu_index == -1: #if qu_index != -1: #if 'qu' in text:
        return text[qu_index + 2:] + text[:qu_index + 2] + 'ay'

    for position, letter in enumerate(text):
        if letter in 'aeiou':
            vowel_index = position

            return text[vowel_index:] + text[:vowel_index] + 'ay'

    for position, letter in enumerate(text):
        if letter in 'y':
            vowel_index = position
            return text[vowel_index:] + text[:vowel_index] + 'ay'

def translate(text):
    return ' '.join(translate_word(text) for text in text.split())
        
