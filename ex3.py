#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

class Point(object):
    """точка на графике"""
    def __init__(self, x, y):
        super(Point, self).__init__()

        self.x = int(x)
        self.y = int(y)

    def position(self):
        "возвращает координатную плоскость точкивозвращает координатную плоскость точки"

        # Точка находится в одной из четвертей

        if self.x > 0 and self.y > 0:
            return ('quarter', 1)

        elif self.x < 0 and self.y > 0:
            return ('quarter', 2)

        elif self.x < 0 and self.y < 0:
            return ('quarter', 3)

        elif self.x > 0 and self.y < 0:
            return ('quarter', 4)

        # Точка находится в начале координат

        elif self.x == 0 and self.y == 0:
            return ('origin')

        # Точка находится на одной из осей

        elif self.x == 0:
            return ('axis', 'y')

        elif self.y == 0:
            return ('axis', 'x')



def majority(n, x):
    "возвращает является ли 'x' большенством от 'n'"
    return n / 2 < x


def main(l):
    "возвращает в виде [сколько находится на оси ординат, сколько находится на 3 коорд. плоскости]"
    on_axis_y = 0
    on_quarter_3 = 0

    for point in l:
        if point.position() == ('quarter', 3):
            on_quarter_3 += 1

        elif point.position() == ('axis', 'y'):
            on_axis_y += 1

    return (on_axis_y, on_quarter_3)


if __name__ == "__main__":
    print("c1_x;c1_y c2_x;c2_y c3_x;c3_y c4_x;c4_y...")

    l = [Point(*p.split(";")) for p in input().split()] # Перебирает список и формирует в виде [[x, y], [x1, y1]]

    on_axis_y, on_quarter_3 = main(l)

    length = len(l)

    majority_axis_y = majority(length, on_axis_y)
    
    majority_quarter_3 = majority(length, on_quarter_3)

    print("Большенство на оси ординат: ", majority_axis_y)
    print("На третьей плоскости: ", majority_quarter_3)


# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 syntax=python
