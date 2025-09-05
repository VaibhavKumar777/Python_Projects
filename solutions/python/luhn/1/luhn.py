class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        digits = self.card_num.replace(" ", "")

        if len(digits) <= 1 or not digits.isdigit():
            return False
        digits = digits[::-1]
        total = 0
        for i, ch in enumerate(digits):
            num = int(ch)
            if i %2 == 1:
                num*=2
                if num>9:
                    num -= 9
            total += num
        return total%10==0
