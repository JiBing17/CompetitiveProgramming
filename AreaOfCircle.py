# Author: Ji Bing Ni
# It is not okay to share my code for anonymously for educational purposes

import math
def main():
 
        while (True):

            temp = input().strip().split()

            # typecasted string numbers to float numbers
            radius = float(temp[0])
            totalDots  = float(temp[1])
            dotsInCircle = float(temp[2])

            # end case
            if radius == 0.0 and totalDots == 0.0 and dotsInCircle == 0.0:
                return
            
            # area of circle
            area = math.pi * (radius * radius)

            # diamter is 2 times the radius
            diameter = 2 * radius

            # width and length is same and diameter is length of square
            squareArea = diameter * diameter

            # area of circle calculation 
            area = math.pi * (radius * radius)

            # estimatedArea calculation
            estimatedArea = (dotsInCircle / totalDots) * squareArea
            
            # prints the results
            print(area, estimatedArea)

main()