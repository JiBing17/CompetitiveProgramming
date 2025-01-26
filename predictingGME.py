# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# https://chat.openai.com/share/55c5b6e5-e1bc-4802-b3b5-45a9176a2a74 - link to chat history

# import sys for better memory usage
import sys

def max_profit(predictions):
    
    n = len(predictions)
    if n < 2:
        return 0
    
    # possible choices
    hold_stock = -predictions[0]  
    no_stock = 0  
    sold = 0  
    
    for i in range(1, n):
        
        # maximum profit if we hold the stock
        new_hold_stock = max(hold_stock, no_stock - predictions[i])
        
        # maximum profit if we don't hold the stock
        new_no_stock = max(no_stock, sold)
        
        # maximum profit if we sold the stock
        new_sold = hold_stock + predictions[i]

        hold_stock = new_hold_stock
        no_stock = new_no_stock
        sold = new_sold
    return max(no_stock, sold)

n = int(sys.stdin.readline().strip())  
predictions = list(map(int, sys.stdin.readline().strip().split()))  
print(max_profit(predictions))
