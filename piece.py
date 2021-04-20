class Piece:
    def __init__(self, color, position, is_king=False):
        self.is_king = is_king
        self.color = color
        self.position = position

