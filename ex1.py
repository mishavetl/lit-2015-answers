#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import random

def smallest(l):
    if len(l) > 1:
        n = l[0]
        del l[0]

        if n < l[0]:
            l[0] = n

        return smallest(l)

    else:
        return l[0]


if __name__ == "__main__":
    print("Type range of random: ( You can use default - just press enter)") 
    n1 = input()

    if n1 == "":
        n1 = 0
        n2 = 10000

    else:
        n1 = int(n1)
        n2 = int(input())

    print(smallest([random.randint(n1, n2), \
                    random.randint(n1, n2), \
                    random.randint(n1, n2), \
                    random.randint(n1, n2)
                ]
            )
        )
    
    input()


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
