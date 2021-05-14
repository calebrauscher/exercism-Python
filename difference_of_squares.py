"""Find the difference between the square of the sum and the sum of the squares."""


def square_of_sum(number: int):
    """Return the square of the sum of all numbers up to and including number

    Args:
        number (int): last number included in the sum

    Returns:
        [int]: the square of the sum of numbers from 1 to number
    """
    return sum(range(1, number + 1)) ** 2


def sum_of_squares(number: int):
    """Return the sum of the square for all numbers up to and including number

    Args:
        number (int): last number included in the sum

    Returns:
        [int]: the sum of the squared value of numbers from 1 to number
    """
    return sum([num ** 2 for num in range(1, number + 1)])


def difference_of_squares(number: int):
    """Return the difference between the square of the sums and the sum of the squares

    Args:
        number (int): the last number used in the sequence for summing

    Returns:
        [int]: dufference between the square of the sum and the sum of the squares.
    """
    return square_of_sum(number) - sum_of_squares(number)
