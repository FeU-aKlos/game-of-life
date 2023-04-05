from argparse import ArgumentParser

def get_arguments():
    parser = ArgumentParser()
    parser.add_argument("-gfs", "--game_field_size", dest="game_field_size", default=5, type=int)
    parser.add_argument("-p", "--pattern_idx", dest="pattern_idx", default=0, type=int, help="0: blinker, 1: beacon, 2: Gosper glider gun <- still not implemented") #TODO Gosper glider gun <- still not implemented
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
    
    return args