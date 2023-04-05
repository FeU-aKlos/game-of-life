from argparse import Namespace
from unittest import TestCase
import logging
import sys
import numpy as np

from game_of_life import GameOfLife

class TestGameOfLife(TestCase): 
    """
    @brief: this class is an unittest testcase for the GameOfLife class
    """
    @classmethod
    def setUpClass(cls):
        logging.basicConfig( stream=sys.stderr )
        logging.getLogger( "TestGameOfLife").setLevel(logging.DEBUG)
        cls.logger = logging.getLogger("TestGameOfLife")

        cls.args = Namespace()
        vars(cls.args)["game_field_size"] = 5
        vars(cls.args)["pattern_idx"] = 0
        cls.game_of_life = GameOfLife(cls.args)
        cls.logger.debug("\n%s",cls.game_of_life.pattern)
        
        cls.args_beacon = Namespace()
        vars(cls.args_beacon)["game_field_size"] = 6
        vars(cls.args_beacon)["pattern_idx"] = 1
        cls.game_of_life_beacon = GameOfLife(cls.args_beacon)
        cls.logger.debug("\n%s",cls.game_of_life_beacon.pattern)
    
    def setUp(self):
        pass
        
    def test_gol_iteration_simple(self):
        """
        @brief: test the gol... simple implementation
        """
        pattern_size = 3
        compare_array = np.ones(pattern_size)
        self.game_of_life.gol_iteration_simple()
        array_oi = self.game_of_life.pattern[1:self.args.game_field_size-1, self.args.game_field_size//2]
        self.logger.debug("\n%s",   self.game_of_life.pattern)
        
        assert (array_oi == compare_array).all()
        
        self.game_of_life.gol_iteration_simple()
        array_oi = self.game_of_life.pattern[self.args.game_field_size//2,  1:self.args.game_field_size-1]
        self.logger.debug("\n%s",   self.game_of_life.pattern)
        
        assert (array_oi == compare_array).all()
        
        
        compare_array_beacon = np.zeros((self.args_beacon.game_field_size,self.args_beacon.game_field_size))
        compare_array_beacon[1:3,1:3] = np.ones((2,2))
        compare_array_beacon[3:5,3:5] = np.ones((2,2))
        self.logger.debug("\n%s", compare_array_beacon)

        assert (self.game_of_life_beacon.pattern == compare_array_beacon).all()
        
        compare_array_beacon[3,3] = 0
        compare_array_beacon[2,2] = 0
        
        self.game_of_life_beacon.gol_iteration_simple()
        
        assert (self.game_of_life_beacon.pattern == compare_array_beacon).all()

        
        self.logger.debug("\n%s",   self.game_of_life_beacon.pattern)
        
        
        
        
    def test_gol_iteration_conv(self):
        self.game_of_life.gol_iteration_conv()

        
        