

import matplotlib.pyplot as plt
import numpy as np

def simple_plot(pattern:np.ndarray):
    """
    @brief: does a simple plot of the pattern
    """
    plt.imshow(pattern)
    plt.show()