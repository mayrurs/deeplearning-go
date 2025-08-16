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

