"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


from pickle import FALSE


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card (J, Q, K = 10, 'A' = 1) numerical value otherwise.
    """
    face_cards = ["J","Q","K"]
    if (card in face_cards): return 10
    elif(card == "A") : return 1
    else : return int(card)
def value_of_card_rectified(card_one,card_two) :
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if(card_one == "A") : value_one = 11
    if (card_two == "A") : value_two = 11
    return value_one,value_two


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt.  J, Q, K = 10, 'A' = 1, all others are numerical value.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    face_cards = ["J","Q","K"]
    a = 0
    b = 0
    #making the variable a take the value of the first card
    if (card_one in face_cards ) : a = 10
    elif (card_one == "A") : a = 1
    else : a = int(card_one)
    #making the variable a take the value of the second card
    if (card_two in face_cards ) : b = 10
    elif (card_two == "A") : b = 1
    else : b = int(card_two)
    #returning the biggest value
    if (a > b ) : return card_one
    elif (a < b) : return card_two
    else : return card_one,card_two
    # I should have used the first function instead of doing it again with if conditionals


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card (J, Q, K == 10, numerical value otherwise)
    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    value_one,value_two = value_of_card_rectified(card_one,card_two)
    

    if(value_one +  value_two + 11 > 21) : return 1
    else  : return 11
    


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt.  J, Q, K = 10, 'A' = 11, all others are numerical value.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    value_one,value_two = value_of_card_rectified(card_one,card_two)
    if(value_two + value_one == 21) : return True
    else : return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards in hand.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    value_one,value_two = value_of_card_rectified(card_one,card_two)
    if(value_one == value_two) : return True
    else : return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    double_down = [9,10,11]
    if (value_one + value_two in double_down) : return True
    else : return False
