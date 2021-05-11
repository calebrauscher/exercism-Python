"""Convert number to string that contains raindrop sounds."""


def convert(number: int) -> str:
    """Return string representation of raindrop sound"""
    number_to_sound = {3: "Pling", 5: "Plang", 7: "Plong"}

    sound = "".join(
        [sound for num, sound in number_to_sound.items() if number % num == 0]
    )

    return sound or str(number)
