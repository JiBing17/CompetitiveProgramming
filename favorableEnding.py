# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes


import sys
sys.setrecursionlimit(100000)

# Node class
class Node:
    def __init__(self, num):
        self.num = num
        self.ending = None
        self.edgesOut = [] 
        self.edgesIn = []   
        
        # number of ways to get to start node is always 1
        if num == "1":
            self.ways = 1
        else:
            self.ways = 0

# topological sort helper function
def topological_sort_util(node, adjlist, visited, stack):
    visited[node.num] = True
    for neighbor_num in node.edgesOut:
        if not visited[neighbor_num]:
            topological_sort_util(adjlist[neighbor_num], adjlist, visited, stack)
    stack.append(node.num)

def topological_sort(adjlist):
    visited = {node_num: False for node_num in adjlist.keys()}
    stack = []
    for node_num, node in adjlist.items():
        if not visited[node.num]:
            topological_sort_util(node, adjlist, visited, stack)
    return stack[::-1]


def main():
    
    numOfTestCase = int(sys.stdin.readline().strip())
    
    for i in range(numOfTestCase):
        
        # set to check if certain node is already created
        nodesCreated = set()
        adjlist = {}
        
        m = int(sys.stdin.readline().strip())
        
        for j in range(m):
            temp = sys.stdin.readline().strip().split()

            # case if only 1 line
            if m == 1:
                if temp[1] == "favourably":
                    print(1)
                else:
                    print(0)
                break
                   
            # create new node and assign ending to node 
            if len(temp) == 2 and temp[0] not in nodesCreated:
                node = Node(temp[0])
                node.ending = temp[1]
                adjlist[temp[0]] = node
                nodesCreated.add(temp[0])
            # node in adjlist so find and assign ending
            elif len(temp) == 2 and temp[0] in nodesCreated:
                adjlist[temp[0]].ending = temp[1]
                
            # out edges going from node 2 - 4 to node 1
            else:
                # create all nodes that are not already in adjlist
                for k in range(len(temp)):
                    if temp[k] not in nodesCreated:
                        
                        node = Node(temp[k])
                        adjlist[temp[k]] = node
                        nodesCreated.add(temp[k])
                # update edges
                for k in range(1,len(temp)):
                    adjlist[temp[0]].edgesOut.append(temp[k])
                    adjlist[temp[k]].edgesIn.append(temp[0])
                    
        # after break, go to next test case
        if m == 1:
            continue
        
        # run topological sort to get the order to update dp (num of ways in node object)
        sorted_nodes = topological_sort(adjlist)
        
        favEndings = 0
        
        for i in range(1, len(sorted_nodes)):    
            node = adjlist[str(sorted_nodes[i])]
        
            # number of ways to get to ith node is sum of ways to get to nodes pointing to the ith node
            for neighbor in node.edgesIn:
                node.ways += adjlist[neighbor].ways
            
            # only add ways of node that ends favourably
            if node.ending == "favourably":
                favEndings += node.ways
                
        print(favEndings)
                        
main()
