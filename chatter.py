# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes
# chatgpt link - https://chat.openai.com/share/5d52ee84-eeb0-4b51-84c2-33df705bdee4
import sys

class UnionFind:
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
    
    def print_union(self):
        unions = {}
        for i in range(len(self.parents)):
            p = self.find(i)
            if p not in unions:
                unions[p] = [i]
            else:
                unions[p].append(i)
        for key in unions:
            print("Parent:", key, "Members:", unions[key])

# random int generator from problem
def randomInt(r,a,b,c):
    return (r * a + b) % c
    
    
def main():
    temp = sys.stdin.readline().strip().split()
    
    while temp:
        
        # vars named in problem description
        n = int(temp[0])
        r = int(temp[1])
        a = int(temp[2])
        b = int(temp[3])
        c = int(temp[4])
        
        uf = UnionFind(n)
        
        for i in range(n):
            
            # generate new x, y, and r
            r = randomInt(r,a,b,c)
            x = r % n 
            r = randomInt(r,a,b,c)
            y = r % n
            
            # redo if same
            while x == y:
                r = randomInt(r,a,b,c)
                x = r % n
                r  = randomInt(r,a,b,c)
                y = r % n
                
            
            # put val in group (connected / talking)
            uf.union(x,y)
                
        
        # Collect group sizes
        group_sizes = {}
        for i in range(n):
            group_id = uf.find(i)
            if group_id not in group_sizes:
                group_sizes[group_id] = 1
            else:
                group_sizes[group_id] += 1

        # Sort group sizes
        sorted_group_sizes = sorted(group_sizes.values(), reverse=True)
        print(len(sorted_group_sizes), end=" ")
        
        multiple = {}
        
        # count frequency of all numbers and store in hash set
        for num in sorted_group_sizes:
            if num not in multiple:
                multiple[num] = 1
            else:
                multiple[num] += 1
                
        # Print size of each group 
        for size, count in multiple.items():
            if count == 1:
                print(size, end= " ")   
                
            # modify format if more than 1 frequency
            else:
                answer = ""
                answer += str(size)
                answer += "x"
                answer += str(count)
                print(answer, end = " ")  
        print()
        temp = sys.stdin.readline().strip().split()
        
    return 

main()
