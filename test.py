# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, letter):
        self.letter = letter
        self.index = None
        self.lowlink = None
        self.onStack = False
        self.inDegrees = 0
        self.outDegrees = 0
        self.inEdges = []
        self.outEdges = []

# tarjans algorithm for finding SCCs
def tarjan(node, stack, index, scc_list):
    node.index = index
    node.lowlink = index
    index += 1
    stack.append(node)
    node.onStack = True

    for neighbor in node.outEdges:
        if neighbor.index is None:
            index = tarjan(neighbor, stack, index, scc_list)
            node.lowlink = min(node.lowlink, neighbor.lowlink)
        elif neighbor.onStack:
            node.lowlink = min(node.lowlink, neighbor.index)

    if node.lowlink == node.index:
        scc = []
        while True:
            popped_node = stack.pop()
            popped_node.onStack = False
            scc.append(popped_node)
            if popped_node == node:
                break
        scc_list.append(scc)

    return index


def find_scc(adjList):
    index = 0
    stack = []
    scc_list = []

    for node in adjList.values():
        if node.index is None:
            index = tarjan(node, stack, index, scc_list)

    return scc_list

# helper function to sort SCCs a certain way
def print_sorted_scc(scc_list):
    
    for scc in scc_list:
        scc.sort(key = lambda s:s.letter)  # Sort elements within each SCC alphabetically
        
    # sort each list by first node letter
    scc_list.sort(key=lambda scc: scc[0].letter)

    for scc in scc_list:
        
        scc_elements = [node.letter for node in scc]

        for elem in scc_elements:
            print(elem, end =" ")
        print()

def main():
    numOfProblems = int(sys.stdin.readline().strip())

    while numOfProblems != 0:
        adjList = {}
        # dont want duplicates so we keep 2 sets
        lettersCreated = set()
        nodesCreated = set()

        for i in range(numOfProblems):
            temp = sys.stdin.readline().strip().split()

            for j in range(len(temp)):
                # new node, add to adjlist 
                if temp[j] not in lettersCreated:
                    node = Node(temp[j])
                    adjList[temp[j]] = node
                    nodesCreated.add(node)
                    lettersCreated.add(temp[j])

                # add directed edges from all nodes 1 to 5 into node 6 (preferred node)
                if j == len(temp) - 1:
                    for node in nodesCreated:
                        if node.letter != temp[j] and node not in adjList[temp[j]].inEdges and node.letter in temp:
                            adjList[temp[j]].inEdges.append(node)
                            if node.inDegrees == 0:
                                adjList[temp[j]].inDegrees += 1
                            else:
                                adjList[temp[j]].inDegrees += node.inDegrees
                            adjList[node.letter].outEdges.append(adjList[temp[j]])
                            adjList[node.letter].outDegrees += 1

        scc_list = find_scc(adjList)
        print_sorted_scc(scc_list)

        numOfProblems = int(sys.stdin.readline().strip())


main()
