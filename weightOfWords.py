# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

def main():

    temp = sys.stdin.readline().strip().split()
    length = int(temp[0])
    weight= int(temp [1])

    # check if weight is either too big or too small
    if weight > length * 26 or weight < length:
        print("impossible")
        return
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    letter = weight // length
    r = weight % length
    currentTotal = 0
    # will contain the letter needed to fill out length - 1 spaces
    chosenLetters = []

    # if remainder, distribute to the letters appropriately
    for i in range(length - 1):
        if r:     
            currentTotal += letter + 1
            chosenLetters.append(letter + 1)
            r -= 1
        else:
            currentTotal += letter
            chosenLetters.append(letter)
    # last letter needed 
    remainder = weight - currentTotal
    string = ""
    lastLetter = letters[remainder - 1]

    # make word with the letters chosen plus last letter
    for i in range(length - 1):
        string += letters[chosenLetters[i] - 1]
    string += lastLetter
    print(string)
    


main()