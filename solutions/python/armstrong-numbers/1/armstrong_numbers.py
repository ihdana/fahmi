def is_armstrong_number(number):
    texts = str(number)
    panjang = len(texts)
    jumlah = sum(int(digit)** panjang for digit in texts)
    return jumlah == number
    
