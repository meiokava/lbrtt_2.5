#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    a = tuple(map(int, input().split()))
    k = 0
    for i in range(1, len(a)):
        if k == 1:
            print(a[i], " ")
        if a[i - 1] == a[i]:
            k = 1
