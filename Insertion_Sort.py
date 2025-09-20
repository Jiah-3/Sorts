from data_nearly_sorted_a_lot import nearly as numbers
#from data_unsorted import numbers
#from data_unsorted_a_lot import numbers
from random import randint, seed, shuffle
#from pyvisalgo import InsertionSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time

def main_level_1():
    print('before:', array)
    count = len(array)

    for i in range(1, count):
        vis.mark_end(i)
        for j in range(i, 0, -1):
            vis.compare(j-1, j)
            if array[j-1] > array[j]:
                vis.swap(j-1, j)
                array[j-1], array[j] = array[j], array[j-1]

    print('after :', array)

def main_level_2():
    print('before:', array)
    count = len(array)

    for i in range(1, count):
        vis.mark_end(i)
        for j in range(i, 0, -1):
            vis.compare(j-1, j)
            if array[j-1] > array[j]:
                vis.swap(j-1, j)
                array[j-1], array[j] = array[j], array[j-1]
            else:
                break

    print('after :', array)

def main():
    #print('before:', array)
    count = len(array)

    for i in range(1, count):
        #vis.mark_end(i, True)
        v = array[i]
        j = i
        while j > 0:
            #vis.compare(j-1, j)
            if array[j - 1] > v:
                #vis.shift(j - 1, j)
                array[j] = array[j - 1]
                #vis.draw()
                j -= 1
            else:
                break
        #vis.shift(i, j, True)
        array[j] = v
        #vis.draw()

    #vis.draw()

    #print('after :', array)

'''
성능 측정 결과
count=100 elapsed=0.000
count=1000 elapsed=0.026
count=2000 elapsed=0.102
count=3000 elapsed=0.259
count=4000 elapsed=0.404
count=5000 elapsed=0.815
count=6000 elapsed=0.941
count=7000 elapsed=1.321
count=8000 elapsed=1.686
count=9000 elapsed=2.136
count=10000 elapsed=2.567
count=15000 elapsed=6.207
count=20000 elapsed=10.484
count=30000 elapsed=23.893
count=40000 elapsed=40.613
count=50000 elapsed=63.781
'''

if __name__ == '__main__':
    seed('Hello') # 'Hello'를 seed로 고정하여 randint가 항상 같은 결과가 나오게 한다
    #vis = Visualizer('Insertion Sort')


    counts = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 30000, 40000, 50000]
    for count in counts:
        array = numbers[:count]
        #shuffle(array)
        startedOn = time()
        main()
        elapsed = time() - startedOn
        print(f'{count=:5d} {elapsed=:7.3f}')
    exit(0)

    while True:
        count = randint(10, 30)
        array = numbers[:count]
        vis.setup(vis.get_main_module())
        main()
        vis.draw()

        again = vis.end()
        if not again: break
