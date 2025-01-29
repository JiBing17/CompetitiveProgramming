# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes


import sys
import numpy as np
def main():
    temp = sys.stdin.readline().strip().split()
    instruments = int(temp[0])
    numOfNotes = int(temp[1])
    playable = {}
    
    for i in range(instruments):
        temp = sys.stdin.readline().strip().split()
        notes = int(temp[0])
        
        for j in range(1, notes + 1 ):
            if int(temp[j]) not in playable:
                playable[int(temp[j])] = set()
                playable[int(temp[j])].add(i)
            else:
                playable[int(temp[j])].add(i)
                
    temp = sys.stdin.readline().strip().split()
    dp = [[float('inf') for i in range(numOfNotes)] for j in range(instruments)]
    
    
    for i in range(instruments):
        currNote = int(temp[0])
        if i in playable[currNote]:
            dp[i][0] = 0
            
    # Printing the dictionary playable
    #print("Playables:")
    #for key, value in playable.items():
    #    print(key, value)
    
    # Printing the 2D array dp
    #print("DP Array:")
    #for row in dp:
    #    print(row)

    for j in range(1, numOfNotes):
        note = int(temp[j])
        ins = playable[note]
        
        for instrument in ins:
            prevNote = int(temp[j-1])
            prevInstruments = playable[prevNote]
                        
            for prev in prevInstruments:
                if prev == instrument:       
                    dp[instrument][j] = min(dp[instrument][j], dp[prev][j-1])
                else:
                    dp[instrument][j] = min(dp[instrument][j] , dp[prev][j-1] + 1)
        
    minSwitches = dp[i][numOfNotes-1]
    
    for i in range(1 , instruments):
        minSwitches = min(minSwitches, dp[i][numOfNotes-1])
    print(minSwitches)
            
    # Print the populated dictionary
    #print(playable)
    #print(np.array(dp))
main()

