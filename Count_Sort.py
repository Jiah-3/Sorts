#from data_unsorted import numbers
from data_unsorted_a_lot import numbers
from pyvisalgo import CountSortVisualizer as Visualizer
#from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
    print(f'before:', array)
    count = len(array)

    global counts
    max_value = max(array)
    counts = [0] * (max_value + 1)
    #print(f'init - {counts=}')

    global result
    result = []

    for i in range(count):
        v = array[i]
        counts[v] += 1
        vis.set_inc_index(i)

    vis.set_inc_index(-1)
    for i in range(max_value):
        counts[i + 1] += counts[i]
        vis.draw()
        vis.wait(1000)

    #global result
    result = [None] * count

    for i in range(count -1, -1, -1):
        v = array[i]
        at = counts[v] - 1
        counts[v] -= 1
        vis.set_inc_index(i, False)
        result[at] = v
        #print(f'{i=:2d} {v=:2d} {result=}')

    vis.set_inc_index(-1, False)
    print('after:', array)

'''
count=100    kind=291 elapsed=0.000
count=1000   kind=261 elapsed=0.000
count=2000   kind=270 elapsed=0.000
count=3000   kind=296 elapsed=0.000
count=4000   kind=182 elapsed=0.000
count=5000   kind=44  elapsed=0.001
count=6000   kind=33  elapsed=0.001
count=7000   kind=172 elapsed=0.001
count=8000   kind=57  elapsed=0.001
count=9000   kind=58  elapsed=0.001
count=10000  kind=45  elapsed=0.001
count=15000  kind=289 elapsed=0.002
count=20000  kind=293 elapsed=0.003
count=30000  kind=173 elapsed=0.004
count=40000  kind=153 elapsed=0.005
count=50000  kind=53  elapsed=0.007
count=100000 kind=13  elapsed=0.014
count=200000 kind=128 elapsed=0.027
count=300000 kind=293 elapsed=0.064
count=400000 kind=208 elapsed=0.063
count=500000 kind=14  elapsed=0.075


'''

if __name__ == '__main__':
    seed('HelloCountSort')
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