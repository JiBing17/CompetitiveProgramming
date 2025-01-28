# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes


import sys
sys.setrecursionlimit(100000000)


# flood fill to mark all the different islands with the current id
def flood_fill(matrix, row, col, n, m, component_id, counter):
    
    if row < 0 or row >= n or col < 0 or col >= m:
        return

    # ran into perimter, increment counter
    if matrix[row][col] == 1:
        counter[0] += 1
        return
    if matrix[row][col] != 0:
        return
    
    matrix[row][col] = component_id
    
    flood_fill(matrix, row + 1, col, n, m, component_id, counter)  # Down
    flood_fill(matrix, row - 1, col, n, m, component_id, counter)  # Up
    flood_fill(matrix, row, col + 1, n, m, component_id, counter)  # Right
    flood_fill(matrix, row, col - 1, n, m, component_id, counter)  # Left


def main():
    
    temp = sys.stdin.readline().strip().split()
    n = int(temp[0])
    m = int(temp[1])
    matrix = [[0 for i in range(m)] for j in range(n)]
    
    for i in range(n):
        temp = sys.stdin.readline().strip()
        for j in range(m):  # Iterate over each column in the row
            matrix[i][j] = int(temp[j])


    component_id = 2
    # Counter for perimeter
    counter = [0]  
    
    # Run flood fill on top and bottom borders if 0 (increment counter if 1)
    for j in range(m):
        if matrix[0][j] == 0:
            flood_fill(matrix, 0, j, n, m, component_id, counter)
            component_id += 1
        
        elif matrix[0][j] == 1:
            counter[0] += 1
            
        if matrix[n - 1][j] == 0:
            flood_fill(matrix, n - 1, j, n, m, component_id, counter)
            component_id += 1

        elif matrix[n-1][j] == 1:
            counter[0] += 1
    
    # Run flood fill on left and right borders if 0 (increment counter if 1)
    for i in range(n):
        
        if matrix[i][0] == 0:
            flood_fill(matrix, i, 0, n, m, component_id, counter)
        elif matrix[i][0] == 1:
            counter[0] += 1
            
        if matrix[i][m - 1] == 0:
            flood_fill(matrix, i, m - 1, n, m, component_id, counter)
        elif matrix[i][m-1] == 1:
            counter[0] += 1
            

    print(counter[0])

main()
