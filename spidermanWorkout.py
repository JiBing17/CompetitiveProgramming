# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

import numpy as np

def main():
    numCases = int(sys.stdin.readline().strip())
    for i in range(numCases):

        numBuildings = int(sys.stdin.readline().strip())
        heights = sys.stdin.readline().strip().split()

        for i in range(len(heights)): 
            heights[i] = int(heights[i])

        totalHeight = sum(heights)

        dp = [[totalHeight + 1 for i in range(numBuildings)] for j in range(totalHeight+1)]
        # inital height
        dp[heights[0]][0] = heights[0]

        for i in range(1, numBuildings):
            for j in range(totalHeight):
                
                # above ground and at position of prev building going up to here (keep track of max height at that point)
                if j - heights[i] >= 0 and dp[j - heights[i]][i-1] != totalHeight + 1:
                    dp[j][i] = max(j, dp[j- heights[i]][i-1])

                # not over max height (want min path between going up and going down)
                if j + heights[i] <= totalHeight:
                    dp[j][i] = min(dp[j][i],dp[j + heights[i]][i-1])

        path = ""
        currHeight = 0

        # wasn't able to reach end at position 0
        if dp[0][-1] == totalHeight + 1:
            path = "IMPOSSIBLE"
            print(path)
            continue

        # total min of max path getting to destination
        mh = dp[0][-1] 

        # backtracking (until 1st building)
        for i in range(numBuildings - 1, 0, -1):
            
            # above ground going up to reach current ith building (going up was the optimal path)
            if currHeight - heights[i] >= 0 and dp[currHeight - heights[i]][i-1] <= mh:

                # update max height and current height for next iteration back
                mh = dp[currHeight - heights[i]][i-1]
                currHeight = currHeight - heights[i]
                path += "U"

            # case where going down to reach the ith building was optimal path
            else:
                currHeight = currHeight + heights[i]
                path += "D"
        
        # always up for first move
        path += "U"
        
        # reverse path taken since we backtracked
        path = path[::-1]
        print(path)
        

main()