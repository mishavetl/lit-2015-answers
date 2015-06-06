#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

from utils import what_symb

def count(l, i=0, acc=0):
    if len(l) == i + 1:
        return acc

    if what_symb(int(l[i])) != what_symb(int(l[i+1])):
        acc += 1
    
    return count(l, i + 1, acc)


if __name__ == "__main__":
    print("Type temperatures separated by space:") 
    l = input().split()

    print(count(l))
    input()


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
