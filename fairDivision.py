# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes

#  https://chat.openai.com/share/9712686d-aeb9-4f1c-a994-51da22866816 - link to chat history

import sys 

def calculate_contribution(p, n, contributions):
    
    total_max_contribution = sum(contributions)

    # can't buy present even with max offers combined
    if total_max_contribution < p:
        print("IMPOSSIBLE")
        return
    
    # sort by val in ascending order, if val are same, sort those by index in descending order
    contributions_with_indices = [(value, index) for index, value in enumerate(contributions)]
    contributions_with_indices = sorted(contributions_with_indices, key= lambda x: (x[0], -x[1]))
 
    peopleLeft = n
    price = p
    payed = []
    
    # running avg
    for value, index in contributions_with_indices:
        moneyNeeded = price // peopleLeft
        
        # have enough
        if value >= moneyNeeded:
           price -= moneyNeeded
           payed.append((index, moneyNeeded, value - moneyNeeded))

        # pay as much as they can
        else:
            price -= value
            payed.append((index , value,  0))
            
        peopleLeft -= 1
    
    # print val by original index
    payed.sort(key=lambda x: x[0])
    
    for (index, value, remainder) in payed:
        print(value, end=" ")
    print()
    

testCases= int(sys.stdin.readline().strip())
for i in range(testCases):
    
    price, numOfPeople = map(int, sys.stdin.readline().strip().split())
    contributions = list(map(int, sys.stdin.readline().strip().split()))
    
    calculate_contribution(price, numOfPeople, contributions)
