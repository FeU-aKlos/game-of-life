import numpy as np
from argparse import Namespace
from scipy import signal 

class GameOfLife():
    """
    @brief: this class implements the gamefield and its pattern, and rules for game of life
    """
    def __init__(self, args:Namespace):
        self.args = args
        self.center_coord = [1,1]
        self._select_pattern()
        
        
    def _select_pattern(self):
        """
        @brief: selects a pattern. 0: blinker, 1: beacon, 2: more fancy :D
        """
        def init_blinker_or_beacon_pattern():
            return np.zeros((self.args.game_field_size,self.args.game_field_size))
        
        self.pattern = {
            0: init_blinker_or_beacon_pattern(),#blinker
            1: init_blinker_or_beacon_pattern(),#beacon
            2: np.array(
                [
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                    [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                ]
            )
        }[self.args.pattern_idx]
    
        if self.args.pattern_idx == 0:
            pattern_size = 3
            self.pattern[self.args.game_field_size//2,1:self.args.game_field_size-1] = np.ones(pattern_size)
            
    def gol_iteration_simple(self):
        """
        @brief: perform one iteration on the gamefield (pattern)
        """
        self.tmp_pattern = self.pattern.copy()

        for col in range(1,self.args.game_field_size-1):
            for row in range(1,self.args.game_field_size-1):
                self.tmp_area_oi = self.pattern[col-1:col+2,row-1:row+2].copy()
                self.tmp_area_oi[self.center_coord[0],self.center_coord[0]] = 0
                life_or_dead_sum = np.sum(self.tmp_area_oi)
                if life_or_dead_sum < 2:
                    self.tmp_pattern[col,row] = 0
                elif life_or_dead_sum>=2 and life_or_dead_sum <=3:
                    if life_or_dead_sum == 3:
                        self.tmp_pattern[col,row] = 1
                elif life_or_dead_sum > 3:
                    self.tmp_pattern[col,row] = 0
        self.pattern = self.tmp_pattern
    
    def gol_iteration_conv(self):
        #TODO: still under development! ... not sure how this can be used, to be more efficient :/
        game_of_convolved_pattern = np.zeros((self.args.game_field_size,self.args.game_field_size))
        kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])
        #kernel is symmetric -> no cross correlation necessary! np.flipud(np.fliplr(kernel))
        game_of_convolved_pattern = signal.convolve2d(self.pattern,kernel, mode="same")
        print(game_of_convolved_pattern)
        
        
            
    
        
        
    