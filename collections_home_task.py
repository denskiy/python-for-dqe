# import the 'random' library to generate a list of random numbers
import random
import string


# generating a list of random number (from 2 to 10) of dictionaries with random letter as keys and
# random number (from 0 to 100) as values

list = [{key: random.randint(0, 100) 
        for key in random.sample(string.ascii_lowercase, k=random.randint(2, 10))} 
        for _ in range(random.randint(2, 10))]

# create a dictionary that will store tuples containing all necessary information for every unique key
max_dict = {}


i = 1 # this var will store a number of dictionary from the list
for dict in list: # loop through dictionaries
    for key, value in dict.items(): # loop through keys & values of dictionaries
        if not max_dict.get(key): # if the key is not already stored in max_dict
            max_dict.update({key: (1, value, i)}) # we add it with count=1, value & number of dictionary
        else: # if the key is already stored in max_dict
            count, max_value, value_index = max_dict[key] # we get the values from corresponding key
            count += 1 # increase a counter value
            max_dict[key] = (count, max_value, value_index) # update only the count value for the key
            if max_dict[key][1] < value: # and if the value is bigger then current one
                max_dict[key] = (count, value, i) # also update the value and the index number
    i += 1

# create another dictionary that will store the final results
result = {}
for key, (count, max_value, value_index) in max_dict.items(): # loop through items of max_dict dictionary
    if count == 1: # if key is only in one dict
        result.update({key: max_value}) # we take the key as is and the value
    else: # if key is in multiple dictionaries
        result.update({f'{key}_{value_index}': max_value}) # we generate the new key using value_index

#check the results
print(list)
print(result)
