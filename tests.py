#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import ex1, ex2, ex4, ex5
from nose.tools import eq_

# Utils

def test_utils_what_symb_with_minus1():
    eq_(ex2.what_symb(-23321), "-")

def test_utils_what_symb_with_minus2():
    eq_(ex2.what_symb(-99999), "-")

def test_utils_what_symb_with_plus1():
    eq_(ex2.what_symb(999992), "+")

def test_utils_what_symb_with_plus2():
    eq_(ex2.what_symb(1), "+")

def test_ex1_smallest_with_small_numbers():
    eq_(ex1.smallest([1, 2, 3, 4, 5]), 1) 

def test_ex1_smallest_with_big_numbers():
    eq_(ex1.smallest([2382328, 999999, 21222, 1111]), 1111) 

def test_ex1_smallest_with_return_index_True():
    eq_(ex1.smallest([238328, 999999, 21222, 1111], r_i=True), [1111, 3]) 

# Ex2

def test_ex2_count_with_two_positive_numbers():
    eq_(ex2.count(["1", "4"]), 0)

def test_ex2_count_with_two_negative_numbers():
    eq_(ex2.count(["-1", "-224"]), 0)

def test_ex2_count_with_two_negative_and_two_positive_numbers():
    eq_(ex2.count(["-1", "1", "-224", "2"]), 3)

# Ex3

###


# Ex4

def test_ex4_count_with_three_diffs():
    eq_(ex4.count(["1", "65", "20"], []), 3)

def test_ex4_count_with_three_same():
    eq_(ex4.count(["1", "1", "1"], []), 1)

def test_ex4_count_with_two_same_and_three_diffs():
    eq_(ex4.count(["1", "2", "1", "5", "3"], []), 4)


# Ex5

def test_ex5_main():
    eq_(ex5.main(["88", "-22", "5", "6", "-93"]), "-")

def test_ex5_main():
    eq_(ex5.main(["0", "22", "-7", "6", "93"]), "+")

def test_ex5_plus_list1():
    eq_(ex5.plus_list(["88", "-22", "5", "6", "-93"]), -16)

def test_ex5_plus_list2():
    eq_(ex5.plus_list(["0", "22", "-7", "6", "93"]), 114)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
