import random

import Data
import Sorts

if __name__ == '__main__':
    # O(N²)
    bubble = Sorts.BubbleSort()
    selection = Sorts.SelectionSort()
    insertion = Sorts.InsertionSort()
    gnome = Sorts.GnomeSort()

    # Middle
    shell = Sorts.ShellSort()
    tournament = Sorts.TournamentSort()
    pyramid = Sorts.PyramidSort()

    # O(NlogN)
    radix = Sorts.LSD()
    quick = Sorts.QuickSort()
    merge = Sorts.MergeSort()

    lists = {
        # Массивы случайных чисел. Длина: 10**4, 10**5, 10**6, 10**7.
        # 'Группа 1. Случайные числа: 0-999, L=10^4': Data.TestsGroup1().a,
        # 'Группа 1. Случайные числа: 0-999, L=10^5': Data.TestsGroup1().b,
        'Группа 1. Случайные числа: 0-999, L=10^6': Data.TestsGroup1().c,
        'Группа 1. Случайные числа: 0-999, L=10^7': Data.TestsGroup1().d,

        # Массивы, включающие несколько отсортированных последовательностей
        'Группа 2. Числа: 0-999, L=10^2*5': Data.TestsGroup2().a,
        'Группа 2. Числа: 0-999, L=10^4*5': Data.TestsGroup2().b,

        # Почти отсортированные массивы случайных чисел с
        # некоторым числом перестановок двух случайных элементов
        # 'Группа 3. Числа: 0-999, L=10^4, 100 перестановок': Data.TestsGroup3().a,
        # 'Группа 3. Числа: 0-999, L=10^5, 1000 перестановок': Data.TestsGroup3().b,
        'Группа 3. Числа: 0-999, L=10^6, 10000 перестановок': Data.TestsGroup3().c,
        'Группа 3. Числа: 0-999, L=10^7, 100000 перестановок': Data.TestsGroup3().d,

        # Полностью отсортированные (в прямом и обратном порядке) массивы
        # 'Группа 4. Числа: 0-999, L=10^4, по возрастанию': Data.TestsGroup4().a1,
        # 'Группа 4. Числа: 0-999, L=10^5, по возрастанию': Data.TestsGroup4().b1,
        'Группа 4. Числа: 0-999, L=10^6, по возрастанию': Data.TestsGroup4().c1,
        'Группа 4. Числа: 0-999, L=10^7, по возрастанию': Data.TestsGroup4().d1,
        # 'Группа 4. Числа: 0-999, L=10^4, по убыванию': Data.TestsGroup4().a2,
        # 'Группа 4. Числа: 0-999, L=10^5, по убыванию': Data.TestsGroup4().b2,
        'Группа 4. Числа: 0-999, L=10^6, по убыванию': Data.TestsGroup4().c2,
        'Группа 4. Числа: 0-999, L=10^7, по убыванию': Data.TestsGroup4().d2,

        # Массивы натуральных чисел от 1 до k, в котором несколько чисел заменены на случайное
        'Группа 5. Числа: 0-10^3, L=10^3, 10 замен': Data.TestsGroup5().a,
        'Группа 5. Числа: 0-10^4, L=10^4, 100 замен': Data.TestsGroup5().b,
        'Группа 5. Числа: 0-10^5, L=10^5, 1000 замен': Data.TestsGroup5().c,

        # Массивы с большим количеством повторений одного элемента (10%, 25%, 50%, 75% и 90%)
        'Группа 6. Числа: 0-999, L=10^5, 10%': Data.TestsGroup6().a,
        'Группа 6. Числа: 0-999, L=10^5, 25%': Data.TestsGroup6().b,
        'Группа 6. Числа: 0-999, L=10^5, 50%': Data.TestsGroup6().c,
        'Группа 6. Числа: 0-999, L=10^5, 75%': Data.TestsGroup6().d,
        'Группа 6. Числа: 0-999, L=10^5, 90%': Data.TestsGroup6().e
    }

    # for key, value in lists.items():
    #     bubble.measure_time(key, value.copy())
    # for key, value in lists.items():
    #     selection.measure_time(key, value.copy())
    # for key, value in lists.items():
    #     insertion.measure_time(key, value.copy())
    # for key, value in lists.items():
    #     gnome.measure_time(key, value.copy())
    # for key, value in lists.items():
    #     shell.measure_time(key, value.copy())
    # for key, value in lists.items():
    #     tournament.measure_time(key, value.copy())
    # for key, value in lists.items():
    #     pyramid.measure_time(key, value.copy())
    # for key, value in lists.items():
    #     radix.measure_time(key, value.copy())
    # for key, value in lists.items():
    #     quick.measure_time(key, value.copy())
    for key, value in lists.items():
        merge.measure_time(key, value.copy())
    # a = [random.randint(0, 999) for _ in range(100)]
    # selection.measure_time('test', a)
