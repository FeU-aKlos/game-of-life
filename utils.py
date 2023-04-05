from argparse import ArgumentParser, Namespace
import matplotlib.pyplot as plt
import numpy as np
import os
import imageio

plt.axis("off")
def get_arguments():
    parser = ArgumentParser()
    parser.add_argument("-gfs", "--game_field_size", dest="game_field_size", default=5, type=int)
    parser.add_argument("-p", "--pattern_idx", dest="pattern_idx", default=0, type=int, help="0: blinker, 1: beacon, 2: Gosper glider gun <- still not implemented") #TODO Gosper glider gun <- still not implemented
    parser.add_argument("-d", "--pattern_storage_directory", dest="pattern_storage_directory", default="patterns", type=str)
    args = parser.parse_args()
    
    if args.pattern_idx == 0:
        try:
            assert args.game_field_size == 5, f"{args.game_field_size} == 5"
        except AssertionError as e:
            print(e)
            print("game field size for chosen pattern must be 5!")
    elif args.pattern_idx == 1:
        try:
            assert args.game_field_size == 6, f"{args.game_field_size} == 6"
        except AssertionError as e:
            print(e)
            print("game field size for chosen pattern must be 6!")
    else:
        print("pattern still not implemented!!!")
        exit(1)
        
    if not os.path.isdir(args.pattern_storage_directory):
        os.makedirs(args.pattern_storage_directory)
    
    return args

PATTERN_DICT = {
    0:"blinker",
    1:"beacon", #<- TODO
    2:"Gosper glider gun" #<- TODO
}


def save_fig(args:Namespace,pattern:np.ndarray, it:int):
    """
    @brief: save the pattern to file
    """
    full_fn = os.path.join(args.pattern_storage_directory, PATTERN_DICT[args.pattern_idx]+f"_{it}.png")
    plt.imshow(pattern)
    plt.savefig(full_fn)
    
def generate_gif(agrs):
    image