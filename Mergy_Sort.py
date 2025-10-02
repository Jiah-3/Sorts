from pyvisalgo import MergeSortVisualizer as Visualizer
# from pyvisalgo import Dummy as visualizer
from time import time
from random import randint, seed, shuffle

def main():
    print('before:', array)
    count = len(array)
    mergeSort(0, count-1)
    print('after :', array)

def mergeSort(left, right):
    if right <= left: return
    mid = (left + right) // 2
    vis.push(left, mid, right)
    mergeSort(left, mid)
    mergeSort(mid+1, right)
    merge(left, mid+1, right)
    vis.pop()

def merge(left, right, end):
    merged = []
    vis.start_merge(merged, False, left)
    l, r = left, right
    while l < right and r <= end:
        vis.compare(l, r)
        if array[l] <= array[r]:
            merged.append(array[l])
            vis.add_to_merged(l, True)
            l += 1
        else:
            merged.append(array[r])
            vis.add_to_merged(r, False)
            r += 1

    while l < right:
        merged.append(array[l])
        vis.add_to_merged(l, True)
        l += 1
    while r <= end:
        merged.append(array[r])
        vis.add_to_merged(r, False)
        r += 1

    vis.end_merge()

    l = left
    for n in merged:
        array[l] = n
        l += 1
        # vis.erase_merged()

if __name__ == '__main__':
    seed('Hello')
    vis = Visualizer('Merge Sort')
    while True:
        count = randint(20, 40)
        array = [ randint(1, 99) for _ in range(count)]
        vis.setup(vis.get_main_module())
        main()
        vis.draw()
        again = vis.end()
        if not again: break

