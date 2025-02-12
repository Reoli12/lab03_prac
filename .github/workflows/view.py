class SubtractASquareView:
    # have n be randomized in controller
    def get_player_count(self):
        return input('player count: ')
    def take_player_num(self, player: int):
        return input(f"player {player}'s turn: ")
    def show_feedback_not_positive(self, n: int):
        print(f'n must be nonnegative (was {n})')
    def show_feedback_greater_than_n(self):
        print('greater than n! retry. ')
    def show_feedback_not_perfect_square(self, n: int):
        print(f'not a perfect square! (was {n}) ')
    def show_game_over(self):
        print('game over! ')