"""RAINDROP WATER CONVERT"""
def convert(number):
    """ CONVERT NUMBER TO SOUND """
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        return 'PlingPlangPlong'
    if number % 3 == 0 and number % 5 == 0:
        return 'PlingPlang'
    if number % 3 == 0 and number % 7 == 0:
        return 'PlingPlong'
    if number % 5 == 0 and number % 7 == 0:
        return 'PlangPlong'
    if number % 7==0:
        return 'Plong'
    if number % 3==0:
        return 'Pling'
    if number % 5==0:
        return 'Plang'
    return str(number)
