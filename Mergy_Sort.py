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
    if right == left + 1:
        if array[right] < array[left]:
            #vis.compare(left, right)
            if array[left] > array[right]:
                #vis.swap(left, right
                array[left], array[right] = array[right], array[left]
            return
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

    array[left:end+1] = merged

    #l = left
    #for n in merged:
        #array[l] = n
        #l += 1

        # vis.erase_merged()

''' 성능 측정          orig slice 2only bugfx
count=100    elapsed=0.000 0.000 0.000 0.000
count=1000   elapsed=0.002 0.001 0.001 0.001
count=2000   elapsed=0.003 0.004 0.003 0.003
count=3000   elapsed=0.005 0.005 0.004 0.005
count=4000   elapsed=0.007 0.008 0.007 0.006
count=5000   elapsed=0.022 0.010 0.010 0.010
count=6000   elapsed=0.026 0.009 0.010 0.011
count=7000   elapsed=0.023 0.011 0.012 0.012
count=8000   elapsed=0.029 0.013 0.012 0.013
count=9000   elapsed=0.020 0.015 0.014 0.015
count=10000  elapsed=0.032 0.019 0.016 0.020
count=15000  elapsed=0.048 0.025 0.025 0.029
count=20000  elapsed=0.074 0.051 0.033 0.046
count=30000  elapsed=0.103 0.079 0.083 0.103
count=40000  elapsed=0.133 0.117 0.078 0.115
count=50000  elapsed=0.175 0.143 0.109 0.279
count=100000 elapsed=0.366 0.272 0.236 0.342
count=200000 elapsed=0.688 0.691 0.499 0.616
count=300000 elapsed=0.960 0.821 0.773 0.849
count=400000 elapsed=1.552 1.197 1.007 1.255
count=500000 elapsed=1.985 1.374 1.546 1.714
count=1000000 elapsed=4.284 3.283 3.573 3.237
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

