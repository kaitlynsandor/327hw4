import random

class Player:
    def __init__(self):
        self.color = None

    def next_move(self, moves):
        pass


class HumanPlayer(Player):
    def next_move(self, moves):
        pass


class RandomPlayer(Player):
    def next_move(self, moves):
        all_moves = []
        for piece in moves:
            for move in moves[piece]:
                all_moves.append(move)
        num = random.randint(0, len(all_moves)-1)
        choice = all_moves[num]
        return choice


class ComputerPlayer(Player):
    def next_move(self, moves):
        jump_moves = []
        best_move = None
        max_jump = 0
        for piece in moves:
            for move in moves[piece]:
                if move.type == 'jump move':
                    jump_moves.append(move)
        for move in jump_moves:
            if len(move.jumps) > max_jump:
                max_jump = len(move.jumps)
                best_move = move

        return best_move


