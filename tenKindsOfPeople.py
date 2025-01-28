# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes


import sys
sys.setrecursionlimit(100000)

# flood fill function to mark different islands with current id
def flood_fill(matrix, row, col, island_id, target):

    # invalid index
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] != target:
        return
    
    # mark with id and run floodfill on top, bottom, right, and left
    matrix[row][col] = island_id
    flood_fill(matrix, row + 1, col, island_id, target)
    flood_fill(matrix, row - 1, col, island_id, target)
    flood_fill(matrix, row, col + 1, island_id, target)
    flood_fill(matrix, row, col - 1, island_id, target)

def main():
    temp = sys.stdin.readline().strip().split()
    r = int(temp[0])
    c = int(temp[1])
    
    # 2d matrix initialization  
    matrix = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        currRow = sys.stdin.readline().strip()
        for j in range(len(currRow)):
            matrix[i][j] = currRow[j]
            
    island_id = 2  
    
    for i in range(r):
        for j in range(c):
            
            # want postive number id for decimal floodfill - 1
            if matrix[i][j] == '1':
                if island_id < 0:
                    island_id = island_id * -1 
                flood_fill(matrix, i, j, str(island_id), '1')
                island_id += 1
                
            # want negative number id for binary floodfill - 0
            if matrix[i][j] == '0':
                if island_id > 0:
                    island_id = island_id * -1
                flood_fill(matrix, i, j, str(island_id), '0')
                island_id -= 1
          
    n = int(sys.stdin.readline().strip())
    
    for i in range(n):
        temp = sys.stdin.readline().strip().split()
        
        r1 = int(temp[0]) - 1
        c1 = int(temp[1]) - 1
        
        r2 = int(temp[2]) - 1
        c2 = int(temp[3]) - 1
        
        decimal = 0
        binary = 0
        neither = 0

        # if same sign (+ or - for binary or decimal) and id are the same (same island)
        # then we can get to from one corrdinate to the other
        if matrix[r1][c1] == matrix[r2][c2] and int(matrix[r1][c1]) > 0 and int(matrix[r2][c2]) > 0:
            decimal = 1
        elif matrix[r1][c1] == matrix[r2][c2] and int(matrix[r1][c1]) < 0 and int(matrix[r2][c2]) < 0:
            binary = 1
        else:
            neither = 1
            
        if decimal:
            print("decimal")
        elif binary:
            print("binary")
        else:
            print("neither")
            
    return

main()
