#!/usr/bin/env python

i = iter('(){}[]<>')  # iterative parenthesis
p = dict(zip(i, i))   # create dictionary from i's tuples
c = p.values()


def balancer(input):
    s = []            # stack
    return s
