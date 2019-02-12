# LIFE733 Assessment 1 Part 1B - Doing mathematical operations

import math  # import the math module

a = int(input("Enter value for a?\n"))  # Asks user to input a value and converts it into an integer value
b = int(input("Enter value for b?\n"))  # Same as line 5
c = int(input("Enter value for c?\n"))  # Same as line 5
d = int(input("Enter value for d?\n"))  # Same as line 5
e = int(input("Enter value for e?\n"))  # Same as line 5
num = [a, b, c, d, e]  # List of user input integers
mean = (sum(num) / len(num))  # mathematical operation to find mean
var = (((num[0] - mean) ** 2) + ((num[1] - mean) ** 2) + ((num[2] - mean) ** 2) + ((num[3] - mean) ** 2) +
            ((num[4] - mean) ** 2)) / len(num)  # mathematical operation to find variance
std_dev = math.sqrt(var)  # uses and imported function from the math module
# to calulate the square root of the variance
print('\nThe user entered: ', num)
print('\nMean is', mean, '(total =', sum(num), ',', 'number of variables =', len(num), ')')
print('\nVariance is', var)
print('\nStd Dev is', std_dev)
