#from data_unsorted import numbers
from data_unsorted_a_lot import numbers
#from pyvisalgo import CountSortVisualizer as Visualizer
from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
    #print(f'before:', array)
    count = len(array)

    global counts
    max_value = max(array)
    counts = [0] * (max_value + 1)
    #print(f'init - {counts=}')

    for i in range(count):
        v = array[i]
        counts[v] += 1
        #vis.set_inc_index(i)

    #vis.set_inc_index(-1)
    for i in range(max_value):
        counts[i + 1] += counts[i]
        #vis.draw()
        #vis.wait(1000)

    global result
    result = [None] * count

    for i in range(count -1, -1, -1):
        v = array[i]
        at = counts[v] - 1
        counts[v] -= 1
        #vis.set_inc_index(i, False)
        result[at] = v
        #print(f'{i=:2d} {v=:2d} {result=}')

    #vis.set_inc_index(-1, False)
    #print('after:', array)

if __name__ == '__main__':
    seed('HelloCountSort')
    counts = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 30000, 40000, 50000, 100000, 200000, 300000, 400000, 500000]
    for count in counts:
        kind = randint(10, 300)
        #print(f'Creating data: {kind=} {count=}')
        array = list(map(lambda x: x%kind, numbers[1000:1000+count]))
        shuffle(array)
        #print('before :', array)
        startedOn = time()
        main()
        elapsed = time() - startedOn
        #print(f'after :, result)
        print(f'{count=:<6d} {kind=:<3d} {elapsed=:.3f}')
    exit()

    vis = Visualizer('Count Sort')
    while True:
        kind = randint(6, 30)
        count = randint(30, 150)
        print(f'Creating data: {kind=} {count=}')
        array = list(map(lambda x: x%kind, numbers[1000:1000+count]))
        vis.setup(vis.get_main_module())
        main()
        vis.draw()
        again = vis.end()
        if not again: break