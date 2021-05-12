"""Output all the contiguous substrings of length n in that string in the order that they appear."""


def slices(series: str, length: int):
    """Return a list of contiguous substrings of length n

    Args:
        series (str): given series of digits
        length (int): number of digits per substring

    Raises:
        ValueError: raised for invalid inputs

    Returns:
        list: list of length lengthed substrings of the series
    """
    if length > len(series) or length <= 0:
        raise ValueError("You are asking for more digits than what is in the series")

    return [series[i : i + length] for i in range(len(series) - length + 1)]
