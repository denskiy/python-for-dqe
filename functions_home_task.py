# import the 'random' library to generate a list of random numbers
import random
import string
import re

# collections home task

# creating a function that will return a list consisting of number of dictionaries
# the function will have random number (2, 10) as the number of lists and number of items
# but the user might have provide those numbers also

def list_generator(l_num = random.randint(2, 10), d_num = random.randint(2, 10)):
    l = [{key: random.randint(0, 100)
        for key in random.sample(string.ascii_lowercase, k=d_num)}
        for _ in range(l_num)]
    return l


# creating a function that will genarate the resulting dictionary

def resulting_dictionary(l: list):
    
    # create a dictionary that will store tuples containing all necessary information for every unique key
    max_dict = {}

    i = 1 # this var will store a number of dictionary from the list
    for dict in l: # loop through dictionaries
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
    
    return result

# check the results
l = list_generator(3, 5)
print(l)
print(resulting_dictionary(l))


# string object home task

# creating a function that will count all whitespaces in string
def whitespace_counter(s: str):
    count = 0 # create a variable that will store number of whitespaces

    for character in str: # check every character in string
        if character.isspace(): # isspace() returns True if a character is a whitespace character
            count += 1 # count this character if True

    return count


# Get the last words from every sentences to form a last sentence
def generate_new_sentence(s: str):
    sent = s.split('.') # split the string into the sentences using dot symbols

    last_sent = [] # create an empty list to store last words

    for sentence in sent: # loop by every sentence
        if sentence:    # if the sentence is not empty
            last = sentence.split()[-1] # split the sentence by words and get the last one
            last_sent.append(last)  # add words to the list

    last_sentence = ' '.join(last_sent) # form the last sentence from the last_sent list

    s = s + ' ' + last_sentence + '.' # concatenate the initial string with last sentence
    return s


# normalize the text from letter case point of view
def normalize_the_case(s: str):
    s = s.lower() # lower the whole text

    capital_words = [] # create an empty list to store the first words which should begin with capital letter

    for word in s.split('.'): # loop by every sentence
        words = word.split() # split the sentences into words
        if words: # if the word is not empty
            words[0] = words[0].capitalize() # capitalize the first word
        capital_words.append(' '.join(words)) # add the words to the list

    final_text = '. '.join(capital_words) # form the text from the capital_words list   
    return final_text


# create a function that will replace the words
def replace_word(s1: str, s2: str, text: str): # user should provide the word that should be replaced
                                               # and the word that should replace it
    final_text = re.sub(rf'\b{s1}\b', s2, text, flags=re.I)
    return final_text


# check the results

str = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


print("Number of whitespace characters:", whitespace_counter(str))
print("With extra sentence:", generate_new_sentence(str))
print("With normalized case:", normalize_the_case(str))
print("With replacements:", replace_word('iz', 'is', str))
