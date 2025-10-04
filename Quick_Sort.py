# from data_unsorted import numbers
# from data_unsorted_a_lot import numbers
from pyvisalgo import QuickSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
    print('before:', array)
    count = len(array)

    vis.push(0, count-1)
    pivot = partition(0, count-1)
    vis.set_pivot(pivot)

    print('after :', array)

def partition(left, right):

    pi = left
    pivot = array[pi]

    p, q = left, right +1

    while True:
        while True:
            p +=1
            vis.set_p(p)
            if q < p: break
            if p <= right: vis.compare(pi, p)
            if p> right or array[p] > pivot: break


            if p <= right: vis.set_left(p)

        while True:
            q -=1
            vis.set_q(q)
            if q < p: break
            if q >= left: vis.compare(pi, q)
            if q < left or array[q] < pivot: break


            if q >= left: vis.set_right(q)

        if p >= q: break


        vis.set_left(p)
        vis.set_right(q)

        vis.swap(p, q)
        array[p], array[q] = array[q], array[p]


    # 이 코드는 partition() 함수의 Loop 를 모두 빠져 나온 후에 실행되는 영역이다
    # pivot 값의 위치를 확정시킨다
    # pivot 값은 왼쪽 그룹 중에 가장 큰 값이므로 q 위치로 옮긴다
    # left 가 q 와 같다면 pivot 보다 작은것이 하나도 없다는 뜻이므로 옮길 필요가 없다
    if left != q:
        vis.swap(left, q, True)
        array[left], array[q] = array[q], array[left]

    return q

if __name__ == '__main__':
    seed('Hello')
    vis = Visualizer('Quick Sort')
    while True:
        count = randint(20, 40)
        array = [ randint(1, 99) for _ in range(count) ]
        vis.setup(vis.get_main_module())
        main()
        vis.draw()
        again = vis.end()
        if not again: break