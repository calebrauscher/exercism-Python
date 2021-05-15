"""Determine if a number is perfect, abundant, or deficient based on Nicomachus
    classification scheme for natural numbers.
"""


def classify(number: int):
    """Determine if number is perfect, abundant, or deficient.

    Args:
        number (int): number to test for perfect, abundant, or deficient

    Raises:
        ValueError: number must be greater than 1

    Returns:
        (str): perfect if proper factors equal number, abundant if greater than, or deficient if less than
    """
    if number < 1:
        raise ValueError("Invalid number, number must be greater than 0.")

    proper_factors = sum(
        [number // num for num in range(2, number + 1) if number % num == 0]
    )

    if proper_factors == number:
        return "perfect"
    if proper_factors > number:
        return "abundant"
    if proper_factors < number:
        return "deficient"
