# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

def main():

    temp = sys.stdin.readline().strip().split()
    candies = int(temp[0])
    numOfChildren = int(temp[1])
    wantedCandies = []
    totalNeeded = 0

    # store candies needed in array as well as the sum 
    for i in range(numOfChildren): 
        candiesNeeded  = int(sys.stdin.readline().strip())
        wantedCandies.append(candiesNeeded)
        totalNeeded += candiesNeeded

    # give out lack of candies instead
    lackOfCandies = totalNeeded - candies
    angryness = 0
    kidsLeft = numOfChildren
    wantedCandies.sort()

    # instead of giving one by one, give each kid the running average
    for i in range(len(wantedCandies)):
        
        avg = lackOfCandies // kidsLeft
        # didn't go over angry level
        if avg <= wantedCandies[i] :
            angryness += avg*avg
            lackOfCandies -= avg
        # went over angry level of current children, update appropriately
        else:
            angryness += wantedCandies[i] * wantedCandies[i]
            lackOfCandies -= wantedCandies[i]
        kidsLeft -= 1
    print(angryness)
main()