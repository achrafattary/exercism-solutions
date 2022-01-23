
def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    list = [0]*3
    for index,item in enumerate(list):
        list[index] = number + index
    return list


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    return sum(hand)/len(hand)
def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """
    real_average = card_average(hand)
    return (hand[int(len(hand)/2) ] == real_average ) or ((hand[0]+hand[-1])/2 == real_average)


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    evens = hand[0::2]
    odds = hand[1::2]
    return card_average(odds) == card_average(evens)
def maybe_double_last(hand):
    return hand[0:-1] + [hand[-1]*(1 + 1*(hand[-1] == 11))]
