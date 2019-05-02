#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())

def testing_number(n):
    if n%2 != 0:
        print('Weird')

    if n%2 == 0 and n in range(2, 6):
        print('Not Weird')

    if n%2 == 0 and n in range(6, 21):
        print('Weird')

    if n%2 == 0 and n > 20:
        print('Not Weird')
    return

testing_number(n)




if __name__ == '__main__':
    N = int(input())