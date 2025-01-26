# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# https://chat.openai.com/share/84fc5b1f-b8a1-4048-8f3c-ff79ffdbb2b5 - chatgpt history

# import sys for better memory usage
import sys
import numpy as np

def min_total_cost(N, fees, dp):

    for j in range(1, N+1):
        for i in range(N, 0, -1):       
            minimum = float('inf')
            # going backward
            if i + j <= N:
                minimum = min(minimum, dp[i+j][j])
            # case going forward
            if i - j > 0 and j - 1 > 0:     
                minimum = min(minimum, dp[i-j][j-1])
            # update to optimal way
            dp[i][j] = min(dp[i][j], minimum + fees[i-1])
               
    optimalPrice = float('inf')
    for i in range(N, 0, -1):
        optimalPrice = min(dp[N][i], optimalPrice)
    return optimalPrice
   
N = int(sys.stdin.readline().strip())
fees = [int(sys.stdin.readline().strip()) for _ in range(N)]

# dp array with i being current block and j being prev jump height
dp = [[ float('inf') for i in range(N+1)] for j in range(N+1)]
# always jump to step 2
dp[2][1] = fees[1]

print(min_total_cost(N, fees, dp))
