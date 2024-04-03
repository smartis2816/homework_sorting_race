import random


class TestsGroup1:  # Массивы случайных чисел. Длина: 10**4, 10**5, 10**6, 10**7.
    def __init__(self):
        self.a = [random.randint(0, 999) for _ in range(10 ** 3)]
        self.b = [random.randint(0, 999) for _ in range(10 ** 4)]
        self.c = [random.randint(0, 999) for _ in range(10 ** 5)]
        self.d = [random.randint(0, 999) for _ in range(10 ** 6)]


class TestsGroup2:  # Массивы, включающие несколько отсортированных последовательностей
    def __init__(self):
        self.a = [random.randint(0, 999) for _ in range(10 ** 2)] + sorted(
            [random.randint(0, 999) for _ in range(10 ** 2)]) + \
                 [random.randint(0, 999) for _ in range(10 ** 2)] + sorted(
            [random.randint(0, 999) for _ in range(10 ** 2)]) + \
                 [random.randint(0, 999) for _ in range(10 ** 2)]
        self.b = [random.randint(0, 999) for _ in range(10 ** 4)] + sorted(
            [random.randint(0, 999) for _ in range(10 ** 4)]) + \
                 [random.randint(0, 999) for _ in range(10 ** 4)] + sorted(
            [random.randint(0, 999) for _ in range(10 ** 4)]) + \
                 [random.randint(0, 999) for _ in range(10 ** 4)]
        self.c = [random.randint(0, 999) for _ in range(10 ** 6)] + sorted(
            [random.randint(0, 999) for _ in range(10 ** 6)]) + \
                 [random.randint(0, 999) for _ in range(10 ** 6)] + sorted(
            [random.randint(0, 999) for _ in range(10 ** 6)]) + \
                 [random.randint(0, 999) for _ in range(10 ** 6)]


class TestsGroup3:  # Почти отсортированные массивы случайных чисел с
    # некоторым числом перестановок двух случайных элементов
    def __init__(self):
        self.a = self.__sorted_array_with_swaps(100, 10 ** 3)
        self.b = self.__sorted_array_with_swaps(100, 10 ** 4)
        self.c = self.__sorted_array_with_swaps(1000, 10 ** 5)
        self.d = self.__sorted_array_with_swaps(10000, 10 ** 6)

    def __sorted_array_with_swaps(self, n, k):
        a = sorted([random.randint(0, 999) for _ in range(k)])
        for _ in range(n - 1):
            num1, num2 = random.randint(0, k - 1), random.randint(0, k - 1)
            a[num1], a[num2] = a[num2], a[num1]
        return a


class TestsGroup4:  # Полностью отсортированные (в прямом и обратном порядке) массивы
    def __init__(self):
        self.a1 = sorted([random.randint(0, 999) for _ in range(10 ** 3)])
        self.b1 = sorted([random.randint(0, 999) for _ in range(10 ** 4)])
        self.c1 = sorted([random.randint(0, 999) for _ in range(10 ** 5)])
        self.d1 = sorted([random.randint(0, 999) for _ in range(10 ** 6)])

        self.a2 = sorted([random.randint(0, 999) for _ in range(10 ** 3)])
        self.b2 = sorted([random.randint(0, 999) for _ in range(10 ** 4)])
        self.c2 = sorted([random.randint(0, 999) for _ in range(10 ** 5)])
        self.d2 = sorted([random.randint(0, 999) for _ in range(10 ** 6)])


class TestsGroup5:  # Массивы натуральных чисел от 1 до k, в котором несколько чисел заменены на случайное
    def __init__(self):
        self.a = self.__array_from_1_to_n_with_random(10, 10 ** 3)
        self.b = self.__array_from_1_to_n_with_random(100, 10 ** 4)
        self.c = self.__array_from_1_to_n_with_random(1000, 10 ** 5)
        self.d = self.__array_from_1_to_n_with_random(10000, 10 ** 6)

    def __array_from_1_to_n_with_random(self, n, k):
        a = [i + 1 for i in range(k)]
        for _ in range(n):
            num = random.randint(0, k - 1)
            a[num] = random.randint(0, 999)
        return a


class TestsGroup6:  # Массивы с большим количеством повторений одного элемента (10%, 25%, 50%, 75% и 90%)
    def __init__(self):
        self.a = self.__array_with_repeats(0.10, 10 ** 3)
        self.b = self.__array_with_repeats(0.25, 10 ** 3)
        self.c = self.__array_with_repeats(0.5, 10 ** 3)
        self.d = self.__array_with_repeats(0.75, 10 ** 3)
        self.e = self.__array_with_repeats(0.90, 10 ** 3)

        self.a1 = self.__array_with_repeats(0.10, 10 ** 4)
        self.b1 = self.__array_with_repeats(0.25, 10 ** 4)
        self.c1 = self.__array_with_repeats(0.5, 10 ** 4)
        self.d1 = self.__array_with_repeats(0.75, 10 ** 4)
        self.e1 = self.__array_with_repeats(0.90, 10 ** 4)

        self.a2 = self.__array_with_repeats(0.10, 10 ** 5)
        self.b2 = self.__array_with_repeats(0.25, 10 ** 5)
        self.c2 = self.__array_with_repeats(0.5, 10 ** 5)
        self.d2 = self.__array_with_repeats(0.75, 10 ** 5)
        self.e2 = self.__array_with_repeats(0.90, 10 ** 5)

        self.a3 = self.__array_with_repeats(0.10, 10 ** 6)
        self.b3 = self.__array_with_repeats(0.25, 10 ** 6)
        self.c3 = self.__array_with_repeats(0.5, 10 ** 6)
        self.d3 = self.__array_with_repeats(0.75, 10 ** 6)
        self.e3 = self.__array_with_repeats(0.90, 10 ** 6)

    def __array_with_repeats(self, n, k):
        a = [random.randint(0, 999) for _ in range(k)]
        num = random.choice(a)
        for i in range(int(len(a) * n)):
            a[i] = num
        random.shuffle(a)
        return a
