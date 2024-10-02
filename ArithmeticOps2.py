#!/bin/python3

import math
import os
import random
import re
import sys



def areweird(n):
    r = n%2
    
    if r != 0:

        print("Weird")
        return
    

    if n < 6:
        print("Not Weird")
        return
        
    if n <= 20:
        print("Weird")
        return  
    
    
    print("Not Weird")
    return


if __name__ == '__main__':
     n = int(input().strip())
     
     areweird(n)


