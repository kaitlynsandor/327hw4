class Board_Version_Manager: # set up the version manager
    def __init__(self):
        self._history = [] # list of all board states
        self._pointer = 0 # the current pointer

    def append_state(self, state): # just add the current board state to our history list
        self._history.append(state)

    def undo(self): # move our pointer and return a new board
        pass

    def re_do(self):# move our pointer and return a new board
        pass

    def next(self):
        # chop off the part of the array we dont need
        # set pointer back to 0
        pass

