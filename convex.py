import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.axes import Axes


class Point:

    def __init__(self, *args):
        if len(args) == 1:
            self.x = args[0][0]
            self.y = args[0][1]

        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


def main():
    pass


if __name__ == '__main__':
    main()
