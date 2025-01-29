# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

import sys
import heapq

sys.setrecursionlimit(10000000)

# Node class
class Node:
    def __init__(self, num):
        self.num = num
        self.edgeWeights = {}

def print_adj_list(adjlist):
    for node_num, node in adjlist.items():
        print(f"Node {node_num}:")
        for neighbor, weight in node.edgeWeights.items():
            print(f"  -> Neighbor: {neighbor}, Weight: {weight}")

def prim(adjlist):
    visited = set()
    total_weight = 0
    pq = []
    
    # Start with an arbitrary node (here, node 0)
    start_node = 0
    visited.add(start_node)
    
    # Add all edges incident to the start node into pq
    for neighbor, weight in adjlist[start_node].edgeWeights.items():
        heapq.heappush(pq, (weight, start_node, neighbor))
    
    while pq:
        weight, u, v = heapq.heappop(pq)
        
        # If the node v is not visited, add it to the MST
        if v not in visited:
            visited.add(v)
            total_weight += weight
            
            # Add all edges incident to v (connected to unvisited nodes) into pq
            for neighbor, weight in adjlist[v].edgeWeights.items():
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, v, neighbor))
    
    return total_weight

def main():
    
    n = int(sys.stdin.readline().strip())
    coordinates = {}
    adjlist = {}
    
    # store node in adjlist
    for i in range(n):
        temp = sys.stdin.readline().strip().split()
        coordinates[i] = (int(temp[0]), int(temp[1]))
        node = Node(i)
        adjlist[i] = node

    # making of graph with corresponding edges / edge weights
    for i in range(n-1):
        x = coordinates[i][0]
        y = coordinates[i][1]
        for j in range(i+1,n):
            x2 = coordinates[j][0]
            y2 = coordinates[j][1]

            weight = abs(x - x2) + abs(y - y2)
            adjlist[i].edgeWeights[j] = weight
            adjlist[j].edgeWeights[i] = weight

    # Run Prim's algorithm to find MST and calculate its weight
    mst_weight = prim(adjlist)
    
    # times 2 for going back
    final_answer = mst_weight * 2
    
    print(final_answer)

main()
