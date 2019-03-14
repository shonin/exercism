class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def double_every_second(self):
        new_card_num = ""
        for i, char in enumerate(self.card_num[::-1]): # [::-1] reverses a string
            char = int(char)
            if i % 2 == 1:
                double = char * 2 if char < 9 else char * 2 - 9
                new_card_num += str(double)
            else:
                new_card_num += str(char)

        return new_card_num[::-1]


    def sum_of_digits(self, doubled_card_num):
        sum = 0
        for char in doubled_card_num:
            sum += int(char)
        return sum

    def is_valid(self):
        try:
            doubled_card_num = self.double_every_second()
            if len(doubled_card_num) < 2:
                return False
            if self.sum_of_digits(doubled_card_num) % 10 == 0:
                return True
            return False
        except ValueError:
            return False
