from pyvisalgo import MergeSortVisualizer as Visualizer
# from pyvisalgo import Dummy as visualizer
from time import time
from random import randint, seed, shuffle

def main():
    print('before:', array)
    count = len(array)
    print('after :', array)

if __name__ == '__main__':
    seed('Hello')
    vis = Visualizer('Merge Sort')
    while True:
        count = randint(20, 40)
        array = [ randint(1, 99) for _ in range(count)]
        vis.setup(vis.get_main_module())
        main()
        vis.draw()
        again = vis.end()
        if not again: break

