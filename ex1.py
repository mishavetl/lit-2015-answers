#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

def smallest(l, i=0, i_min=0):
    if len(l) == i:
        return i_min + 1

    if l[i] < l[i_min]:
        i_min = i

    return smallest(l, i + 1, i_min)


if __name__ == "__main__":
    print("n1 n2 n3 n4")
    l = [int(x) for x in input().split()]

    print(smallest(l))

    input()


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
