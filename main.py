#Ускорение скользящего среднего
from typing import List, Tuple


def moving_average(arr):
    pass

#Наивный вариант решения 2-SUM
def two_sum(arr, x):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == x:
                return arr[i], arr[j]
            return None, None


#Вариант решения 2-SUM с сортировкой
def two_sum_sort(arr, x):
    arr.sort() #сортируем массив
    left = 0
    right = len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == x:
            return arr[left], arr[right]
        if curr_sum < x:
            left += 1
        else:
            right -= 1
    return None, None
        
#Вариант решения 2-SUM с использованием доп.памяти
def two_sum_memory(arr, x):
    temp = set()
    for i in arr:
        y = x - i
        if y in temp:
            return y, i
        else:
            temp.add(i)
    return None, None