# LIFE733 Assessment 1 Part 1C - Conditional statements – The triangle problem

print('\nTriangle Definition Calculator\nPlease enter three positive whole numbers as lengths, in the range '
      '1 to 1000 inclusive:')  # description of the program explained to user
a = int(input('Enter Side 1: '))  # Asks user to input a value and converts it into an integer value
b = int(input('Enter Side 2: '))  # Same as line 5
c = int(input('Enter Side 3: '))  # Same as line 5
len_list = [a, b, c]  # organises input values into a list
len_list_sort = sorted(len_list)  # sorts values in the list in ascending numerical order
if (a < 1 or b < 1 or c < 1) or (a > 1000 or b > 1000 or c > 1000):
    # test if either of these statements are true: any sides <1 or a any sides >1000
    exit('Invalid: All of the sides need to be within the range 1-1000\n')
elif len_list_sort[0] + len_list_sort[1] <= len_list_sort[2]:  # tests if the sides can be used to form a triangle
    print('Entered values:\n', len_list, '\nSorted values:\n', len_list_sort, '\nTriangle is Impossible')
elif len_list_sort[0] == len_list_sort[1] == len_list_sort[2]:  # test if each of the sides are equal in length
    print('Entered values:\n', len_list, '\nSorted values:\n', len_list_sort, '\nTriangle is Equilateral')
elif len_list_sort[0] == len_list_sort[1] or len_list_sort[0] == len_list_sort[2] or len_list_sort[1] == \
        len_list_sort[2]:  # test whether any two sides of the triangle are equal in length
    print('Entered values:\n', len_list, '\nSorted values:\n', len_list_sort, '\nTriangle is Isosceles')
elif (len_list_sort[0] != len_list_sort[1] and len_list_sort[0] != len_list_sort[2] and len_list_sort[1] !=
      len_list_sort[2]) and ((len_list_sort[0]**2) + (len_list_sort[1]**2) == (len_list_sort[2]**2)):
    # tests whether each of the sides of the triangle are different and then tests if the triangle is right angled
    print('Entered values:\n', len_list, '\nSorted values:\n', len_list_sort, '\nTriangle is Right angled')
elif (len_list_sort[0] != len_list_sort[1] and len_list_sort[0] != len_list_sort[2] and len_list_sort[1] !=
      len_list_sort[2]) and ((len_list_sort[0]**2) + (len_list_sort[1]**2) != (len_list_sort[2]**2)):
    # tests whether each of the sides of the triangle are different and then tests if the triangle is not right angled
    print('Entered values:\n', len_list, '\nSorted values:\n', len_list_sort, '\nTriangle is Scalene')
