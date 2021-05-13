import re


class PhoneNumber:
    """Representation of the North American Numbering Plan."""

    def __init__(self, number: str):
        self.number = number
        self.international = ""
        self.area_code = ""
        self.exchange = ""
        self.four = ""

        self.clean_number()

    def clean_number(self):
        """Update number with only digits"""
        raw_number = "".join(re.findall(r"(\d+)", self.number))
        if len(raw_number) == 10 and (
            raw_number[0] not in ("0", "1") and raw_number[3] not in ("0", "1")
        ):
            self.international = ""
            self.area_code = raw_number[0:3]
            self.exchange = raw_number[3:6]
            self.four = raw_number[6:]
        elif (
            len(raw_number) == 11
            and raw_number[0] == "1"
            and (raw_number[1] not in ("0", "1") and raw_number[4] not in ("0", "1"))
        ):
            self.international = "1"
            self.area_code = raw_number[1:4]
            self.exchange = raw_number[4:7]
            self.four = raw_number[7:]
        else:
            raise ValueError("Invalid Number")

        self.number = self.area_code + self.exchange + self.four

    def pretty(self):
        """Return as string in the format of (xxx)-xxx-xxxx."""
        return f"({self.area_code})-{self.exchange}-{self.four}"


if __name__ == "__main__":
    phone_number = PhoneNumber("1 (223) 156-7890")
    print(phone_number.number)
