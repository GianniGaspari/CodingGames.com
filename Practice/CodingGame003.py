import sys
import math


while True:
    max_h = 0
    for i in range(8):
        mountain_h = int(input())
        if mountain_h > max_h:
            max_h = mountain_h
            fire = i
    print(fire)