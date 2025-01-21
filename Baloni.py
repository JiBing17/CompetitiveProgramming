# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes
# Kattis Week-2

# import sys for better memory usage
import sys

def main():
    
    # read first line for the n number of ballons in the next line
    firstLine = int(sys.stdin.readline().strip())

    # array to keep track of different heights of ballons that have been popped (0 for not popped and anything else for popped)
    array = [0 for i in range(10000000)]

    # store the height of ballons in an array of size n
    temp = sys.stdin.readline().strip().split()

    # set currentHeight equal to height after popping first ballon 
    currentHeight = int(temp[0]) - 1

    # add one to the height of the arrow after popping the first ballon
    array[currentHeight] += 1

    # intial shot is 1 (shot at first ballon height)
    arrowsShot = 1
    
    # iterates through each height of the following balloons after the first one
    for i in range(1,len(temp)):

        # if popped, add one to height of balloon after pop
        if array[int(temp[i])] > 0:
            
            array[int(temp[i]) - 1] += 1
            
            array[int(temp[i])] -= 1

            # skip to next balloon
            continue

        else:
            # case where our arrow cant reach height, so we shoot new arrow and add 1 to the height of updated balloon height for future iterations 
            arrowsShot += 1
            currentHeight = int(temp[i]) - 1

            array[currentHeight] += 1


    # prints the number of arrows shot after popping all balloons
    print(arrowsShot)

main()
