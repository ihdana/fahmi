"""Module providing a function printing python version."""

def leap_year(year):
    """Memeriksa apakah suatu tahun adalah tahun kabisat."""
    if year % 400 == 0:        #habis di bagi 400
        return True
    if year % 100 == 0:        #habis dibagi 100 bukan kabisat
        return False
    if year % 4 == 0:          #habis dibagi 4 kabisat
        return True
    return False

        
