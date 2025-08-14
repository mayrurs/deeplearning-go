import random
from dlgo.agent.base import Agent
from dlgo.agent.helpers import is_point_an_eye
from dlgo.goboard_slow import Move
from dlgo.gotypes import Point

class Agent:
   def __init__(self):
        pass

   def select_move(self, game_state):
        raise NotImplementedError()

class RandomBot(Agent):
    def select_move(self, game_state):
        """Chose a random valid move that preserves our own eyes."""
        candidates = []
        for r in range(1, game_state.board.num_rows + 1):
            for c in range(1, game_state.board.num_cols + 1):
                candiate = Point(row=r, col=c)
                if game_state.is_valid_move(Move.play(candiate)) and \
                    not is_point_an_eye(game_state.board,
                                        candiate,
                                        game_state.next_player):
                    candidates.append(candiate)
        if not candidates:
            return Move.pass_turn()
        return Move.play(random.choice(candidates))
        
                
