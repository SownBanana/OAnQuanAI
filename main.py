from Coach import Coach
from Oanquan.Game import OanquanGame as Game
from Oanquan.tensorflow.NNet import NNetWrapper as nn
from utils import *
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

args = dotdict({
    'numIters': 1000,
    'numEps': 100,              # Số lần Self-play mỗi iter
    'tempThreshold': 15,
    'updateThreshold': 0.6,     # Update best.pth.tar nếu tỉ lệ thắng trên ngưỡng
    'maxlenOfQueue': 200000,    # Number of game examples to train the neural networks.
    'numMCTSSims': 25,          # Number of games moves for MCTS to simulate.
    'arenaCompare': 40,         # Number of games to play during arena play to determine if new net will be accepted.
    'cpuct': 1,

    'checkpoint': './temp/',    # folder lưu examples và best model

    'load_model': False,         # False - train lại từ đầu
    'load_folder_file': ('./temp/','best.pth.tar'), # model để train tiếp tục
    'numItersForTrainExamplesHistory': 20,

})

if __name__ == "__main__":
    g = Game(8)
    nnet = nn(g)

    if args.load_model:
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])

    c = Coach(g, nnet, args)
    if args.load_model:
        print("Load trainExamples from file")
        c.loadTrainExamples()
    c.learn()
