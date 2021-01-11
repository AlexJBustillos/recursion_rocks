# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.
import math
def find_max(l):
    if len(l) == 1:
        return l[0]
    if l[0] > find_max(l[1:]):
        return l[0]
    else:
        return find_max(l[1:]) 

print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45

def find(l, current_max = -math.inf):
    if len(l) == 0:
        return current_max
    
    if l[0] > current_max:
        new_current_max = l[0]
    else:
        new_current_max = current_max
    
    return find(l[1:], new_current_max)

print(find([1, 4, 45, 6, -50, 10, 2]))
