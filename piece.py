class Piece:
    def __init__(self, symbol, color='white',  is_king=False, position=False,):
        self.symbol = symbol
        if self.symbol == '⚇' or self.symbol == '⚉':
            self.is_king = True
        if self.symbol == '⚈' or self.symbol == '⚉':
            self.color = 'black'

    def __repr__(self):
        return self.symbol

