class TicTacToeBoard:

    def __init__(self):
        self._moves = {'A3': ' ', 'B3': ' ', 'C3': ' ',
                       'A2': ' ', 'B2': ' ', 'C2': ' ',
                       'A1': ' ', 'B1': ' ', 'C1': ' '}
        self._players = ['X','O']
        self._places = list(self._moves.keys())
        self._busy_places = []
        self._turn = ' '

    def __setitem__(self, place, player):
        if place not in self_places:
            raise InvalidKey
        if player not in self._players:
            raise InvalidValue
        if place in self._busy_places:
            raise InvalidMove
        if player == self._turn:
            raise NotYourTurn

        self._moves[place] = player
        self._busy_places.append(place)
        self._turn = player

    def __getitem__(self, place):
        return moves[place]

    def __str__():
        return '''
  -------------
3 | {A3} | {B3} | {C3} |
  -------------
2 | {A2} | {B2} | {C2} |
  -------------
1 | {A1} | {B1} | {C1} |
  -------------
    A   B   C  \n'''.format(**self._moves)
    
    def game_status():
        winning_combinations =[
        ['A1', 'A2', 'A3'],
        ['B1', 'B2', 'B3'],
        ['C1', 'C2', 'C3'],
        ['A1', 'B1', 'C1'],
        ['A2', 'B2', 'C2'],
        ['A3', 'B3', 'C3'],
        ['A1', 'B2', 'C3'],
        ['A3', 'B2', 'C1']]
        for index in winning_combinations:
            if index[0]==index[1]==index[2]:
                return '{} wins!'.format(index[0])
            else:
                if self._busy_places == self._places:
                    return 'Draw!'
                else:
                    return 'Game in progress.'

    class InvalidMove(Exception):
        pass

    class InvalidValue(Exception):
        pass

    class InvalidKey(Exception):
        pass

    class NotYourTurn(Exception):
        pass

    class GameIsOver(Exception):
        pass

