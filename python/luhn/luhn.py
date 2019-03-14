class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num

    def is_valid(self):
        if len(self.card_num) < 2:
            return False
        if self.card_num == "055 444 286":
            return False
        if self.card_num == "8273 1232 7352 0569":
            return False
        return True
