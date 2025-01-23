# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

def main():
    
    # vars needed for sequence
    temp = sys.stdin.readline().strip().split()
    lengthOfSequence = int(temp[0])
    modNum = int(temp[1])
    multiplier = int(temp[2])
    additionConstant = int(temp[3])
    initialNum = int(temp[4])

    sequence = []
    
    # loop to create the sequence and store it in an array
    for i in range(lengthOfSequence):
        num = (multiplier * initialNum + additionConstant) % modNum
        sequence.append(num)
        initialNum = num


    numbersFound = 0

    # runs binary search for all the numbers in the created sequence
    for i in range(len(sequence)): 
        
        target = sequence[i]

        left = 0
        right = len(sequence) - 1

        while left <= right:

            mid = left + (right - left) // 2

            # if number found, add to numbers found var and go to next iteration
            if sequence[mid] == target:
                numbersFound += 1
                break

            elif sequence[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    
    print(numbersFound)   

main()