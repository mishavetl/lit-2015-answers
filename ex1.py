#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import random

def smallest(l, i=0):
    print(l)
    print(i)
    if len(l) > i + 1:
        n = l[i]

        if n < l[i + 1]:
            l[i + 1] = n

        return smallest(l, i + 1)

    else:
        return l[i]


if __name__ == "__main__":
    print("n1 n2 n3 n4")
    l = input().split()

    print(smallest(l))

    input()


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
