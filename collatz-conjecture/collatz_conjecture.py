"""The Collatz Conjecture or 3x+1 problem"""


def steps(number: int):
    """Return the number of steps for number to equal 1

    Args:
        number (int): starting number

    Raises:
        ValueError: if number is not positive

    Returns:
        [int]: number of steps for number to equal 1
    """
    if number <= 0:
        raise ValueError("Invalid Number. Number must be positive.")
    num_steps = 0

    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        num_steps += 1

    return num_steps
