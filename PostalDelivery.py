# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

def main():

    temp = sys.stdin.readline().strip().split()

    # vars needed to store data from stdin
    numOfRoutes = int(temp[0])
    maxCapacity = int(temp[1])

    # var used to check the current amount we have (same as max capacity at start)
    currentAmount = maxCapacity

    # total distance starts at 0
    totalDistance = 0

    # 2 arrays for array for storing both distance to get there and capacity number each station takes
    negativeArray = []
    positiveArray = []
   
    # loop used to store the data in it's appropirate array
    for i in range(numOfRoutes):

        # temp array to store data
        temp = sys.stdin.readline().strip().split()

        # get distance / value for the ith station
        distance = int(temp[0])
        value = int(temp[1])

        # another temp array to store distance / value and append to it's appropriate array
        temp2 = []

        # negative array case
        if distance < 0:
            temp2.append(distance)
            temp2.append(value)
            negativeArray.append(temp2)
        # positive array case
        else:
            temp2.append(distance)
            temp2.append(value)
            positiveArray.append(temp2)

    # treat negative array as postive
    for i in range(len(negativeArray)):
        negativeArray[i][0] = -1 * negativeArray[i][0]

    # sort both arrays in descending order
    negativeArray = sorted(negativeArray, key = lambda x: x[0], reverse = True)
    positiveArray= sorted(positiveArray, key = lambda x: x[0], reverse = True)

    """  print("n")
    for element in negativeArray:
        print(element)

    print("p")
    for element in positiveArray:
        print(element) """
    
    # index used
    nIndex = 0
    pIndex = 0

    while nIndex != len(negativeArray):

        currentAmount = maxCapacity
        totalDistance += 2 * negativeArray[nIndex][0]  
        
        if currentAmount >= negativeArray[nIndex][1]:

            currentAmount -= negativeArray[nIndex][1]
            nIndex += 1

            while currentAmount != 0 and nIndex != len(negativeArray):

                if currentAmount >= negativeArray[nIndex][1]:
                    currentAmount -= negativeArray[nIndex][1]
                    nIndex += 1 
                else:
                    negativeArray[nIndex][1] -= currentAmount
                    currentAmount = 0
            
                
        else:
            negativeArray[nIndex][1] -= currentAmount
            currentAmount = 0
        
            
    while pIndex != len(positiveArray):

        currentAmount = maxCapacity
        totalDistance += 2 * positiveArray[pIndex][0]  
        
        if currentAmount >= positiveArray[pIndex][1]:

            currentAmount -= positiveArray[pIndex][1]
            pIndex += 1

            while currentAmount != 0 and pIndex != len(positiveArray):

                if currentAmount >= positiveArray[pIndex][1]:
                    currentAmount -= positiveArray[pIndex][1]
                    pIndex += 1 
                else:
                    positiveArray[pIndex][1] -= currentAmount
                    currentAmount = 0
            
                
        else:
            positiveArray[pIndex][1] -= currentAmount
            currentAmount = 0
        

    print(totalDistance)

main()