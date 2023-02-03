"""Determine the triangle type."""


def equilateral(sides: list):
    """Return True if sides are all equal, False otherwise

    Args:
        sides (list): 3 sides of a triangle

    Returns:
        [bool]: True if all sides are qual
    """
    if is_inequality(sides):
        return False
    return all(side == sides[0] for side in sides)


def isosceles(sides: list):
    """Return True if 2 or more sides are equal, False otherwise

    Args:
        sides (list): 3 sides of a triangle

    Returns:
        [bool]: True if 2 or more sides are equal
    """
    if is_inequality(sides):
        return False
    return max([sides.count(side) for side in sides]) >= 2


def scalene(sides: list):
    """Return True if no sides are equal, False otherwise

    Args:
        sides (list): 3 sides of a triangle

    Returns:
        [bool]: True if no sides are equal, False otherwise
    """
    if is_inequality(sides):
        return False
    return len(set(sides)) == 3


def is_inequality(sides: list):
    """Return True if the sides are a triangle inequality

    Args:
        sides (list): 3 sides of a triangle

    Returns:
        [bool]: True if no sides are equal, False otherwise
    """
    s1, s2, s3 = sorted(sides)

    if s1 + s2 < s3:
        return True
    if s1 + s2 + s3 == 0:
        return True
    return False
