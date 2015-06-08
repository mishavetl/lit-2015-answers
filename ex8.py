#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

def smaller(n):
    "возвращает самое близкое значение которое меньше 'n' из его цифр"
    i = -2

    n = list(str(n))

    for _ in range(len(n)):
        if n[i + 1] < n[i]:
            n_bak = n[i]

            n[i] = n[i + 1]
            n[i + 1] = n_bak

            break

        i -= 1

    return ''.join(n)


def bigger(n):
    "возвращает самое близкое значение которое больше 'n' из его цифр"
    for i in range(



if __name__ == "__main__":
    print("n1 n2 n3 n4")
    l = [int(x) for x in input().split()] # List comprehension
                                        # считывает входные данные и переводит их в тип integer

    print(smaller(l))

    input()


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
