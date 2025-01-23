# Author: Ji Bing Ni 
# It is not ok to share my code anonymously for educational purposes


# import sys for better memory usage
import sys

class MinHeap:  # minHeap copied from: https://www.geeksforgeeks.org/min-heap-in-python/
  
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
  
    # Function to return the position of 
    # parent for the node currently 
    # at pos 
    def parent(self, pos): 
        return pos//2
  
    # Function to return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self, pos): 
        return 2 * pos 
  
    # Function to return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self, pos): 
        return pos*2 > self.size 
  
    # Function to swap two nodes of the heap 
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    # Function to heapify the node at pos 
    def minHeapify(self, pos): 
  
        # If the node is a non-leaf node and greater 
        # than any of its child 
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
  
                # Swap with the left child and heapify 
                # the left child 
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.minHeapify(self.leftChild(pos)) 
  
                # Swap with the right child and heapify 
                # the right child 
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.minHeapify(self.rightChild(pos)) 
  
    # Function to insert a node into the heap 
    def insert(self, element): 
        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
  
    # Function to build the min heap using 
    # the minHeapify function 
    def minHeap(self): 
  
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 
  
    # Function to remove and return the minimum 
    # element from the heap 
    def remove(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.minHeapify(self.FRONT) 
        return popped 
    
    # function used to access the smallest value in heap
    def getMin(self):
        return self.Heap[self.FRONT]
    



def main():

    # intialize minHeap
    mH = MinHeap(1000000)

    # reads line and store the 2 num into vars (num of researchers and num of addtional time for eahc station after researcher leaves)
    data = sys.stdin.readline().strip().split()

    # vars for storing those numbers
    numOfResearchers = int(data[0])
    additionalTime = int(data[1])

    # worst case of unlockings would be the number of researchers (unlock 1 for each)
    maxUnlockings = numOfResearchers

    # current unlocking intialized to 1 (at least 1 to be unlocked)
    currentUnlockings = 1

    # an array of array to store the following info (start time, end time (free), time until room close (end time + additonal time))
    periods = []
    
    # goes through each researcher
    for i in range(numOfResearchers):

        # reads line and stores the 2 num in temp array
        temp = sys.stdin.readline().strip().split()

        # int typecast for start
        start = int(temp[0])

        # int typecast + calculation for end
        end = start + int(temp[1])

        # calculation for until room close using end + additonal time
        untilClose = end + additionalTime
        
        # another temp array for appending 
        temp2 = []

        # append the data that we got for each researcher
        temp2.append(start)
        temp2.append(end)
        temp2.append(untilClose)

        # append that array to our array of arrays
        periods.append(temp2)
    
    # sort array of arrays by start time
    periods = sorted(periods, key = lambda x: x[0])


    # goes through each period 
    for i in range(len(periods)):
        
        # skip first one (no checks needed )
        if i == 0:

            # add station end time into min heap
            mH.insert(periods[i][2])

            continue
        
        # removes end times that has passed already
        if periods[i][0] > mH.getMin():
            mH.remove()

            
        # check if current start time needs to open new room (room is occupied or earliest close time of lab is less than when the current researcher starts)
        if periods[i][0] < mH.getMin() - additionalTime or periods[i][0] > mH.getMin():
            
            # add new room by adding end time into min heap
            mH.insert(periods[i][2])

            # add to the number of unlockings
            currentUnlockings += 1
        
        else:
           
           # remove earliest time slot since it's now being occupied
            mH.remove()
            # add the end time slot of the used room
            mH.insert(periods[i][2])

    # subract the rooms we unlocked to the worst case to get the number of rooms we saved
    numOfUnlockingsSaved = maxUnlockings - currentUnlockings    

    # print that answer
    print(numOfUnlockingsSaved)
        
main()