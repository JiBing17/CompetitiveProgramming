# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes


# import sys for better memory usage
import sys

def min_days_to_retire(n, M, investments):
    
    # bounds for BSTA
    left = 1
    right = 10**10
    
    while left < right:
    
        mid = left + (right - left) // 2 
        bool = canRetire(mid, n, M, investments)
        
        # adjust bounds for a smaller day
        if bool:
            right = mid
        # adjust bounds for a bigger day
        else:
            left = mid + 1

    return left

# can function used to see if we can retire given a certain day 
def canRetire(days, n, M, investments):
    
    valid = []
    for money, cost in investments:
        
        # valid investment bank where we can break even given d days
        if cost  <= days * money:
            valid.append((money, cost))
            
    totalCost = 0
    profit = 0
    
    # calculate cost for each valid bank and profit made 
    for m, c in valid:
        totalCost += c
        profit += m * days
    
    # true if we still have more than enough to retire given M 
    remainder =  profit - totalCost
    return remainder >= M
    
n, M = map(int, sys.stdin.readline().strip().split())
investments = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
print(min_days_to_retire(n, M, investments))
