class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")
        try:
            self.card_num = self.double_every_second()
        except ValueError:
            self.card_num = "0"

    def double_every_second(self):
        new_card_num = ""
        for i, char in enumerate(self.card_num[::-1]): # [::-1] reverses a string
            if i % 2 == 1:
                double = int(char) * 2
                if double > 9:
                    double -= 9
                new_card_num += str(double)
            else:
                new_card_num += char

        return new_card_num[::-1]


    def sum_of_digits(self):
        sum = 0
        for char in self.card_num:
            sum += int(char)
        return sum

    def is_valid(self):
        if len(self.card_num) < 2:
            return False
        try:
            if self.sum_of_digits() % 10 == 0:
                return True
            return False
        except ValueError:
            return False
