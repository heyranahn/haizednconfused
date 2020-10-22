import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def diagonals_spiral_sum(sizeofspiral):
    
    #we want to find only the sum of the diagonals in the spiral
    #...the spiral's diagonals are odd and also squared
    
    #501^2 (squared)
    max_size_of_spiral = 251001
    
    #because diagonals are odd, creating odd number list
    odd_nums = range(1,max_size_of_spiral+1,2)
    
    #counter for the space of the corners (4)
    space = 1

    #counter
    i = 0

    #start at 1
    total = 1
    
    #while loop that uses counter & iterates until the odd number
    # ...list is not equal to the maximum size of spiral
    while odd_nums[i] != max_size_of_spiral:
        for x in range(4):
            i += space
            total += odd_nums[i]
        space += 1
    return total

#should be 83960501
print(diagonals_spiral_sum(501))