# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes


import sys

# Node class
class Node:
    def __init__(self, name, language, languageUnderstood):
        self.name = name
        self.language = language
        self.languageUnderstood = languageUnderstood
        self.edgesOut = []  # Outgoing edges
        self.edgesIn = []   # Incoming edges
        self.index = -1
        self.lowlink = -1
        self.onStack = False

# Tarjan's algorithm for finding strongly connected components
def tarjan(node, stack, index, scc_list):
    node.index = index
    node.lowlink = index
    index += 1
    stack.append(node)
    node.onStack = True

    for neighbor_name in node.edgesOut:
        neighbor = name_to_node[neighbor_name]
        if neighbor.index == -1:
            index = tarjan(neighbor, stack, index, scc_list)
            node.lowlink = min(node.lowlink, neighbor.lowlink)
        elif neighbor.onStack:
            node.lowlink = min(node.lowlink, neighbor.index)

    if node.lowlink == node.index:
        scc = []
        while True:
            popped = stack.pop()
            popped.onStack = False
            scc.append(popped)
            if popped == node:
                break
        scc_list.append(scc)

    return index

def find_strongly_connected_components(adj_list):
    index = 0
    stack = []
    scc_list = []

    for node in adj_list:
        if node.index == -1:
            index = tarjan(node, stack, index, scc_list)

    return scc_list

def main():
    numOfPeople = int(sys.stdin.readline().strip())
    adjList = []

    # Create nodes and populate the adjacency list
    for i in range(numOfPeople):
        temp = sys.stdin.readline().strip().split()
        name = temp[0]
        languageSpoken = temp[1]
        languageUnderstood = temp[2:]
        node = Node(name, languageSpoken, languageUnderstood)
        adjList.append(node)

    # Populate edges based on language understanding relationships
    for i in range(len(adjList)):
        for j in range(i + 1, len(adjList)):
            
            # edge in from node i to node j (node j understands node i)
            if adjList[i].language in adjList[j].languageUnderstood or adjList[i].language == adjList[j].language:
                adjList[i].edgesOut.append(adjList[j].name)
                adjList[j].edgesIn.append(adjList[i].name)
                
            # edge in from node j to node i (node i understands node j)
            if adjList[j].language in adjList[i].languageUnderstood or adjList[j].language == adjList[i].language:
                adjList[j].edgesOut.append(adjList[i].name)
                adjList[i].edgesIn.append(adjList[j].name)

    # Create a dictionary to quickly access nodes by their names
    global name_to_node
    name_to_node = {node.name: node for node in adjList}

    scc_list = find_strongly_connected_components(adjList)

    # Find the size of the largest SCC (amount of people that are staying)
    max_scc_size = max(len(scc) for scc in scc_list)

    result = numOfPeople - max_scc_size

    print(result)

if __name__ == "__main__":
    main()
