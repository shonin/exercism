class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num

    def is_valid(self):
        if len(self.card_num) < 2:
            return False
        return True
