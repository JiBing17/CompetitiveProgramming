# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

def main():

    numTrains = int(sys.stdin.readline().strip())

    if numTrains == 0:
        print("0")
        return

    # LIS dp array
    dp = [1 for i in range(numTrains)]
    weights = []

    for i in range(numTrains):
        weights.append(int(sys.stdin.readline().strip()))

    # LIS   
    for i in range(numTrains- 1, -1, -1):
        for j in range(i+1,numTrains):
            # weight is bigger than the current jth weight
            if weights[j] < weights[i]: 
                # update current ith length
                dp[i] = max(dp[i], 1 + dp[j])

    # LDS dp array
    dp2 = [1 for i in range(numTrains)]

    # LDS
    for i in range(numTrains -1, -1, -1):
        for j in range(i+1, numTrains):
            # weight is smaller than the current jth weight
            if weights[j] > weights[i]: 
                # update current ith length 
                dp2[i] = max(dp2[i], 1 + dp2[j])
    
    sizes = []
    
    # find max by comparing each column in the two dp arrays
    for num in dp2:
        index = dp2.index(num)
        num2 = dp[index]
        sum = num2 + num
        sizes.append(sum)

    
    print(max(sizes) -1)
    
main()