# LIFE733 - Assessment 1 Part 1D - Sorting Exam Scores Into Lists

exam_scores = [10, 78, 65, 96, 76, -27, 100, 191, 56, 79, 60, 33, 56, 50, 75, 45, 99, 60, 67, 68, 31, 99, 21, 0, 55, 76,
               45, 25, 78, 78, 80, 59, 0, 24, 66, 24, 103, 12]  # list of exam scores
sorted_es = sorted(exam_scores)  # Function to sort integers in list into ascending numerical value
dist = []  # Creation of an empty list for sorting to later
merit = []  # Same as line 6
pas = []  # Same as line 6
fail = []  # Same as line 6
error = []  # Same as line 6
for x in sorted_es:  # For loop to sort and add integers from exam_scores to pre-made lists
    if x < 0:  # removes error values less and 0
        del (x)
    elif x < 40:
        fail.append(x)
    elif x < 60:
        pas.append(x)
    elif x < 70:
        merit.append(x)
    elif x <= 100:
        dist.append(x)
for x in exam_scores:  # Another for loop to add index positions of integers outside of 0-100 range
    if x < 0:
        error.append(exam_scores.index(x))
    elif x > 100:
        error.append(exam_scores.index(x))
dist.sort(reverse=1)  # Alters list to descending numerical order
merit.sort(reverse=1)  # Same as line 25
pas.sort(reverse=1)  # Same as line 25
dist_mean = (sum(dist) / len(dist))  # Function to calculate the mean of the dist list
merit_mean = (sum(merit) / len(merit))  # Function to calculate the mean of the merit list
pas_mean = (sum(pas) / len(pas))  # Function to calculate the mean of the pas list
fail_mean = (sum(fail) / len(fail))  # Function to calculate the mean of the fail list
print('Distinction grades (mean =', dist_mean, '):', dist)
print('Merit grades (mean =', merit_mean, '):', merit)
print('Pass grades (mean =', pas_mean, '):', pas)
print('Fail grades (mean =', fail_mean, '):', fail)
print('Errors in positions:', error)
