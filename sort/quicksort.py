#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: zzwwsun

lst = [3,1,5,9,4,7,2,0,]

def quicksort(lst):

    if len(lst) < 2:
        return lst

    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i <= pivot]
        bigger = [i for i in lst[1:] if i >= pivot]
        return quicksort(less)+[pivot]+quicksort(bigger)

print(quicksort(lst))