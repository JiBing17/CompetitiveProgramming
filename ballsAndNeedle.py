# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes


import sys
sys.setrecursionlimit(100000)

# Node class
class Node:
    def __init__(self, values):
        self.values = values
        self.edges = set()


# helper functions for detecting cycles
def has_cycle_util(node, parent, visited):
    visited.add(node)
    for neighbor in node.edges:
        if neighbor not in visited:
            if has_cycle_util(neighbor, node, visited):
                return True
        elif neighbor != parent:
            return True
    return False

def has_cycle(adj_list):
    if len(adj_list) < 3:
        return False
    visited = set()
    for node in adj_list.values():
        if node not in visited:
            if has_cycle_util(node, None, visited):
                return True
    return False

def main():
    
    numOfNeedle = int(sys.stdin.readline().strip())
    nodesCreated = set()
    nodesCreatedP2 = set()
    adjList = {}
    adjList2 = {}

    for i in range(numOfNeedle):
        
        # boolean to check if the two nodes are both new
        newNodes = 1
        newNodesP2 = 1
        
        sameNode = 0
        temp = sys.stdin.readline().strip().split()

        # p2 for floor closed chains check
        valOne = tuple(temp[:3])
        valTwo = tuple(temp[3:])
        valOneP2 = tuple(temp[:2])
        valTwoP2 = tuple(temp[3:5])
        
        node1P2 = None
        node2P2 = None
        node1 = None
        node2 = None
        appended = 0
        appendedP2 = 0
        
        
        # new node case
        if valOne not in nodesCreated:
            node1 = Node(valOne)
            adjList[valOne] = node1
            nodesCreated.add(valOne)
            
        elif valOne in nodesCreated:
            newNodes = 0

        if valTwo not in nodesCreated:
            node2 = Node(valTwo)
            adjList[valTwo] = node2
            nodesCreated.add(valTwo)
        elif valTwo in nodesCreated:
            newNodes = 0
            
        # new node case for floor closed chains
        if valOneP2 not in nodesCreatedP2:
            node1P2 = Node(valOneP2)
            adjList2[valOneP2] = node1P2
            nodesCreatedP2.add(valOneP2)
            
        elif valOneP2 in nodesCreatedP2:
            newNodesP2 = 0
            
        if valTwoP2 not in nodesCreatedP2:
            node2P2 = Node(valTwoP2)
            adjList2[valTwoP2] = node2P2
            nodesCreatedP2.add(valTwoP2)
            
        elif valTwoP2 in nodesCreatedP2:
            if valTwoP2 == valOneP2:
                sameNode = 1
            newNodesP2 = 0


        
        # both nodes created
        if newNodes:
            node1.edges.add(node2)
            node2.edges.add(node1)
        else:
            # case if both nodes are in adjlist already (connect edges)
            if node1 is None and node2 is None:
                node1 = adjList[valOne] 
                node2 = adjList[valTwo]
                node1.edges.add(node2)
                node2.edges.add(node1)
                appended = 1
            
            # case if 1 new node and other in adjacency list
            elif node1 is None:
                target = valOne
                nodeToConnect = node2
            else:
                target = valTwo
                nodeToConnect = node1

            # find node in adjlist and update edges
            if not appended:
                adjList[target].edges.add(nodeToConnect)
                nodeToConnect.edges.add(adjList[target])
                        
        
        # same logic but for floor closed chains
        if sameNode: 
            continue
        
        elif newNodesP2:
            node1P2.edges.add(node2P2)
            node2P2.edges.add(node1P2)
        else:
            if node1P2 is None and node2P2 is None:
                node1P2 = adjList2[valOneP2] 
                node2P2 = adjList2[valTwoP2]
                node1P2.edges.add(node2P2)
                node2P2.edges.add(node1P2)
                appendedP2 = 1
                
            elif node1P2 is None:
                target = valOneP2
                nodeToConnect = node2P2
            else:
                target = valTwoP2
                nodeToConnect = node1P2

            if not appendedP2:
                adjList2[target].edges.add(nodeToConnect)
                nodeToConnect.edges.add(adjList2[target])

    if has_cycle(adjList):
        print("True closed chains")
    else:
        print("No true closed chains")
    
    if has_cycle(adjList2):
        print("Floor closed chains")
    else:
        print("No floor closed chains")

if __name__ == "__main__":
    main()
