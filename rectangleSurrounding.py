# Author: Ji Bing Ni
# It is not okay to share my code for anonymously for educational purposes
# Kattis Week-1

# import sys for less memory usage
import sys
import io
import numpy as np

# boolean used to check if it is first pass or not
first_pass = 1

# capture output
output = io.StringIO()

# size of the grid
size = (900, 900)

# numpy array initialized to 0
coordinates = np.zeros(size)

# var used to keep track of the number of squares
squares_covered = 0

# goes through each line in standard input
for line in sys.stdin:
    # store numbers in the line into numbers array
    numbers = line.split()

    # skips the first line
    if len(numbers) == 1:
        if first_pass:
            first_pass = 0
            continue

        else:
            # used sum function to get sum of function and increment squares covered by that amount
            squares_covered += int(np.sum(coordinates))
            # string typecast 
            answer = str(squares_covered)
            # print the answer
            print(answer)

            # rest the 2 vars for next iteration
            squares_covered = 0
            coordinates = np.zeros(size)
            continue
    else:
        # takes each element in coordinates and type cast them into ints and store as vars for calculation purposes
        x1 = int(numbers[0])
        y1 = int(numbers[1])
        x2 = int(numbers[2])
        y2 = int(numbers[3])
        # sets the targeted area in coordinates to 1
        coordinates[x1:x2, y1:y2] = 1