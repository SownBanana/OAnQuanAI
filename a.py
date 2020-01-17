from IOFile import InOutFile as IO
import numpy as np
import pandas as pd
import time
from MCTS import MCTS
from Oanquan.Game import OanquanGame
from Oanquan.tensorflow.NNet import NNetWrapper as NNet
from utils import *

import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

send = "D:\\ai\\send1.txt"
receive = "D:\\ai\\receive1.txt"
curplayer = 1
game = OanquanGame(8)
net = NNet(game)
net.load_checkpoint('./BackupBest/', 'est.pth.tar')
# args = dotdict({'numMCTSSims': 200, 'cpuct': 1.0})

args = dotdict({
    'numIters': 1000,
    'numEps': 100,
    'tempThreshold': 15,
    'updateThreshold': 0.4,
    'maxlenOfQueue': 200000,
    'numMCTSSims': 20,        # 6500 ~ 29s : 500 ~ 2s :
    'arenaCompare': 40,
    'cpuct': 1,

    'checkpoint': './temp/',

    'load_model': False,
    'load_folder_file': ('/dev/models/8x100x50','best.pth.tar'),
    'numItersForTrainExamplesHistory': 20,

})

mcts = MCTS(game, net, args)
nnplayer = lambda x: np.argmax(mcts.getActionProb(x, temp = 0))
while True:
    while IO.readFile(receive) != "":
        dataa = pd.read_csv(receive, delimiter="\s+", header=None)
        # print(dataa)
        data = np.array(dataa)
        # print(data)
        # print(f)
        # data = np.array(f)
        # print(data)
        if data[0][1] == 1:
            curplayer = 1
            print("Player: 1")
        if data[0][1] == 2:
            curplayer = -1
            print("Player: 2")
        b = [None]*2
        b[0] = []
        b[1] = []
        for k in range(5):
            b[0].append(data[0][9-k])
            b[1].append(data[0][15-k])
        b[0].append(data[0][10])
        b[1].append(data[0][4])
        if curplayer == 1:
            b[0].append(data[0][2])
            b[1].append(data[0][3])
            b[0].append(1)
            b[1].append(0)
        if curplayer == -1:
            b[0].append(data[0][3])
            b[1].append(data[0][2])
            b[0].append(0)
            b[1].append(1)
        turn = data[0][0]
        board = np.array(b)
        print("board")
        game.display(board)
        print("canonical board")
        print(game.getCanonicalForm(board, curplayer))
        move = nnplayer(game.getCanonicalForm(board, curplayer))
        print("move")
        print(move)
        if curplayer == 1:
            # if move > 4:
            #     move = move - 5
            #     direct = 1
            # else:
            #     direct = - 1
            # move = 11 - move
            if move > 4:
                move = move - 5
                direct = -1
            else:
                direct = 1
            move = 5 - move
        if curplayer == -1:
            if move > 4:
                move = move - 5
                direct = -1
            else:
                direct = 1
            move = 11 - move
        print(str(move))
        print(str(direct))
        time.sleep(0.20)
        IO.writeFile(send, ""+str(direct)+" "+str(move))
        IO.writeFile(receive, "")
        time.sleep(0.20)

