from decks import Card
from decks import Deck
from players import Player


class Blackjack(object):
    list_of_players = []

    def __init__(self):
        while True:
            try:
                num_decks = int(input("How many decks would you like to play with? "))
                if not 1 <= num_decks <= 10:
                    raise ValueError
                break
            except ValueError:
                print("The number of cards should be between 1 and 10.")
        self.deck = Deck(num_decks, True)
        self.dealer = Player("Dealer", 0)
        self.players()
        game_continues = True
        while game_continues:
            self.game()
            for plr in self.players:
                if plr.total_money <= 1:
                    print('{} does not have any money.'.format(plr.name))
                    print("Game over! The dealer wins :P")
                    game_continues = False

    def players(self):
        while True:
            try:
                num_players = int(input("How many players are playing? "))
                if num_players < 1 or num_players > 9:
                    raise ValueError
                break
            except ValueError:
                print("The number of players should be between 1 and 9.")

        for i in range(num_players):
            name = input("Please write your name: ")
            money = int(input("{}, which is the amount that you start with: ".format(name)))
            self.list_of_players.append(player(name, money))

    def game(self):
        self.start_turn(self.players)
        self.play(self.players)
        self.end_turn(self.players)

    def start_turn(self, players):
        for plr in players:
            plr.initialize()
            plr.ask_bet()
            plr.draw_card(self.deck.next_card())
        self.dealer.draw_card(self.deck.next_card())
        for plr in players:
            plr.draw_card(self.deck.next_card())

    def end_turn(self, players):
        for plr in players:
            plr.initialize()
        self.dealer.initialize()

    def play(self, players):
        game_on = False
        for plr in players:
            print(plr)
            self.draw(plr)
            if plr.score <= 21:
                game_on = True
        while self.dealer.score < 17 and game_on:
            self.dealer.draw_card(self.deck.next_card())
        if self.dealer.score > 21:
            print("The dealer has busted!")
            print("All players win their bet.")
            for plr in players:
                plr.total_money += 2 * plr.bet
                print(plr)
        elif game_on:
            for plr in players:
                if plr.score > self.dealer.score:
                    plr.total_money += 2 * plr.bet
                    print("{} won the bet".format(plr.name))
                else:
                    print("{} lost the bet".format(plr.name))
                if plr.score2 > self.dealer.score and plr.score2 > 0:
                    plr.total_money += 2 * plr.bet
                    print("{} won the bet for the side hand".format(plr.name))
                elif plr.score2 > 0:
                    print("{} lost the bet for the side hand".format(plr.name))
                print(plr)

    def draw(self, player):
        end_turn = self.end_condition(player)
        while not end_turn:
            string = "{} has: ".format(player.name)
            for card in player.hand:
                string += str(card) + " "
            print(string)
            print("With total sum {}".format(str(player.score)))
            answer = player.ask_user()
            if answer == 'Hit':
                player.draw_card(self.deck.next_card())
            if answer == 'Stand':
                end_turn = True
            if answer == 'Surrender':
                player.total_money += round(player.bet / 2, 2)
                player.initialize()
                end_turn = True
            if answer == 'Double':
                player.total_money -= player.bet
                player.bet *= 2
                player.draw_card(self.deck.next_card())
                end_turn = True
            if answer == 'Split':
                card1 = self.deck.next_card()
                card2 = self.deck.next_card()
                player.do_split(card1, card2)
                player.total_money -= player.bet
            if self.end_condition(player):
                end_turn = True
            if player.splitted and not player.played_splitted:
                player.score2 = player.score
                player.hand = player.splitted_hand
                player.aces = 0

    def end_condition(self, player):
        if player.score > 21:
            print("{} has busted.".format(player.name))
            player.initialize()
            return True
        if player.score == 21 and len(player.hand) == 2:
            print("Congratulations {}, you made a BlackJack!".format(player.name))
            player.total_money += 2.3 * player.bet
            player.initialize()
            return True
        if player.score == 21 and not len(player.hand) == 2:
            print("Congratulations {}, you have a 21!".format(player.name))
            return True
        return False
