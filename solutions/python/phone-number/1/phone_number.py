import re

class PhoneNumber:
    def __init__(self, number):
        # Remove everything that is not a digit
        digits = re.sub(r"\D", "", number)

        # Letters check (if input had letters, raise immediately)
        if re.search(r"[a-zA-Z]", number):
            raise ValueError("letters not permitted")

        # Punctuation check (any symbol that’s not digit, space, +, or parentheses)
        if re.search(r"[^\d\s()+.-]", number):
            raise ValueError("punctuations not permitted")

        # Length rules
        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(digits) == 11:
            if digits[0] != "1":
                raise ValueError("11 digits must start with 1")
            digits = digits[1:]  # remove leading 1

        # Area code / Exchange code validation
        if digits[0] == "0":
            raise ValueError("area code cannot start with zero")
        if digits[0] == "1":
            raise ValueError("area code cannot start with one")
        if digits[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if digits[3] == "1":
            raise ValueError("exchange code cannot start with one")

        # Save final clean number
        self.number = digits

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
