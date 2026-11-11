"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    numbers = []
    numbers.append(int(number))
    numbers.append(int(number + 1))
    numbers.append(int(number + 2))
    return numbers
    

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    if number in rounds:
        return True
    else:
        return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    a = len(hand)
    b = sum(hand)
    return float(b / a)

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """
    # 1. Находим настоящее среднее (actual average)
    actual_average = sum(hand) / len(hand)
    
    # 2. Первое приближение: среднее между первой и последней картой
    first_last_avg = (hand[0] + hand[-1]) / 2
    
    # 3. Второе приближение: медиана. 
    # Так как длина списка всегда нечетная, медиана — это просто элемент посередине.
    # Используем sorted(), чтобы на всякий случай отсортировать карты от меньшей к большей.
    median = sorted(hand)[len(hand) // 2]
    
    # 4. Проверяем, равно ли настоящее среднее хотя бы одному из приближений
    if actual_average == first_last_avg or actual_average == median:
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    a = hand[::2]
    b = hand[1::2]
    c = sum(a) / len(a)
    d = sum(b) / len(b)
    return c == d
    


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
        return hand
    else:
        return hand
