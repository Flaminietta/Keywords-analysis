#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========================================================
Get the frequency of any n-gram (composition of n-words)
========================================================

"""

from itertools import tee, islice

def ngrams(lst, n):
  tlst = lst
  while True:
    a, b = tee(tlst)
    l = tuple(islice(a, n))
    if len(l) == n:
      yield l
      next(b)
      tlst = b
    else:
      break

