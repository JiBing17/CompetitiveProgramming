# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes



import sys
sys.setrecursionlimit(10000000)

def print_adjlist(adjlist):
    for node_name, node in adjlist.items():
        print(f"Node: {node_name}")
        print("  Level:", node.level)
        print("  Outgoing Edges:")
        for neighbor_name, neighbor_node in node.edgesOut.items():
            print(f"    {neighbor_name} (Level: {neighbor_node.level})")
        print()

# Node class
class Node:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.edgesOut = {}
        self.edgesIn = {}   
             
def main():
    
    temp = sys.stdin.readline().strip().split()
    n = int(temp[0])
    m = int(temp[1])
    d = int(temp[2])
    
    if d == 0:
        print(0) 
        return

    adjlist = {}
    noSkeptical = set()

    
    for i in range(n):
        temp = sys.stdin.readline().strip().split()
        name = temp[0]
        level = int(temp[1])
        node = Node(name, level)
        
        # start node
        if node.level == 0:
            noSkeptical.add(temp[0])
            
        adjlist[name] = node
        
    for i in range(m):
        temp = sys.stdin.readline().strip().split()
        adjlist[temp[0]].edgesOut[temp[1]] = adjlist[temp[1]]
        adjlist[temp[1]].edgesIn[temp[0]] = adjlist[temp[0]]
        
    #print_adjlist(adjlist)

    startName = sys.stdin.readline().strip()
    num = 0
    currDay = 0
    
    
    while currDay != d:
        
        for name in list(noSkeptical):
            node = adjlist[name]
            done = 1
            for neighbor in node.edgesOut:
                neighborNode = adjlist[neighbor]
                
                if neighborNode.level > 0:
                    neighborNode.level -= 1
                    done = 0
                    if neighborNode.level == 0:
                        num += 1
                        noSkeptical.add(neighborNode.name)
                
            if done:
                noSkeptical.remove(node.name)
            
        currDay += 1
        #print(num)

    print(num)
    
main()