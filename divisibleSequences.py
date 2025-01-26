# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

import numpy as np
import math

def main():
    numOfTest = int(sys.stdin.readline().strip())
    for i in range(numOfTest):

        temp = sys.stdin.readline().strip().split()
        divider = int(temp[0])
        numOfSequence = int(temp[1])
        sequences = sys.stdin.readline().strip().split()

        counter = 0
        prefixSum = []
        prefixSum.append(0)
        total = 0

        for i in range(numOfSequence):
            total += int(sequences[i])
            prefixSum.append(total)
        
        bins = [[]]
        remainders = {}

        # put prefix sums that have same remainder in same bin
        for num in prefixSum:
            r = num % divider

            if r in remainders:
                for i in range(1,len(bins)):
                    if bins[i][0] % divider == r:
                        bins[i].append(num)
                
            else:
                remainders[r] = r
                bins.append([num])

        # length choose 2 and add to counter
        for bin in bins:
            length = len(bin)
            counter += math.comb(length, 2)

        print(counter)     
main()