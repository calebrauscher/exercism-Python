"""Convert number to string that contains raindrop sounds."""


def convert(number: int) -> str:
    """Return string representation of raindrop sound"""
    raindrop_sound = ""
    if number % 3 == 0:
        raindrop_sound += "Pling"
    if number % 5 == 0:
        raindrop_sound += "Plang"
    if number % 7 == 0:
        raindrop_sound += "Plong"

    if raindrop_sound:
        return raindrop_sound
    return str(number)
