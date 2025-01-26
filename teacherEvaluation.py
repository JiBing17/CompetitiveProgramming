# Author: Ji Bing Ni
# It is not ok to share my code anonymously for educational purposes


# import sys for better memory usage
import sys

def additional_students_needed(numOfStudents, perferredAverage, scores):
    
    sum_score = sum(scores)
    current_average = sum(scores) // numOfStudents
    
    score = current_average
    students = numOfStudents
    
    # invalid case (can't make progress if 100)
    if perferredAverage >= 100:
        return "impossible"
    
    # perfect score for each additional student to minimize students needed
    while (score < perferredAverage):
        
        students += 1
        score = (sum_score + 100) // students
        
        # update for next iteration
        sum_score += 100
        additional_students = students - numOfStudents
        
    # return the difference in students now to initial amount of students   
    return additional_students
      

numOfStudents, perferredAverage = map(int, sys.stdin.readline().strip().split())
scores = list(map(int, sys.stdin.readline().strip().split()))

result = additional_students_needed(numOfStudents, perferredAverage, scores)
print(result)
