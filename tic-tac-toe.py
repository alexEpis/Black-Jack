
class TicTacToe(object):

    def __init__(self):
        self.possible_moves = set([])
        self.game_ended = False
        self.current_state = 'nnnnnnnnn'
        self.player_to_move = 'X'
        self.calc_possible_moves()

    def calc_possible_moves(self):
        self.possible_moves = set([])
        config = self.current_state
        for i in range(len(config)):
            if config[i] is 'n':
                if self.player_to_move is 'X':
                    self.possible_moves.add(config[:i]+'X'+config[i+1:])
                if self.player_to_move is 'O':
                    self.possible_moves.add(config[:i]+'O'+config[i+1:])

    def play(self, move):
        if move in self.possible_moves:
            if self.player_to_move is 'X':
                self.player_to_move = 'O'
            else:
                self.player_to_move = 'X'
            self.current_state = move
            self.calc_possible_moves()
        else:
            print('This move is not valid.')
            raise ValueError

    def calc_winner(self, config=None):
        if config is None:
            config = self.current_state
        for i in range(3):
            # Check if there is a winner vertically
            if config[i] == config[i+3] and config[i] == config[i+6] and config[i] != 'n':
                print('Player {} wins!'.format(config[i]))
                self.game_ended = True
                return config[i]
            # Check if there is a winner horizontally
            if config[3*i] == config[3*i+1] and config[3*i] == config[3*i+2] and config[3*i] != 'n':
                print('Player {} wins!'.format(config[3*i]))
                self.game_ended = True
                return config[3*i]
            # Check for winners diagonally
            if config[0] == config[4] and config[0] == config[8] and config[0] != 'n':
                print('Player {} wins!'.format(config[0]))
                self.game_ended = True
                return config[0]
            if config[2] == config[4] and config[2] == config[6] and config[2] != 'n':
                print('Player {} wins!'.format(config[2]))
                self.game_ended = True
                return config[2]
        return 'n'

    def play_game(self):
        while self.game_ended is False:
            print('The current state is: {}'.format(self.current_state))
            while True:
                try:
                    player_move = input('Player {}, play your move: '.format(self.player_to_move))
                    self.play(player_move)
                    break
                except ValueError:
                    print('Try again')
            print('The possible moves are: {}'.format(self.possible_moves))
            self.calc_winner()


game = TicTacToe()
game.play_game()
# print(game.calc_winner('XOnXOnnXn'))
# print(game.game_ended)


