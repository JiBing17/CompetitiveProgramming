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
        self.repair = False
        self.distance = float('inf')  # Initialize distance to infinity

# Dijkstra's Algorithm
def dijkstra(adjlist, start_node, currDistance, distanceLimit, numNodes):
    pq = [(0, start_node, currDistance)]  # Priority queue to store (distance, node) tuples
    start_node.distance = 0
    reached_n = False
    
    while pq:
        distance, curr_node, curr = heapq.heappop(pq)
        #print()
        
        #print("node popped off: ", curr_node.num)
        #print("currDistance: ", curr)
        
        if distance > curr_node.distance:
            continue
        
        # refresh
        if curr_node.repair:
            curr = distanceLimit
            # dijkstra(adjlist, curr_node, curr, distanceLimit, numNodes)
        
        # reached ending
        if curr_node.num == numNodes:  # Check if target node is reached
            reached_n = True
        
        
        #minWeight = 2**31 + 1
        
        for neighbor, weight in curr_node.edgeWeights.items():
            c = curr
            #print("neighbor : ", neighbor, "weight to get there: ", weight)
            if curr >= weight:
                
                #minWeight = min(minWeight, weight)
                
                new_distance = distance + weight
                
                if new_distance <= adjlist[neighbor].distance:
                    
                    adjlist[neighbor].distance = new_distance
                    c -= weight

                    heapq.heappush(pq, (new_distance, adjlist[neighbor], c))
                    #print("node added: ", adjlist[neighbor].num, "new distance: ", new_distance)
                          
        #currDistance -= minWeight  # Update currDistance
                    
    return adjlist, reached_n

# Floyd Warshall's Algorithm
def floyd_warshall(adjlist, numNodes):
    # Initialize distances between all pairs of nodes as infinity
    distances = {i: {j: float('inf') for j in range(1, numNodes + 1)} for i in range(1, numNodes + 1)}

    # Set distance to self as 0
    for i in range(1, numNodes + 1):
        distances[i][i] = 0

    # Update distances based on existing edges
    for node_key, node in adjlist.items():
        for adj_node, weight in node.edgeWeights.items():
            distances[int(node_key)][int(adj_node)] = weight

    # Perform Floyd Warshall's algorithm
    for k in range(1, numNodes + 1):
        for i in range(1, numNodes + 1):
            for j in range(1, numNodes + 1):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances

# Function to print the distance matrix
def print_distances(distances, numNodes):
    print("Distance Matrix:")
    for i in range(1, numNodes + 1):
        for j in range(1, numNodes + 1):
            if distances[i][j] == float('inf'):
                print("INF", end=" ")
            else:
                print(distances[i][j], end=" ")
        print()

def main():
    temp = input().strip().split()
    numNodes = int(temp[0])
    numOfEdges = int(temp[1])
    numOfRepairStations = int(temp[2])
    distanceLimit = int(temp[3])

    temp = input().strip().split()

    adjlist = {}
    repairNums = set()
    repairNums.add(1)  # Assuming the starting node is always 1

    nodesCreated = set()

    for station in temp:
        repairNums.add(int(station))

    for i in range(numOfEdges):
        temp = input().strip().split()

        for j in range(len(temp) - 1):
            if int(temp[j]) not in nodesCreated:
                node = Node(int(temp[j]))
                adjlist[int(temp[j])] = node
                nodesCreated.add(int(temp[j]))

                if int(temp[j]) in repairNums:
                    node.repair = True

        weight = int(temp[2])
        adjlist[int(temp[0])].edgeWeights[int(temp[1])] = weight
        adjlist[int(temp[1])].edgeWeights[int(temp[0])] = weight

    # Run Floyd Warshall's algorithm
    distances = floyd_warshall(adjlist, numNodes)

    # Print the distance matrix
    print_distances(distances, numNodes)

    adjlist, reached_n = dijkstra(adjlist, adjlist[1], distanceLimit, distanceLimit, numNodes)
    
    if not reached_n:
        print("impossible")
    else:
        print(adjlist[numNodes].distance)
    
main()
