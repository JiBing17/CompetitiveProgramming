# Author: Ji Bing Ni
# It is not okay to share my code for anonymously for educational purposes

def main():

        # reads first line for n upcomming lines
        firstLine = int(input().strip())

        # for loop based on the n number of lines
        for i in range(firstLine):
            
            # get next line from input and split each element into temp array
            temp = input().strip().split()

            # assigns correct variable from each index of temp array with typecast
            population = int(temp[0])
            rate = int(temp[1])
            food = int(temp[2])

            # copy of food each year for rest purposes
            foodEachYear = food

            # inital years survied
            surviedYears = 0

            # goes until world is out of food
            while food >= 0:
                
                # account for food eaten that year by the population
                food = food - population

                # end while loop when we no longer have enough food for everyone
                if food < 0:
                    break

                # new year, update population by rate
                population = population * rate

                # reset food for each year
                food = foodEachYear

                # add 1 to years survied
                surviedYears += 1
            
            # prints the total number of years the world has until its no longer sustainable
            print(surviedYears)

main()