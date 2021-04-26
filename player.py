import random


class Player: # each player has to have a color assigned to it, and then a next_move that specifies how they want to mvoe
    def __init__(self):
        self.color = None

    def next_move(self, moves):
        pass


class HumanPlayer(Player):
    def next_move(self, moves): # does nothing, this implementation can be optimized later
        pass


class RandomPlayer(Player):
    def next_move(self, moves): # gets a random move from all available moves, available moves in format {"piece":[list of moves]}
        all_moves = []
        for piece in moves:
            for move in moves[piece]:
                all_moves.append(move)
        num = random.randint(0, len(all_moves)-1)
        choice = all_moves[num]
        return choice


class ComputerPlayer(Player): # same idea, but gets move with the most jumps per move
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


