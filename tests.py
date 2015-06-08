#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import ex1, ex2, ex4, ex5, ex6, ex7, ex8
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

# Ex1

def test_ex1_smallest_with_small_numbers():
    eq_(ex1.smallest([1, 2, 3, 4, 5]), 1)

def test_ex1_smallest_with_big_numbers():
    eq_(ex1.smallest([2382328, 999999, 21222, 1111]), 4)

# Ex2

def test_ex2_count_with_two_positive_numbers():
    eq_(ex2.count(["1", "4"]), 0)

def test_ex2_count_with_two_negative_numbers():
    eq_(ex2.count(["-1", "-224"]), 0)

def test_ex2_count_with_two_negative_and_two_positive_numbers():
    eq_(ex2.count(["-1", "1", "-224", "2"]), 3)

# Ex3

####

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


# Ex6

def test_ex6_biggest():
    eq_(ex6.biggest([1, 5, 5, 9, 0]), 4)

def test_ex6_biggest2():
    eq_(ex6.biggest([92828, 999, 78563, 555559, 1111111111]), 5)

# Ex7

#def test_ex7_main():
    #eq_(ex7.main(["1", "5", "5", "9", "0"]), 4)

#def test_ex7_main2():
    #eq_(ex7.main(["92828", "999", "78563", "555559", "1111111111"]), 4)

#def test_ex7_main3():
    #eq_(ex7.main(["144", "5", "258", "1345", "7", "258", "1", "144", "6"]), 4)

def test_ex7_divide_list():
    eq_(ex7.divide_list([1, 2, 5, 3, 6]), [[1, 2], [3, 6]])

def test_ex7_divide_list2():
    eq_(ex7.divide_list([828, 2201013, 10010023, 383848 , 222]), [[828, 2201013], [383848 , 222]])

# Ex8

def test_ex8_sort_l():
    eq_(ex8.sort_l([7, 9, 1, 3, 90, 1, 345, 0, 50]), [0, 1, 1, 3, 7, 9, 50, 90, 345])

def test_ex8_sort_l1():
    eq_(ex8.sort_l([7, 1, 10, 3, 5]), [1, 3, 5, 7, 10])

def test_ex8_smaller():
    eq_(ex8.smaller(["1", "9", "5"]), "159")

def test_ex8_bigger():
    eq_(ex8.bigger(["1", "9", "5"]), "519")


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
