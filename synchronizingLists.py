# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

def main():

    n = int(sys.stdin.readline().strip())

    # keeps iterating until we are at end of input (n = 0)
    while n != 0:
        
        originalFirstList = []
        firstList = []
        secondList = []
        
        # reads in values for the 2 lists
        for j in range(n * 2):
                
            num = int(sys.stdin.readline().strip())

            # num belongs in first list
            if j < n:
                
                firstList.append(num)
                originalFirstList.append(num)

            # num belongs to second list
            else:
                secondList.append(num)
            
            # sort to "synchronize"
            firstList.sort()
            secondList.sort()

        for k in range(len(originalFirstList)):

            # orginal number from input of first list
            num = originalFirstList[k]
            
            # get index of that number from sorted first list
            index = firstList.index(num)

            # use index to print value from second list
            print(secondList[index])

        print()

        n = int(sys.stdin.readline().strip())

main()