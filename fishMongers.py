# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

def main():

    # first lines gives you number of fish and number of fishMongers
    temp = sys.stdin.readline().strip().split()

    numOfFishes  = int(temp[0])
    numOfMongers = int(temp[1])

    # an array of arrays that will store the data for each fishMonger
    fishMongers = []

    # intial earnings
    earnings = 0
    
    # fishes array that contains the weight of each fish caught read from the second line
    fishes = sys.stdin.readline().strip().split()

    # type cast all weight into integers
    for i in range(len(fishes)):
        fishes[i] = int(fishes[i])
    
    # sort weight in descending order so we can sell the heaviest fish to the fishMonger that will pay the most per kilo
    fishes.sort(reverse = True)

    # goes through each of the fish mongers data line by line
    for i in range(numOfMongers):

        # stores into temp array
        temp = sys.stdin.readline().strip().split()

        # typecast into integers (num of fishes willing to buy and money per kilo respectively)
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])

        # add array to the fishMongers array
        fishMongers.append(temp)

    # sort by money per kilo that fishMonger would buy fish for
    fishMongers = sorted(fishMongers, key = lambda x: x[-1], reverse = True)

    # index needed to keep track of the current fishMonger we are on (start = 0)
    currentMonger = 0

    # var for keeping track num of mongers
    numOfMongers = len(fishMongers)


    # goes through each fish from biggest kilo to smallest since sorted
    for i in range(len(fishes)):

        # fish kilo of current fish
        fishKilo = fishes[i]

        # earnings updates by fish kilo multiplied my money per kilo of current fishMonger (also sorted in descedning order to get max profit)
        earnings += fishKilo * fishMongers[currentMonger][1]

        # update number of fish that current fish Monger is willing to buy
        fishMongers[currentMonger][0] -= 1

        # if current fishMonger is satisfied and reached his / her buy limit, move on to next fishMonger with the next highest price per kilo of fish
        if fishMongers[currentMonger][0] == 0:
            currentMonger += 1

            # break out of for loop if index is invalid (out of mongers)
            if currentMonger == numOfMongers:
                break
        
        

    # prints total earnings at end 
    print(earnings)
        
main()