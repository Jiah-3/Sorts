#from pyvisalgo import MergeSortVisualizer as Visualizer
# from pyvisalgo import Dummy as visualizer
from time import time
from random import randint, seed, shuffle
#from data_unsorted import numbers
from data_unsorted_a_lot import numbers

def main():
    #print('before:', array)
    count = len(array)
    mergeSort(0, count-1)
    #print('after :', array)

def mergeSort(left, right):
    if right <= left: return
    mid = (left + right) // 2
    #vis.push(left, mid, right)
    mergeSort(left, mid)
    mergeSort(mid+1, right)
    merge(left, mid+1, right)
    #vis.pop()

def merge(left, right, end):
    merged = []
    #vis.start_merge(merged, False, left)
    l, r = left, right
    while l < right and r <= end:
        #vis.compare(l, r)
        if array[l] <= array[r]:
            merged.append(array[l])
            #vis.add_to_merged(l, True)
            l += 1
        else:
            merged.append(array[r])
            #vis.add_to_merged(r, False)
            r += 1

    while l < right:
        merged.append(array[l])
        #vis.add_to_merged(l, True)
        l += 1
    while r <= end:
        merged.append(array[r])
        #vis.add_to_merged(r, False)
        r += 1

    #vis.end_merge()

    l = left
    for n in merged:
        array[l] = n
        l += 1
        # vis.erase_merged()

''' 성능 측정
count=100    elapsed=0.000
count=1000   elapsed=0.002
count=2000   elapsed=0.003
count=3000   elapsed=0.005
count=4000   elapsed=0.007
count=5000   elapsed=0.022
count=6000   elapsed=0.026
count=7000   elapsed=0.023
count=8000   elapsed=0.029
count=9000   elapsed=0.020
count=10000  elapsed=0.032
count=15000  elapsed=0.048
count=20000  elapsed=0.074
count=30000  elapsed=0.103
count=40000  elapsed=0.133
count=50000  elapsed=0.175
count=100000 elapsed=0.366
count=200000 elapsed=0.688
count=300000 elapsed=0.960
count=400000 elapsed=1.552
count=500000 elapsed=1.985
count=1000000 elapsed=4.284
'''

if __name__ == '__main__':
    seed('Hello')

    counts = [
        100, 1000, 2000, 3000, 4000, 5000,
        6000, 7000, 8000, 9000, 10000, 15000,
        20000, 30000, 40000, 50000,
        100000, 200000, 300000, 400000, 500000,
        1000000, 2000000, 3000000, 4000000, 5000000,
    ]
    for count in counts:
        # array = number[:count]
        # shuffle(array)
        mmm = count * 10 + randint(1, 1000)
        array = [ randint(1, mmm) for _ in range(count)]
        #print('before:', array)
        startedOn = time()
        main()
        elapsed = time() - startedOn
        print(f'{count=:<6d} {elapsed=:.3f}')
    exit()
    vis = Visualizer('Merge Sort')
    while True:
        count = randint(20, 40)
        array = [ randint(1, 99) for _ in range(count)]
        vis.setup(vis.get_main_module())
        main()
        vis.draw()
        again = vis.end()
        if not again: break

