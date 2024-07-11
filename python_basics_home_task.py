"""create list of 100 random numbers from 0 to 1000"""

# import the 'random' library to generate a list of random numbers
import random

# create the list, where the cycle has 100 iterations and every element is a random integer
# number from 0 to 1000
l = [random.randint(0, 1000) for element in range (100)]


"""sort list from min to max(without using sort())"""

# first loop with number of iterations equal to length of list
# as the max number of swapps = list length
for i in range (len(l)):
    # second loop for picking ajustment elements and we don't need to pick the last one
    for j in range(len(l) - 1):
        # if the element is larger then the next one
        if l[j] > l[j + 1]:
            # the elements are being swapped
            l[j], l[j + 1] = l[j + 1], l[j]


"""calculate average for even and odd numbers"""
"""print both average result in console"""

# declare variables that will store the sums and total number of odd/even numbers
odd_count = 0
odd_average_sum = 0
even_count = 0
even_average_sum = 0

# check if each element of the list is odd or even by deviding it by 2
# and adding it either to even_average_sum or to odd_average_sum
# also counting the number of respective elements
for element in l:
    if element % 2 == 0:
        even_average_sum += element
        even_count += 1
    else:
        odd_average_sum += element
        odd_count += 1

# finding and printing the average results
print (f'the average of odd numbers: {odd_average_sum/odd_count}\n'
       f'the average of even numbers: {even_average_sum/even_count}')
