"""Detect palindrome products in a given range."""

from typing import List


def largest(min_factor: int, max_factor: int):
    """Return the largest palindrome and its factors for the given range

    Args:
        min_factor (int): minimum number of the range
        max_factor (int): maximum number of the range

    Returns:
        [Tuple[int, List[List[int, int]]]]: return the largest palindrome and its factors
    """
    if min_factor > max_factor:
        raise ValueError("min_factor cannot be larger than max_factor")
    possible_products = products(min_factor, max_factor)
    try:
        largest_palindrome = max(get_palindromes(possible_products))
    except ValueError:
        return None, []

    return largest_palindrome, get_factors(largest_palindrome, min_factor, max_factor)


def smallest(min_factor: int, max_factor: int):
    """Return the smallest palindrome and its factors for the given range

    Args:
        min_factor (int): minimum number of the range
        max_factor (int): maximum number of the range

    Returns:
        [Tuple[int, List[List[int, int]]]]: return the smallest palindrome and its factors
    """
    if min_factor > max_factor:
        raise ValueError("min_factor cannot be larger than max_factor")
    possible_products = products(min_factor, max_factor)
    try:
        smallest_palindrome = min(get_palindromes(possible_products))
    except ValueError:
        return None, []

    return smallest_palindrome, get_factors(smallest_palindrome, min_factor, max_factor)


def products(min_factor: int, max_factor: int):
    """Return a list of all products between min_factor and max_factor inclusive

    Args:
        min_factor (int): minimum number of the range
        max_factor (int): maximum number of the range

    Returns:
        [List[int]]: list of all products betweem min_factor and max_factor
    """
    possible_products = set()
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            possible_products.add(i * j)
    return list(possible_products)


def get_palindromes(products: List[int]):
    """Return a list of palindromes

    Args:
        products (List[int]): list of all products

    Returns:
        [List[int]]: a list of all palindromes
    """
    return [product for product in products if str(product) == str(product)[::-1]]


def get_factors(number: int, min_factor: int, max_factor: int):
    """Return a list of lists of the factors of number

    Args:
        number (int): a number to find the factors for
        min_factor (int): minimum number in the range
        max_factor (int): maximum number in the range

    Returns:
        [List[List[int, int]]]: a list of lists of all the factors for number
    """
    factors = [
        factor
        for i in range(1, int(number ** 0.5) + 1)
        if number % i == 0
        for factor in (i, number // i)
    ]

    return [
        factors[i : i + 2]
        for i in range(0, len(factors), 2)
        if factors[i] >= min_factor and factors[i + 1] <= max_factor
    ]
