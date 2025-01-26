# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# Teammate: Youngjun Yoo

# import sys for better memory usage
import sys
import numpy as np


def main():

    for line in sys.stdin:

        temp = line.strip().split()
        choices = int(temp[0])
        length = int(temp[1])
        totalCombinations = 1

        # denominator: k choices for each spot (k*k*k..)
        for i in range(length):
            totalCombinations *= (choices + 1)

        # state: how many ways to end on that number for that given length
        dp = [ [0 for i in range(choices + 3)] for j in range(length) ] 
        
        # + 3 to add 2 borders on top left and top right (-1 for border)
        for i in range(choices + 3):
            if i == 0 or i == choices + 2:
                dp[0][i] = -1
            # start at 1 for each ending of length 1
            else:
                dp[0][i] = 1

        # column borders
        for i in range(length):
            dp[i][0] = -1
 
        for i in range(1, length):
            for j in range(1, choices + 2):
                # out of bounds
                if dp[i - 1][j - 1] == -1:
                    topLeft = 0
                else:
                    topLeft = dp[i - 1][j - 1]
                topTop = dp[i-1][j]
                # out of bounds
                if dp[i - 1][j + 1] == -1:
                    topRight = 0
                else:
                    topRight = dp[i - 1][j + 1]
                
                dp[i][j] = topLeft + topTop + topRight        
    
        validOnes = 0

        # add up all ways to end of on that num at ending length (skipping borders)
        for j in range(1, choices + 2):
            validOnes += dp[length - 1][j]

        # 9 decimal place format
        result = "{:.9f}".format((validOnes / totalCombinations) * 100)
        print(result)
    
main()