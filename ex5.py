#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

from utils import what_symb

def plus_list(l, i=0, n=0):
    return plus_list(l, i + 1, n + int(l[i])) if len(l) > i else n

def main(l):
    return what_symb(plus_list(l))

if __name__ == "__main__":
    print("Type numbers separated by space:") 
    l = input().split()

    print(main(l))

    input()


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
