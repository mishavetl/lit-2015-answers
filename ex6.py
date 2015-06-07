#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

def biggest(l, i=0, i_max=0):
    if len(l) == i:
        return i_max + 1

    if l[i] > l[i_max]:
        i_max = i

    return biggest(l, i + 1, i_max)

if __name__ == "__main__":
    print("list of n numbers")
    l = [int(x) for x in input().split()]

    answer = biggest(l)

    print("Position: {0}\nNumber: {1}".format(answer, l[answer - 1]))

    input()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
