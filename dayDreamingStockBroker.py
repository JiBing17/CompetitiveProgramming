# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

def main():

    # number of days we can travel back (first line == d)
    numOfDaysBefore = int(sys.stdin.readline().strip())

    # inital money we start with 
    money = 100
    
    # array to store all prices in array
    prices = []

    # read each following line and append price onto the array of prices (for checking adjacent day prices)
    for i in range(numOfDaysBefore):

        price = int(sys.stdin.readline().strip())
        prices.append(price) 
    
    
    # iterates through each day for oldest to newest
    for i in range(len(prices) -1):
        
        # if we are able to buy and prices is less than tmr
        if prices[i] <= money and prices[i] < prices[i+1]:

            # limit of shares can only be less than 100000
            sharesGained = min(money // prices[i], 100000)
            # update money from shares bought
            money -= sharesGained * prices[i]
            # update money from selling the shares for the next day
            money += sharesGained * prices[i+1]
        
    # print the total earnings we have gained after the iteration ends
    print(money)
            
main()