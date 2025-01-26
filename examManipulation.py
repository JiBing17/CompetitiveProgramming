# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

import numpy as np


def main():
    temp = sys.stdin.readline().strip().split()
    numOfStudents = int(temp[0])
    numOfProblems = int(temp[1])

    dp = [[0 for i in range(numOfProblems)] for j in range(numOfStudents)]

    for i in range(numOfStudents):
        answers = sys.stdin.readline().strip()

        j = 0
        for char in answers:
            if answers[j] == "T":
                dp[i][j] = 1
            j += 1
            
    for j in range(numOfStudents):
        pickedTrue = 0
        pickedFalse = 0
        if dp[j][0] == 0:
            pickedFalse += 1
        else:
            pickedTrue += 1
    lowestScore = min(pickedTrue, pickedFalse)


    for i in range(1, numOfProblems):
        pickedTrue = 0
        pickedFalse = 0
        for j in range(numOfStudents):
           

            if dp[j][i] == 0:
                pickedFalse += 1
            else:
                pickedTrue += 1

        low = min(pickedTrue, pickedFalse)

        lowestScore = max(lowestScore, low)
            
    print(lowestScore)
            

    #print(np.matrix(dp))

    

main()