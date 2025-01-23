# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import bisect
import sys

def main():

    temp = sys.stdin.readline().strip().split()
    n = int(temp[0])
    h = int(temp[1])
    
    stalagmites = []
    stalactites = []
    
    # var used to keep track of stalagmites or stalactites
    counter = 0

    # fill both arrays with their corresponding heights
    for i in range(n):

        height  = int(sys.stdin.readline().strip())

        if counter % 2 == 0:
            stalagmites.append(height)
        else:
            stalactites.append(height)

        counter += 1


    # sort stalagmites in descending order
    stalagmites.sort()

    # subract height by stalactities (up bars) for checking hit purposes (sort at end of loop)
    for i in range(len(stalactites)):
        stalactites[i] = h - stalactites[i]
    stalactites.sort()

    
    hits = 0

    # minHits start as some arbitrary big number
    minHits = 10000000000
    count = 0

    # tries each height from 1 to 7 (1 = .5 , 2 = 1.5, ...)
    for i in range(1,h + 1):
        
        hits = 0

        # index of where that height would be inserted in the sorted stalagmites array 
        indexOfInsert = bisect.bisect_left(stalagmites, i)

        # every thing after that we would hit.
        hits += len(stalagmites) - indexOfInsert

        # do similar thing for the top 
        indexOfInsert = bisect.bisect_left(stalactites, i)
        
        # since upside down, everything before index we would hit
        hits += indexOfInsert

        if hits == minHits:
            count += 1

        if hits < minHits:
            count = 1
            minHits = hits
        
    print(minHits, count)

main()