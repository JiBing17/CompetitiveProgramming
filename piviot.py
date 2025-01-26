# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

def main():
    n = int(sys.stdin.readline().strip())
    temp = sys.stdin.readline().strip().split()
    lowest = []
    biggest = []
    low = int(temp[len(temp) - 1])
    big = int(temp[0])

    # intial values for array
    lowest.append(low)
    biggest.append(big)

    # biggest number at ith postion going forwards
    for i in range(1, len(temp)):
        num = int(temp[i])
        big = max(num, big)        
        biggest.append(big)
    
    # lowest number at ith position going backwards
    for i in range(len(temp) - 2, -1, -1):
        num = int(temp[i])
        low = min(num, low)
        lowest.append(low)
    
    # reverse so we access the correct indices
    lowest.reverse()
    counter = 0

    for i in range(len(temp)):
        currIndex = i
        num = int(temp[i])
        # first index case
        if currIndex == 0 and num < lowest[currIndex + 1]:
            counter += 1
        # last index case
        elif currIndex == len(temp) - 1 and num > biggest[currIndex - 1 ]:
            counter += 1
        elif num > biggest[currIndex - 1] and num < lowest[currIndex + 1]:
            counter += 1

    print(counter)


main()