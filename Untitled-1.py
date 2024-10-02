#!/bin/python3

import math
import os
import random
import re
import sys

teste= int(0)

if __name__ == '__main__':
    n = int(input().strip())
    try:
        teste = str(n/2)
        teste = int(teste)
    except ValueError:
        print("Weird")
    else:
        teste= int(n)
        if n < 6:
            print("Not Weird")
        if n > 6 and n < 20:
            print("Weird")
        if n > 20:
            print("Not Weird")