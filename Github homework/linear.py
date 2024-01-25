def Linear():
    import random
    rand = sorted([random.randint(-10, 10) for i in range(10)])
    print(rand)
    num = int(input('Введите число: '))

    def LinearSearch(rand, num):
        for i in range(len(rand)):
            if rand[i] == num:
                return i
        return -1

    print(f'Введенное число находится на {LinearSearch(rand, num)} позиции')


Linear()
