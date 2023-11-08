def eratosphene(n):
    easy = [True] * (n + 1)
    p = 2
    while p**2 <= n:
        if easy[p]:
            for i in range(p**2, n + 1, p):
                easy[i] = False
        p += 1

    numbers = []
    for i in range(2, n + 1):
        if easy[i]:
            numbers.append(i)

    return numbers

limit = int(input("Введите натуральное число N: "))
numbers = eratosphene(limit)
print(f"Простые числа до {limit}: {numbers}")
