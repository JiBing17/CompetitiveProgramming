# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

import sys
import heapq

def main():
    temp = sys.stdin.readline().strip().split()
    row = int(temp[0])
    col = int(temp[1])
    
    matrix = [[0 for i in range(col)] for j in range(row)]
    
    for i in range(row):
        temp = sys.stdin.readline().strip().split()
        for j in range(len(temp)):
            matrix[i][j] = int(temp[j])
    
    pq  = [(matrix[0][0],0,0)]
    
    visited = [[0 for i in range(col)] for j in range(row)]
    maxEncountered = -1
    
    for i in range(1,row):
        heapq.heappush(pq,(matrix[i][0], i,0))
        
    while pq:
        
        currDepth, currR, currC = heapq.heappop(pq)
        visited[currR][currC] = 1
        maxEncountered = max(maxEncountered, currDepth)
        
        if currC == col - 1:
            break
        
        neighbors = [(currC+1, currR), (currC-1, currR), (currC, currR+1), (currC, currR-1)]
        
        for nc, nr in neighbors:
            if 0 <= nc < col and 0 <= nr < row and visited[nr][nc] == 0:
                heapq.heappush(pq, (matrix[nr][nc], nr, nc))
                
    print(maxEncountered)

main()
