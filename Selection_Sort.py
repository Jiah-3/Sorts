from data_unsorted import numbers
#from data_unsorted_a_lot import numbers
from random import randint, seed, shuffle
from pyvisalgo import SelectionSortVisualizer as Visualizer
#from pyvisalgo import Dummy as Visualizer
from time import time

def main():
    print('before : ', array)
    count = len(array)

    print('after : ', array)

if __name__ == '__main__':
    seed('Hello') # 'Hello'를 seed로 고정하여 randint가 항상 같은 결과가 나오게 한다
    vis = Visualizer('Selection Sort')

    while True:
        count = randint(10, 30)
        array = numbers[:count]
        vis.setup(vis.get_main_module())
        main()
        vis.draw()

        again = vis.end()
        if not again: break