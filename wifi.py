# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

def main():

    # can function
    def isReachable(distance, houses):

        # radius of point
        totalRange = distance + distance
        
        # aways place one
        signal = houses[0] + totalRange
        numOfPoints = 1

        for i in range(1, len(houses)):
            # need another access point
            if not houses[i] <= signal:
                numOfPoints += 1
                signal = houses[i] + totalRange
        
        return numOfPoints

    numOfCases = int(sys.stdin.readline().strip())

    for i in range(numOfCases):
        temp = sys.stdin.readline().strip().split()
        numOfAccessPoints = int(temp[0])
        numOfHouses = int(temp[1])
        houses = []
        for j in range(numOfHouses):
            houses.append(int(sys.stdin.readline().strip()))
        houses.sort()

        # binary search on max radius of access point to pass in for can function
        left = 0
        right = 10000000

        for i in range(50):

            mid = left + (right - left) / 2
            pointsUsed = isReachable(mid, houses)

            # smaller radius if we use less or equal access points 
            if pointsUsed <= numOfAccessPoints:
                right = mid 
            else:
                left = mid
        
        print(f'{mid:.1f}')

main()