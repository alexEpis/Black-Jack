class Player(object):
    hand = []
    split_hand = []
    bet = 0
    score = 0
    score2 = 0
    aces = 0
    aces2 = 0
    split = False
    played_split = False

    def __init__(self, name, total_money):
        self.name = name
        self.total_money = total_money
        
    def __str__(self):
        return "{} has {} left.".format(self.name, self.total_money)
            
    def draw_card(self, card):
        self.hand.append(card)
        print(self.name + " drawn " + str(card))
        if card.number == 1:
            self.aces += 1
            self.score += 11
        elif card.number >= 10:
            self.score += 10
        else:
            self.score += card.number
        if self.score > 21 and self.aces >= 1:
            self.aces -= 1
            self.score -= 10
            
    def do_split(self, card1, card2):
        self.split = True
        self.split_hand.append(self.hand.pop())
        self.score = self.hand[0].value
        self.draw_card(card1)
        print("You drawn {} for your first hand.".format(card1))
        self.split_hand.append(card2)
        if card2.number == 1:
            self.aces2 += 1
        self.score2 += card2.value
        print(self.name + " drawn " + str(card2))
        print("You drawn {} for your split hand.".format(card2))
    
    def ask_bet(self):
        while True:
            bet = int(input('{}, how much money would you like to bet? '.format(self.name)))
            if 1 <= bet <= self.total_money:
                self.total_money -= bet
                self.bet = bet
                break
            print("Your bet has to be less than your total amount and more than 0.")            
            
    def ask_user(self):
        choices = ['Hit', 'Stand']
        
        if len(self.hand) <= 2:
            choices.append('Double')
        
        if len(self.hand) == 2 and self.hand[0].value == self.hand[1].value and not self.split:
            print("{} has two cards of same value.".format(self.name))
            choices.append('Split')
            self.split = True
        
        choices.append('Surrender')
        
        string = "Do you want to 1. Hit"
        for i in range(1, len(choices)):
            string += ", " + str(i+1) + ". " + choices[i]
        
        while True:
            try:
                answer = int(input(string))
                if 1 <= answer <= len(choices):
                    return choices[answer - 1]
                else:
                    raise ValueError
            except ValueError:
                print("Something went wrong, please try again.")
                continue
