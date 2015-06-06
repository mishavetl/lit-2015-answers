#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import random

def what_symb(n):
    return "+" if n >= 0 else "-"


def random_ints(n, f, t, acc):
    print(acc.append(random.randint(f, t)))
    print("acc: ", acc)
    return random_ints(n - 1, f, t, acc.append(random.randint(f, t))) if n > 0 else acc


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
