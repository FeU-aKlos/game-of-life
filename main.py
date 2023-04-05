from game_of_life import GameOfLife

from visualize_gol import simple_plot
from utils import get_arguments

def main():
    args = get_arguments()
    game_of_life = GameOfLife(args)
    game_of_life.gol_iteration_simple()
    simple_plot(game_of_life.pattern)
    
        
    

if __name__=="__main__":
    main()