#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

def smaller(n):
    "возвращает самое близкое значение которое меньше 'n' из его цифр"
    i = -2

    for _ in range(len(n)):
        if n[i + 1] < n[i]:
            n_bak = n[i]

            n[i] = n[i + 1]
            n[i + 1] = n_bak

            break

        i -= 1

    return ''.join(n)


def sort_l(l):
    "сортирует список из чисел, не знаю как называется так как я сам до него дошел"
    len_l = len(l)

    for i in range(len_l):
        for j in range(len_l - i - 1):
            if int(l[j]) > int(l[j + 1]):
                l[j], l[j + 1] = l[j + 1], l[j] # Меняем местами

    return l

def bigger(n):
    "возвращает самое близкое значение которое больше 'n' из его цифр"
    n1 = int(n[0])
    n2 = int(n[1])

    n2_i = 1

    for i in range(1, len(n)):
        on_check = int(n[i])
        if n1 < on_check < n2:
            n2 = on_check
            n2_i = i

    n[n2_i] = str(n1)
    n[0] = str(n2)


    return n[0] + ''.join(sort_l(n[1:]))


if __name__ == "__main__":
    print("n")
    l = list(input)

    print("Меньше: ", smaller(l))
    print("Больше: ", bigger(l))

    input()


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
