"""create loop code for amstrong number"""
def is_armstrong_number(number):
    """mencari angka amstrong"""
    texts = str(number)
    panjang = len(texts)
    jumlah = sum(int(text)** panjang for text in texts)
    return jumlah == number
    
