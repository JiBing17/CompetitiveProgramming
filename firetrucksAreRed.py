# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes


import sys

def print_adjlist(adjlist):
    print("Adjacency List:")
    for key, value in adjlist.items():
        print(f"{key}: {value}")

def print_union_find(uf):
    print("Union-Find Data Structure:")
    for i in range(len(uf.parents)):
        print(f"Node {i}: Parent={uf.parents[i]}, Rank={uf.ranks[i]}, Size={uf.sizes[i]}")

class Node:
    def __init__(self, num):
        self.num = num
        self.parent = None
        self.rank = 0
        self.traits = set()
        self.edgeWeights = {}
        
class UnionFind: # UF from github https://github.com/stevenhalim/cpbook-code/blob/1920c2e816b49c38b538da6a385754240215fed4/ch2/ourown/unionfind_ds.py#L71
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.numdisjoint = n

    def find(self, x):
        xp = x
        children = []
        while xp != self.parents[xp]:
            children.append(xp)
            xp = self.parents[xp]
        for c in children:
            self.parents[c] = xp
        return xp

    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return

        if self.ranks[ap] < self.ranks[bp]:
            self.parents[ap] = bp
            self.sizes[bp] += self.sizes[ap]
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]

def main():
    numOfNodes = int(sys.stdin.readline().strip())
    uf = UnionFind(numOfNodes)

    # hash set with key being similar trait storing nums with that trait
    adjlist = {}
    for i in range(numOfNodes):
        temp = sys.stdin.readline().strip().split()
        numTraits = int(temp[0])
        for j in range(1, numTraits + 1):
            trait = temp[j]
            if trait not in adjlist:
                adjlist[trait] = []
            adjlist[trait].append(i)
    
    
    # dont union
    mentioned = []
    
    # Union Find on numbers in the same hash key / trait
    for key in adjlist:
        for i in range(len(adjlist[key]) - 1):
            
            # not connected
            if not uf.find(adjlist[key][i]) == uf.find(adjlist[key][i+1]):
                mentioned.append([adjlist[key][i] + 1, adjlist[key][i+1] + 1, key])
                
                uf.union(adjlist[key][i], adjlist[key][i+1])
            
             
    # Check if all nodes are in the same set (connected)
    if uf.numdisjoint != 1:
        print("impossible")
    
    else:
        for set in mentioned:
            for num in set:
                print(num, end=" ")
            print()
    
if __name__ == "__main__":
    main()
