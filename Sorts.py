import json
import random
import time
import sys

sys.setrecursionlimit(10000001)


class Sorts:
    __COUNT = 2

    def run(self, array):
        pass

    def measure_time(self, key, value):
        result = 0
        for i in range(1, self.__COUNT):
            array = value.copy()
            start_time = time.time()
            self.run(array)
            end_time = time.time()
            result += (end_time - start_time)
        result = (result / self.__COUNT) * 1000
        data = {'Алгоритм': f'{self.__class__.__name__}', 'Массив': key, 'Время работы в миллисекундах:': result}
        with (open(f'./results/{self.__class__.__name__}.json', 'a', newline='', encoding='utf-8') as f):
            json.dump(data, f, ensure_ascii=False, indent=2)


# Пузырьковая сортировка - O(N²) - устойчивый - неестественный
class BubbleSort(Sorts):

    def run(self, array):
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array


# Сортировка выбором - O(N²) - неустойчивый - неестественный
class SelectionSort(Sorts):

    def run(self, array):
        for i in range(len(array) - 1):
            index_min = i
            for j in range(i + 1, len(array)):
                if array[j] < array[index_min]:
                    index_min = j
            array[i], array[index_min] = array[index_min], array[i]
        return array


# Сортировка вставками - O(N²) - устойчивый - естественный
class InsertionSort(Sorts):

    def run(self, array):
        for i in range(1, len(array)):
            k = array[i]
            j = i - 1
            while j >= 0 and array[j] > k:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = k
        return array


# Гномья сортировка - O(N²) - устойчивый - неестественный
class GnomeSort(Sorts):

    def run(self, array):
        i, j = 1, 2
        while i < len(array):
            if array[i] > array[i - 1]:
                i, j = j, j + 1
            else:
                array[i - 1], array[i] = array[i], array[i - 1]
                i = i - 1
                if i == 0:
                    i, j = j, j + 1
        return array


# Сортировка Шелла - O(N²) - устойчивый - естественный
class ShellSort(Sorts):

    def run(self, array):
        subarray = len(array) // 2
        while subarray >= 1:
            for i in range(subarray, len(array)):
                k = array[i]
                j = i - 1
                while j >= 0 and array[j] > k:
                    array[j + 1] = array[j]
                    j -= 1
                array[j + 1] = k
            subarray //= 2
        return array


# Поразрядная сортировка - O(nlogn) - устойчивый - неестественный
class LSD(Sorts):

    def __find_number_of_digits(self, array):
        amax = array[0]
        for el in array:
            if el > amax:
                amax = el
        m = 0
        while amax > 0:
            amax = amax // 10
            m += 1
        return m

    def __division_sort(self, array, remainder, divider):
        groups = [[] for _ in range(10)]
        for el in array:
            groups[int(el % remainder // divider)].append(el)
        array = []
        for item in groups:
            array += item
        return array

    def run(self, array):
        m = self.__find_number_of_digits(array)
        remainder = 10
        divider = 1
        while m > 0:
            array = self.__division_sort(array, remainder, divider)
            m -= 1
            remainder *= 10
            divider *= 10
        return array


# Быстрая сортировка
class QuickSort(Sorts):

    def run(self, array):
        min_index, max_index = 0, len(array) - 1
        res = self.__quick_sort(array, min_index, max_index)
        return res

    def __quick_sort(self, array, min_index, max_index):
        if min_index >= max_index:
            return array
        pivot = array[random.randint(min_index, max_index)]
        i, j = min_index, max_index
        while i <= j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        self.__quick_sort(array, min_index, j)
        self.__quick_sort(array, i, max_index)


# Пирамидальная сортировка - O(N*log2N) - неустойчивый - неестественный
class PyramidSort(Sorts):
    def __swap(self, array, num_1, num_2):
        array[num_1], array[num_2] = array[num_2], array[num_1]

    def __move_element(self, array, root, size):
        maxindex = root
        a = root * 2 + 1
        b = root * 2 + 2
        if a < size and array[maxindex] < array[a]:
            maxindex = a
        if b < size and array[maxindex] < array[b]:
            maxindex = b
        if maxindex == root:
            return
        self.__swap(array, maxindex, root)
        self.__move_element(array, maxindex, size)

    def run(self, array):
        for i in range(len(array) // 2, -1, -1):
            self.__move_element(array, i, len(array))
        for j in range(len(array) - 1, 0, -1):
            self.__swap(array, 0, j)
            self.__move_element(array, 0, j)
        return array


# Сортировка слиянием - O(N*log2N) - устойчивый
class MergeSort(Sorts):
    def __merge(self, array, min_index, pivot, max_index):
        left = array[min_index:pivot + 1]
        right = array[pivot + 1:max_index + 1]
        pointer, left_index, right_index = min_index, 0, 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                array[pointer] = left[left_index]
                left_index += 1
            else:
                array[pointer] = right[right_index]
                right_index += 1
            pointer += 1
        while left_index < len(left):
            array[pointer] = left[left_index]
            left_index += 1
            pointer += 1
        while right_index < len(right):
            array[pointer] = right[right_index]
            right_index += 1
            pointer += 1

    def __merge_sort(self, array, min_index, max_index):
        if max_index - min_index < 1:
            return array
        pivot = (min_index + max_index) // 2
        self.__merge_sort(array, min_index, pivot)
        self.__merge_sort(array, pivot + 1, max_index)
        self.__merge(array, min_index, pivot, max_index)
        return array

    def run(self, array):
        min_index, max_index = 0, len(array) - 1
        res = self.__merge_sort(array, min_index, max_index)
        return res
