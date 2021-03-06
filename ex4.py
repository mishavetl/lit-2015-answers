#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

def count(l, lc, i=0, acc=0):
    if len(l) == i:
        return acc
    
    n = l[i]

    if n not in lc:
        lc.append(n)
        acc += 1
    
    return count(l, lc, i + 1, acc)


if __name__ == "__main__":
    print("Type numbers separated by space:") 
    l = input().split()

    print(count(l, []))

    input()


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
