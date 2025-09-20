from data_unsorted import numbers
#from data_unsorted_a_lot import numbers
from pyvisalgo import SelectionSortVisualizer as Visualizer
#from pyvisalgo import Dummy as Visualizer

from random import randint, seed, shuffle
from time import time

def main():
    print('before : ', array)
    count = len(array)

    for a in range(count):
        min_value = array[a]
        min_at = a
        vis.selection(a)
        for b in range(a+1, count):
            vis.compare(min_at, b)
            if min_value > array[b]:
                min_value = array[b]
                min_at = b
                vis.selection(b)
        vis.swap(a, min_at)
        array[a], array[min_at] = array[min_at], array[a]
        vis.mark_done(a)
        print(f'{min_at=}. swap {a} <=> {min_at}')

    print('after : ', array)

'''

성능측정:
count=100 0.000
count=1000 0.018
count=2000 0.105
count=3000 0.207
count=4000 0.409
count=5000 0.549
count=6000 0.750
count=7000 0.970
count=8000 1.278
count=9000 1.425
count=10000 1.716
count=15000 4.196
count=20000 7.317
count=30000 15.246
count=40000 27.774
count=50000 43.077

'''

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