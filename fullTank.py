# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes
import sys
import heapq


# Node class
class Node:
    def __init__(self, num):
        self.num = num
        self.edges = {}
        self.cost = -1


def dj(start , end, adjlist, maxFuel, cost):
    
    pq = [(cost, start, maxFuel)]
    
    reached = 0
    minCost = float('inf')
    
    
    while pq:     
        
        # cost , node, current fuel
        c, n, f = heapq.heappop(pq)   
        
        # popped end node (reached)   
        if n == end:
            reached = 1
            minCost = c
            break      
        node = adjlist[n]     
           
        for num in node.edges:          
            while f < node.edges[num]:
                f += 1          
            while f <= maxFuel:
                heapq.heappush(pq, (f * node.cost + c, num, f))
                f += 1
    if reached:
        print(minCost) 
        return 
    print("impossible") 
    return
 
      
def main():
    temp = sys.stdin.readline().strip().split()
    c = int(temp[0])
    r = int(temp[1])
    
    temp = sys.stdin.readline().strip().split()
    nodesCreated = set()
    adjlist = {}
    
    for i in range(r):
        
        temp2 = sys.stdin.readline().strip().split()
        for j in range(len(temp2)):
            
            # new node instance store in adjlist
            if j != len(temp2) - 1 and temp2[j] not in nodesCreated:
                node = Node(int(temp2[j]))
                node.cost = int(temp[node.num])
                adjlist[int(temp2[j])] = node
                nodesCreated.add(temp2[j])
                    
            # connect nodes with edge weight 
            if j == len(temp2) - 1:
                edgeWeight = int(temp2[j])
                adjlist[int(temp2[0])].edges[int(temp2[1])] = edgeWeight
                adjlist[int(temp2[1])].edges[int(temp2[0])] = edgeWeight
                
    q = int(sys.stdin.readline().strip())
    
    for i in range(q):
        
        temp2 = sys.stdin.readline().strip().split()
        maxFuel = int(temp2[0])
        start = int(temp2[1])
        end = int(temp2[2])
        cost = 0
        
        dj(start, end, adjlist, maxFuel, cost)

    print("Adjacency List:")
    for node_num, node in adjlist.items():
        print(f"Node {node_num}:")
        print("  Cost:", node.cost)
        print("  Edges:", node.edges)

    
# Print the adjacency list
main()
