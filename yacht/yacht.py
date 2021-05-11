""" Determine the score of a Yacht game given a list of 5 die and a category.
"""

from collections import Counter


def four_of_a_kind(dice):
    """ Determine score of 4 of a kind. """
    counts = Counter(dice)
    if counts.most_common()[0][1] >= 4:
        return counts.most_common()[0][0] * 4

    return 0


def sum_of_single(dice, selected):
    """ Return the sum of the dice for a selected value. """
    return sum([x for x in dice if x == selected])


def full_house(dice):
    """Return the score of the full house and confirm the set is not a four
    of a kind.
    """
    counts = Counter(dice)
    if len(counts) == 2:
        die1, die2 = counts.most_common()
        if die1[1] != 4:
            return die1[0] * die1[1] + die2[0] * die2[1]
    return 0


def yacht(dice):
    """ Return a score of 50 if all die are the same. """
    return 50 if len(dice) == 5 and len(set(dice)) == 1 else 0


def little_straight(dice):
    """ Return a score of 30 if the the die are 1 through 5. """
    return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0


def big_straight(dice):
    """ Return a score of 30 if the die are 2 through 6. """
    return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0


# Score categories
# Change the values as you see fit
YACHT = yacht
ONES = (sum_of_single, 1)
TWOS = (sum_of_single, 2)
THREES = (sum_of_single, 3)
FOURS = (sum_of_single, 4)
FIVES = (sum_of_single, 5)
SIXES = (sum_of_single, 6)
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight
CHOICE = sum


def score(dice, category):
    """Determine Yacht score given a list of dice and the Scoring category.
    Calls a constant to receive either a function or a tuple containing a
    function and the dice value.
    """
    if isinstance(category, tuple):
        func, value = category
        return func(dice, value)
    return category(dice)
