#from data_unsorted import numbers
from data_unsorted_a_lot import numbers
from random import randint, seed, shuffle
#from pyvisalgo import HeapSortVisualizer as Visualizer
#from pyvisalgo import Dummy as Visualizer
from time import time

def heapify(root, size):
    lc = root * 2 + 1
    if lc >= size: return
    child = lc
    rc = root * 2 + 2
    if rc < size:
        #vis.compare(rc, lc)
        if array[rc] > array[lc]:
            child = rc

    #vis.compare(root, child)
    if array[root] < array[child]:
        #vis.swap(root, child)
        array[root], array[child] = array[child], array[root]
        heapify(child, size)

def main():
    #print('before', array)
    count = len(array)
    #vis.build_tree()

    last_parent_index = count // 2 - 1
    for n in range(last_parent_index, -1, -1):
        #vis.set_root(n)
        heapify(n, count)

    last_sort_index = count - 1
    while last_sort_index > 0:
        #vis.compare(0, last_sort_index)
        #vis.swap(0, last_sort_index)
        #첫번째와 마지막의 원소를 교환한다
        array[0], array[last_sort_index] = array[last_sort_index], array[0]
        #vis.set_tree_size(last_sort_index)
        heapify(0, last_sort_index)
        last_sort_index -= 1

    #vis.set_tree_size(0)
    #print('after', array)

'''
count=   100 elapsed=  0.000
count=  1000 elapsed=  0.006
count=  2000 elapsed=  0.011
count=  3000 elapsed=  0.018
count=  4000 elapsed=  0.025
count=  5000 elapsed=  0.028
count=  6000 elapsed=  0.038
count=  7000 elapsed=  0.040
count=  8000 elapsed=  0.048
count=  9000 elapsed=  0.056
count= 10000 elapsed=  0.064
count= 15000 elapsed=  0.105
count= 20000 elapsed=  0.132
count= 30000 elapsed=  0.231
count= 40000 elapsed=  0.344
count= 50000 elapsed=  0.465
count=100000 elapsed=  1.107
count=200000 elapsed=  2.222
count=300000 elapsed=  3.344
count=400000 elapsed=  4.869
count=500000 elapsed=  6.107
'''

if __name__=='__main__':
    seed('Hello')
    counts = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 30000, 40000, 50000, 100000, 200000, 300000, 400000, 500000]
    for count in counts:
        array = numbers[:count]
        shuffle(array)
        startedOn = time()
        main()
        elapsed = time() - startedOn
        print(f'{count=:6d} {elapsed=:7.3f}')
    exit()
    vis = Visualizer('Heap Sort')
    while True:
        array = numbers[:randint(10, 30)]
        vis.setup(vis.get_main_module())
        startedOn = time()
        main()
        elapsed = time() - startedOn
        print(f'Elapsed time: {elapsed:.3f}s')
        again = vis.end()
        if not again: break