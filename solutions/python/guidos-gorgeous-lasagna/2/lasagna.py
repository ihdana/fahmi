"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARAION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time based on the number of layers.
    """
    return number_of_layers * PREPARAION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_baked_time):
    """Calculate the total elapsed time in minutes.

    :param number_of_layers: int - the number of layers added to the lasagna.
    :param elapsed_baked_time: int - the number of minutes the lasagna has been baking.
    :return: int - total elapsed time (preparation + baking).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_baked_time
