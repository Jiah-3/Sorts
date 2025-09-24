#from data_unsorted import numbers
from data_unsorted_a_lot import numbers
from pyvisalgo import RadixSortLsdVisualizer as Visualizer
#pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle
from math import log10, ceil

def main():
    print(f'before:', array)
    count = len(array)

    global counts
    max_value = max(array)
    radix_count = ceil(log10(max_value))
    print(f'{max_value=} {log10(radix_count)=} {radix_count=}')
    counts = [0] * 10

    global result
    result = []

    div = 1
    for pos in range(1):
        for i in range(count):
            v = array[i] // div % 10 #divdml 자리 숫자를 수하면 v는 0~9사이의 값
            counts[v] += 1
            vis.set_inc_index(div, i)

        print(f'counts= {counts}')
        vis.set_inc_index(div, -1)
        for i in range(9):
            counts[i+1] += counts[i]
            vis.draw()
            vis.wait(1000)

        print(f'indices={counts}')


    #print('after :', array)

if __name__=='__main__':
    seed('HelloCountSort')
    vis = Visualizer('Radix Sort: LSD')
    while True:
        kind = 1000
        count = randint(30, 150)
        print(f'Creating data: {kind=} {count=}')
        begin = 500 + randint(1, 100)
        array = list(map(lambda x: x%kind, numbers[begin:begin+count]))
        vis.setup(vis.get_main_module())
        main()
        vis.draw()
        again = vis.end()
        if not again: break;