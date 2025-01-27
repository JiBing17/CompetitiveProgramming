# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

import sys
sys.setrecursionlimit(100000)  

# node class used for adjlist
class Node:
    def __init__(self, num):
        self.num = num
        self.inDegrees = 0
        self.outDegrees = 0
        self.edges = []
        self.lowlink = -1
        self.index = -1
        self.onStack = False
        

def strongconnect(v, index, stack, scc_list):
    v.index = index
    v.lowlink = index
    index += 1
    stack.append(v)
    v.onStack = True

    for w in v.edges:
        if w.index == -1:
            index = strongconnect(w, index, stack, scc_list)
            v.lowlink = min(v.lowlink, w.lowlink)
        elif w.onStack:
            v.lowlink = min(v.lowlink, w.index)

    if v.lowlink == v.index:
        scc = []
        while True:
            w = stack.pop()
            w.onStack = False
            scc.append(w)
            if w == v:
                break
        scc_list.append(scc)

    return index

# tarjan's algorithm used to find SCCs 
def tarjan(graph):
    index = 0
    stack = []
    scc_list = []

    for v in graph:
        if v.index == -1:
            index = strongconnect(v, index, stack, scc_list)

    return scc_list

# helper function used for graph contraction
def contract_graph(graph, sccs):
    
    contracted_graph = {}
    new_node_counter = 1

    for scc in sccs:
        contracted_node = Node(new_node_counter)
        new_node_counter += 1
        for node in scc:
            contracted_graph[node.num] = contracted_node
               
    for node in graph:
        contracted_node = contracted_graph[node.num]
        for neighbor in node.edges:
            if neighbor.num in contracted_graph:
                contracted_neighbor = contracted_graph[neighbor.num]

                # update edges of new contracted graph
                if contracted_neighbor != contracted_node and contracted_neighbor not in contracted_node.edges:
                    contracted_node.edges.append(contracted_neighbor)
                    contracted_node.outDegrees += 1 
                    contracted_neighbor.inDegrees += 1
                    
    return contracted_graph


def main():
    numOfTestCase = int(sys.stdin.readline().strip())

    for _ in range(numOfTestCase):
        temp = sys.stdin.readline().strip().split()

        n = int(temp[0])
        m = int(temp[1])

        graph = [Node(i) for i in range(1, n+1)]

        # making the adjacency list
        for _ in range(m):
            temp2 = sys.stdin.readline().strip().split()
            node1 = int(temp2[0])
            node2 = int(temp2[1])
            graph[node1 - 1].edges.append(graph[node2 - 1])
            graph[node1 - 1].outDegrees += 1
            graph[node2 - 1].inDegrees += 1

        scc_list = tarjan(graph)
        
        # case if one SCC only 
        if len(scc_list) == 1:
            print("0")
            continue
    
        contracted_graph = contract_graph(graph, scc_list) 

        visitedIn = set()
        visitedOut = set()
        zero_in_degrees_count = 0
        zero_out_degrees_count = 0

        # count number of 0s in InDegrees and outDegrees of contracted graph 
        for node in contracted_graph.values():
            if node.num not in visitedIn:
                visitedIn.add(node.num)
                if node.inDegrees == 0:
                    zero_in_degrees_count += 1 
            if node.num not in visitedOut:
                visitedOut.add(node.num)
                if node.outDegrees == 0:
                    zero_out_degrees_count += 1
                    
        # take max and that is min of edges to make graph into SCC 
        max_zero_degrees = max(zero_in_degrees_count, zero_out_degrees_count)
        print(max_zero_degrees)

main()

