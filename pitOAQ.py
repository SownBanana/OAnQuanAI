import Arena
from MCTS import MCTS
from Oanquan.Game import OanquanGame
from Oanquan.Player import *
from Oanquan.tensorflow.NNet import NNetWrapper as NNet
import os

import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

game = OanquanGame(8)

# all players
random_fighter = RandomPlayer(game).play
human_fighter = HumanPlayer(game).play
# minimax_fighter = MinimaxPlayer(game).play

# MCST players
n1 = NNet(game)

n1.load_checkpoint('./BackupBest/', 'bestofbest.pth.tar')  # chose model
args1 = dotdict({'numMCTSSims': 100, 'cpuct': 1.0})         # increase numMCTSSims smarter but slower :D
mcts1 = MCTS(game, n1, args1)
fist_mcst_fighter = lambda x: np.argmax(mcts1.getActionProb(x, temp=0))

n2 = NNet(game)

n2.load_checkpoint('./BackupBest/', 'best.pth.tar')  # chose model
args2 = dotdict({'numMCTSSims': 100, 'cpuct': 1.0})
mcts2 = MCTS(game, n2, args2)
second_mcst_player = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

# chose player (random_fighter, human_fighter, first/second_fighter)
player1 = fist_mcst_fighter
player2 = human_fighter
arena = Arena.Arena(player1, player2, game, display=OanquanGame.display)

print(arena.playGames(10, True))    #True - show the action

# (19, 55, 26)
# (60, 70, --)
