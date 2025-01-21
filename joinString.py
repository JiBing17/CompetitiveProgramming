# Author: Ji Bing Ni
# It is not okay to share my code for anonymously for educational purposes
# Kattis Week-1

# node class for link list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.tail = None

# import needed to less memory usage
import sys

def main():


    # firstline gives us the n number of lines strings that follows (using sys import for efficient memory usage)
    firstLine = int(sys.stdin.readline().strip())

    if firstLine == 1:
        print(sys.stdin.readline().strip())
        return

    # temp array to store the number of strings
    temp = []

    # goes through each string and adds to temp array using sys import for more efficient memory usage
    for i in range(firstLine):

        node = Node(sys.stdin.readline().strip())
        node.tail = node
        temp.append(node)
        

    # goes through the next n-1 lines to concat the targeted strings to one another
    for i in range(firstLine - 1):
                
        # line gives us 2 numbers of strings we need to concat and stores them strings into an array
        temp2 = sys.stdin.readline().strip().split()
        
        # substract 1 to both to get the correct index of where these strings are located
        string1Index = int(temp2[0]) - 1
        string2Index = int(temp2[1]) - 1

        n1 = temp[string1Index]
        n2 = temp[string2Index]

        n1.tail.next = n2

        
        n1.tail = n2.tail

        temp[string2Index] = Node("")

    # goes and prints out all the node in a single line using dummy node (intial start node)
    for i in range(len(temp)):
        if temp[i].data != "":
            index = i

    node = temp[index]

    while node != None:
        print(node.data, end = "")
        node = node.next
main() 