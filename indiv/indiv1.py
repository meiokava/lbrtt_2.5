#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    a = tuple(map(int, input().split()))
    k = 0
    for ind, val in enumerate(a):
        if k == 1:
            print(val, " ")
        if a[ind - 1] == val:
            k = 1

