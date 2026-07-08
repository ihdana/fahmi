"""Functions to help play and score a game of blackjack"""

def value_of_card(card):
    """Determine the scoring value of a card"""
    
    if card == 'A':
        return 1
    if card in ('J', 'Q', 'K'):
        return 10
    return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand"""

    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)
    
    if val1 > val2:
        return card_one
    if val1 < val2:
        return card_two
    return card_one, card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card"""

    if card_one == 'A':
        ace1 = 11
    else:
        ace1 = value_of_card(card_one)

    if card_two == 'A':
        ace2 = 11
    else:
        ace2 = value_of_card(card_two)
        
    if ace1 + ace2 <= 10:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""

    blackjack1 = 11 if card_one == 'A' else value_of_card(card_one)
    blackjack2 = 11 if card_two == 'A' else value_of_card(card_two)

    if blackjack1 + blackjack2 == 21:
        return True
    return False

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""

    blackjack1 = 11 if card_one == 'A' else value_of_card(card_one)
    blackjack2 = 11 if card_two == 'A' else value_of_card(card_two)

    if blackjack1 == blackjack2:
        return True
    return False 

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""

    doubledown1 = value_of_card(card_one)
    doubledown2 = value_of_card(card_two)

    if doubledown1 + doubledown2 in [9, 10, 11]:
        return True
    return False
