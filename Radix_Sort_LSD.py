#from data_unsorted import numbers
from data_unsorted_a_lot import numbers
#from pyvisalgo import RadixSortLsdVisualizer as Visualizer
#pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle
from math import log10, ceil

def main():
    global array
    #print(f'before:', array)
    count = len(array)

    global counts
    max_value = max(array)
    radix_count = ceil(log10(max_value + 1))
    #print(f'{max_value=} {log10(radix_count)=} {radix_count=}')

    global result
    result = []

    div = 1
    for pos in range(radix_count):
        counts = [0] * 10
        for i in range(count):
            v = array[i] // div % 10 #divdml 자리 숫자를 수하면 v는 0~9사이의 값
            counts[v] += 1
            #vis.set_inc_index(div, i)

        #print(f'counts= {counts}')
        #vis.set_inc_index(div, -1)
        for i in range(9):
            counts[i+1] += counts[i]
            #vis.draw()
            #vis.wait(1000)

        #print(f'indices={counts}')

        result = [None] * count

        for i in range(count-1, -1, -1):
            v = array[i] // div % 10
            at = counts[v] - 1
            counts[v] -= 1
            #vis.set_inc_index(div, i, False)
            result[at] = array[i]
            #print(f'{i=:2d} {v=:2d} {result=}')

        #vis.result_to_array()
        array = result
        result = []
        div *= 10

    #print('after :', array)
'''
count=100    elapsed=0.000
count=1000   elapsed=0.002
count=2000   elapsed=0.003
count=3000   elapsed=0.005
count=4000   elapsed=0.008
count=5000   elapsed=0.008
count=6000   elapsed=0.009
count=7000   elapsed=0.016
count=8000   elapsed=0.012
count=9000   elapsed=0.019
count=10000  elapsed=0.030
count=15000  elapsed=0.036
count=20000  elapsed=0.032
count=30000  elapsed=0.100
count=40000  elapsed=0.100
count=50000  elapsed=0.167
count=100000 elapsed=0.241
count=200000 elapsed=0.497
count=300000 elapsed=0.888
count=400000 elapsed=1.185
count=500000 elapsed=1.574
count=1000000 elapsed=2.815
count=2000000 elapsed=7.813
count=3000000 elapsed=11.341
count=4000000 elapsed=14.626
count=5000000 elapsed=20.483
count=10000000 elapsed=47.878
'''
if __name__=='__main__':
    seed('HelloCountSort')
    counts = [1000000, 2000000, 3000000, 4000000, 5000000, 10000000]
    for count in counts:
        startedOn = time()
        array = list(map(lambda x: randint(1, count), range(count)))
        elapsed = time() - startedOn
        print(f'Creating List: {count=:<6d} {elapsed=:.3f}')
        #shuffle(array)
        #print(f'before:', array)
        startedOn = time()
        main()
        elapsed = time() - startedOn
        #print(f'after :', array)
        print(f'{count=:<6d} {elapsed=:.3f}')
    exit()

    vis = Visualizer('Radix Sort: LSD')
    while True:
        kind = 100000
        count = randint(30, 80)
        print(f'Creating data: {kind=} {count=}')
        array = list(map(lambda x: randint(1, kind), range(count)))
        vis.setup(vis.get_main_module())
        main()
        vis.draw()
        again = vis.end()
        if not again: break