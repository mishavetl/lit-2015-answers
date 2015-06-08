#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

def divide_list(l, acc=[]):
    len_l = len(l)

    return [l[:len_l / 2], l[-(len_l / 2):]]

# def main(l, i=0, i_rev=-1, acc=0):
#     print("i: ", i)
#     print("i_rev: ", i_rev)
#     print("acc: ", acc)
#     if -(i_rev) + i > len(l):
#         return acc
#
#     if l[i] != l[i_rev]:
#         acc += 1
#
#     else:
#         i_rev -= 1
#
#     return main(l, i + 1, i_rev, acc)

def main(l):
    i = 0
    x = -1
    acc = 0

    while -(i_rev) + i <= len(l):
        if find(l[1], l[0][i]):
            acc += 1

        else:
            x -= 1

    return acc

if __name__ == "__main__":
    print("list of n numbers")
    l = input.split()

    print(main(l))

    input()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
