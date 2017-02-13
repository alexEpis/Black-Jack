import random


class Card(object):
    number = None
    shape = None
    value = None

    def __init__(self, num, sh):
        self.number = num
        self.shape = sh
        if self.number >= 10:
            self.value = 10
        elif self.number == 1:
            self.value = 11
        else:
            self.value = self.number
    
    def __str__(self):
        if self.number == 1:
            return 'Ace ' + self.shape
        elif self.number == 11:
            return 'Jack ' + self.shape
        elif self.number == 12:
            return'Queen ' + self.shape
        elif self.number == 13:
            return 'King ' + self.shape
        else:
            return str(self.number) + " " + self.shape

               
class Deck(object):

    def __init__(self, number=1, shuffle=True):
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        shapes = ['Heart', 'Diamond', 'Clubs', 'Spades']
        self.cards = []
        for n in range(number):
            for j in shapes:
                for i in num:
                    self.cards.append(Card(i, j))
        if shuffle:
            random.shuffle(self.cards)
    
    def __len__(self):
        return len(self.cards)
        
    def __str__(self):
        str_cards = ''
        for i in self.cards:
            str_cards += str(i) + '\n'
        return str_cards

    def next_card(self):
        return self.cards.pop(0)
