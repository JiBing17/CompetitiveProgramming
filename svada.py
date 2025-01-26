# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

def main():

    totalTime = int(sys.stdin.readline().strip())
    nMonkeys = int(sys.stdin.readline().strip())

    nMonkeyStats = []
    # storing info for first type of monekys (start time / num produced per time)
    for i in range(nMonkeys):
        temp = sys.stdin.readline().strip().split()
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        nMonkeyStats.append(temp)

    mMonkeys = int(sys.stdin.readline().strip())
    mMonkeyStats = []
    # storing info for second type of monekys (start time / num crack per time)
    for i in range(mMonkeys):
        temp = sys.stdin.readline().strip().split()
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        mMonkeyStats.append(temp) 
    
    left = 1
    right = totalTime
    
    # can function
    def isThereFood(time):
        totalProduction = 0
        for monkey in nMonkeyStats:
            # time left to produce
            startTime = time - monkey[0]
            totalProduction += max(0, startTime // monkey[1] + 1)

        totalCracked = 0
        for monkey in mMonkeyStats:
            # time left to crack
            startTime = totalTime - (time + monkey[0])
            totalCracked += max(0, startTime // monkey[1] + 1)

        return totalProduction <= totalCracked
    
    # binary search answer as input for can function
    while left < right:
        mid = left + (right - left + 1) // 2
        boolean = isThereFood(mid)

        # produced too little (more time for type a)
        if boolean:
            left = mid
        else:
            right = mid - 1
            
    minTime = left
    print(minTime) 

main()