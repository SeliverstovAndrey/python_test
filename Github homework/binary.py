def Binary():
    import random
    rand = sorted([random.randint(-10, 10) for i in range(10)])
    print(rand)
    num = int(input('Введите число: '))

    def BinarySearch(rand, num):
        first = 0
        last = len(rand) - 1
        index = -1
        while (first <= last) and (index == -1):
            mid = (first + last) // 2
            if rand[mid] == num:
                index = mid
            else:
                if num < rand[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return index

    print(f'Введенное число находится на {BinarySearch(rand, num)} позиции')


Binary()
