# Сортировка массива по возрасанию
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if i < smallest:
            smallest = arr[i]
            smallest_index = i
        return smallest_index
#Теперь на основе этой функции можно написать функцию сортировки выбором
def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

# Вставка элемента по индексу
def get_node_by_index(node, index):
    while index:
        node = node.next
        index -= 1
    return node

def insert_node(head, index, value):
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node
    previous_node = get_node_by_index(head, index-1)
    new_node.next = previous_node.next
    previous_node.next = new_node
    return head


#Ускорение скользящего среднего
from typing import List, Tuple


def binary_search(list, i):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == i:
            return mid
        if guess > i:
            


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


# Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку, и на экране появляются три случайных числа. 
# Если все три числа оказываются одной чётности, игрок выигрывает.
# Напишите программу, которая по трём числам определяет, выиграл игрок или нет.
def check_parity(a: int, b: int, c: int) -> bool:    
    if a % 2 == b % 2 == c % 2:
        result = True
        return result
        

def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")

a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))


# Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей.
# Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз.
# Диагональные элементы соседними не считаются.
from typing import List, Tuple

def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    
    pass

def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col

matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))