from game_of_life import GameOfLife

from utils import get_arguments, save_fig

def main():
    args = get_arguments()
    game_of_life = GameOfLife(args)
    if args.pattern_idx < 2:
        iterations = 2
        for i in range(iterations):
            game_of_life.gol_iteration_simple()
            save_fig(args,game_of_life.pattern,i)
    
        
    

if __name__=="__main__":
    main()