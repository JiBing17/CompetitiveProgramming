# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

# import sys for better memory usage
import sys

# global var to keep track of the different valid word combinations we can make
totalNumOfWords = 0

# helper function to check if word is a valid word with the given conditions
def isWordValid(word):

    # vars used for checking validness of word
    hasL = False
    consecutiveVowels = 0
    consecutiveConsonants = 0

    # array of all letters that are vowels
    vowels = ["A", "E", "I", "O", "U"]

    # array of all letters that are consonants
    consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

    # goes through each character in the word
    for char in word:

        # one check if it is L
        if char == "L":
            hasL = True

        # another check to see if character is consonant or vowel
        if char in vowels:

            # increment vowel streak
            consecutiveVowels += 1

            # reset consonant streak
            consecutiveConsonants = 0

        elif char in consonants:

            # increment consonant streak
            consecutiveConsonants += 1

            # reset vowel streak
            consecutiveVowels = 0

        # after each character, we check if we have gotten 3 in a row or not, if so return false
        if consecutiveVowels == 3 or consecutiveConsonants == 3:
            return False
        
    # at the end of the iteration, we just need to check if word as L or not since concecutive checks were taken care of
    if hasL == True:
        return True
    # return false if not True (no L)
    return False


# recursive function used to traverse through decision tree
def wordMaker(index, combinations, word):

    # uses global var to keep track of totalNumOfWords we have in all
    global totalNumOfWords

    # word count set to 1 for multiplying purposes 
    wordCounter = 1

    # case once we get to the end of the word (all blanks filled)
    if index == len(word): 
        
        # check if that is a valid word or not using helper function
        if isWordValid(word) == True:

            # goes through each character in word and get the total number of letter combinations we can fill in for that index
            for i in range(len(word)):

                # multiply these ways to get the total amount of words that can be formed using these combination of letters
                wordCounter *= combinations[i]

            # adds it to total word count (current "branch" of the decision tree)
            totalNumOfWords += wordCounter

        # return back (backtracking in terms of decision tree)
        return
    
    # case if character in word at current index is a blank space
    if word[index] == "_":

        # decision 1, fill space with an L
        word[index] = "L"
        # there is only 1 way we can fill this space with L for that index
        combinations[index] = 1
        # recursively call the function with next index with updated word and ways
        wordMaker(index + 1,combinations,word)
    
        # decision 2, fill space with any vowel 
        word[index] = "A"
        # there is 5 ways we can fill this space with vowels for that index
        combinations[index] = 5
        # recursively call the function with next index with updated word and ways
        wordMaker(index + 1,combinations,word)

        # decision 3, fill space with any consonant (besides L)
        word[index] = "B"
        # there are 20 ways for that index
        combinations[index] = 20
        # recursively call the function with next index with updated word and ways
        wordMaker(index + 1,combinations,word)

        # resets the number of ways / word state for future uses
        word[index] = "_"
        combinations[index] = 1

    # case where there is already a letter in that index
    else:
        # recursively go to next index 
        wordMaker(index + 1, combinations, word)


def main():
    
    # takes in the inputted word using sys
    word = sys.stdin.readline().strip()

    # array used to keep track of the number of letters that index in string can store (default is 1)
    combinations = [1 for i in range(100)]
    
    # calls the recursive function on the inputted word at index 0
    wordMaker(0, combinations, list(word))

    # after recursive function ends, prints the total number of words that can be formed when filling out the blank spaces
    print(totalNumOfWords)

main()
