# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

def main():

    temp = sys.stdin.readline().strip().split()

    # n and m
    numOfPaintSizes = int(temp[0])
    numOfNeededSize = int(temp[1])

    # arrays used to store info (store sizes and what size we need)
    sizes = []
    neededSizes = []

    # store sizes in shop to size array
    for i in range(numOfPaintSizes):
        size = int(sys.stdin.readline().strip())
        sizes.append(size)

    # vars for checking extra amount
    perfectSize = 0
    actualSize = 0

    # store sizes needed to another array
    for i in range(numOfNeededSize):
        size = int(sys.stdin.readline().strip())
        perfectSize += size
        neededSizes.append(size)    
    
    sizes.sort()
    neededSizes.sort()

    # goes through each needed size and performs binary search on store sizes
    for i in range(len(neededSizes)):

        # out of bounds index to start
        index = 100000

        # binary search for number
        left = 0
        right = len(sizes) - 1
        
        while left < right:

            mid = left + (right - left) // 2
            
            if sizes[mid] == neededSizes[i]:
                index = mid
                break

            elif sizes[mid] < neededSizes[i]:
                left = mid + 1

            else:
                right = mid - 1
        
        # if number not found, change to the closest number to it
        if index == 100000:
            index = left

        # gets the next size bigger than size needed (case if target size is smaller)
        while sizes[index] < neededSizes[i]:
            index += 1

        # gets the next size bigger than size needed (case if target size is already bigger)
        while sizes[index] > neededSizes[i] and index != 0 and sizes[index - 1] > neededSizes[i]:
            index -= 1
        
        # update actual size that we got
        actualSize += sizes[index]

    print(actualSize - perfectSize)

main()