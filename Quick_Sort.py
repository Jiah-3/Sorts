# from pyvisalgo import QuickSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
    #print('before:', array)
    count = len(array)
    quicksort(0, count-1)

    #print('after :', array)

def quicksort(left, right):
    #if left == right: vis.fix(left)
    if left >= right: return
    if right < left + 4:
        insertionsort(left, right)
        return
    #vis.push(left, right)
    pivot = partition(left, right)
    #vis.set_pivot(pivot)
    quicksort(left, pivot-1)
    quicksort(pivot+1, right)
    #vis.pop()

def insertionsort(left, right):
    for i in range(left + 1, right + 1):
        v = array[i]
        # vis.mark_end(i, v)
        j = i - 1
        while j >= left and array[j] > v:
            # vis.shift(j)
            array[j + 1] = array[j]
            j -= 1
        # vis.insert(i, j+1)
        array[j + 1] = v

def partition(left, right):

    pi = left
    pivot = array[pi]

    p, q = left, right +1

    while True:
        while True:
            p +=1
            #vis.set_p(p)
            if q < p: break
            #if p <= right: vis.compare(pi, p)
            if p> right or array[p] > pivot: break


            #if p <= right: vis.set_left(p)

        while True:
            q -=1
            #vis.set_q(q)
            if q < p: break
            #if q >= left: vis.compare(pi, q)
            if q < left or array[q] < pivot: break


            #if q >= left: vis.set_right(q)

        if p >= q: break


        #vis.set_left(p)
        #vis.set_right(q)

        #vis.swap(p, q)
        array[p], array[q] = array[q], array[p]



    # 이 코드는 partition() 함수의 Loop 를 모두 빠져 나온 후에 실행되는 영역이다
    # pivot 값의 위치를 확정시킨다
    # pivot 값은 왼쪽 그룹 중에 가장 큰 값이므로 q 위치로 옮긴다
    # left 가 q 와 같다면 pivot 보다 작은것이 하나도 없다는 뜻이므로 옮길 필요가 없다
    if left != q:
        #vis.swap(left, q, True)
        array[left], array[q] = array[q], array[left]

    return q

'''성능 측정
#Quick Sort           Normal  2-swap  4-Ins
count=100     elapsed= 0.000  0.000   0.000
count=1000    elapsed= 0.001  0.001   0.001
count=2000    elapsed= 0.003  0.003   0.002
count=3000    elapsed= 0.004  0.003   0.005
count=4000    elapsed= 0.006  0.005   0.005
count=5000    elapsed= 0.007  0.006   0.006
count=6000    elapsed= 0.009  0.006   0.007
count=7000    elapsed= 0.022  0.007   0.009
count=8000    elapsed= 0.017  0.009   0.012
count=9000    elapsed= 0.026  0.010   0.012
count=10000   elapsed= 0.029  0.013   0.014
count=15000   elapsed= 0.025  0.017   0.039
count=20000   elapsed= 0.042  0.023   0.043
count=30000   elapsed= 0.063  0.039   0.077
count=40000   elapsed= 0.148  0.090   0.068
count=50000   elapsed= 0.147  0.079   0.096
count=100000  elapsed= 0.256  0.203   0.218
count=200000  elapsed= 0.600  0.378   0.405
count=300000  elapsed= 0.802  0.623   0.805
count=400000  elapsed= 1.125  0.852   1.071
count=500000  elapsed= 1.645  1.093   1.478
count=1000000 elapsed= 3.360  2.297   2.679
count=2000000 elapsed= 8.011  6.157   7.123
count=3000000 elapsed=12.169  9.965   9.634
count=4000000 elapsed=15.897  13.828  13.284
count=5000000 elapsed=20.592  16.930  16.680
'''
if __name__ == '__main__':
    seed('Hello')

    counts = [
        # 10,20,30,50,100
        100, 1000, 2000, 3000, 4000, 5000,
        6000, 7000, 8000, 9000, 10000, 15000,
        20000, 30000, 40000, 50000,
        100000, 200000, 300000, 400000, 500000,
        1000000, 2000000, 3000000, 4000000, 5000000,
    ]
    for count in counts:
        startedOn = time()
        array = [ randint(1, count) for _ in range(count) ]
        creation = time() - startedOn
        # shuffle(array)
        # print('before:', array)
        startedOn = time()
        main()
        elapsed = time() - startedOn
        # print('after: ', array)
        print(f'{count=:<7d} {elapsed=:6.3f} {creation=:5.2f}')
    exit()

    #vis = Visualizer('Quick Sort')
    while True:
        count = randint(20, 40)
        array = [ randint(1, 99) for _ in range(count) ]
        vis.setup(vis.get_main_module())
        main()
        vis.draw()
        again = vis.end()
        if not again: break