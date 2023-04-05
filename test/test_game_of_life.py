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
        cls.args = Namespace()
        vars(cls.args)["game_field_size"] = 5
        vars(cls.args)["pattern_idx"] = 0
        cls.logger = logging.getLogger("TestGameOfLife")
        cls.game_of_life = GameOfLife(cls.args)
        cls.logger.debug("\n%s",cls.game_of_life.pattern)
    
    def setUp(self):
        pass
        
    def test_gol_iteration_simple(self):
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
        
    def test_gol_iteration_conv(self):
        self.game_of_life.gol_iteration_conv()

        
        