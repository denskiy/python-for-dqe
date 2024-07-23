import re

# create the variable with text
str = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# calculate the number of whitespace characters in the text
count = 0 # create a variable that will store number of whitespaces

for character in str: # check every character in string
    if character.isspace(): # isspace() returns True if a character is a whitespace character
        count += 1 # count this character if True

print("Number of whitespace characters:", count) # I've got 94 whitespace characters but I think that's
                                                 # because of slighly different format of text
                                                 # My assumption is that there should not be the 8 extra
                                                 # whitespace characters at the beginning of last 4 rows
                                                 # and an extra space should be between 'Fix' amd '"iz"'

# Get the last words from every sentences to form a last sentence
sent = str.split('.') # split the string into the sentences using dot symbols

last_sent = [] # create an empty list to store last words

for sentence in sent: # loop by every sentence
    if sentence:    # if the sentence is not empty
        last = sentence.split()[-1] # split the sentence by words and get the last one
        last_sent.append(last)  # add words to the list

last_sentence = ' '.join(last_sent) # form the last sentence from the last_sent list

str = str + ' ' + last_sentence + '.' # concatenate the initial string with last sentence


# normalize the text from letter case point of view
str = str.lower() # lower the whole text

capital_words = [] # create an empty list to store the first words which should begin with capital letter

for word in str.split('.'): # loop by every sentence
    words = word.split() # split the sentences into words
    if words: # if the word is not empty
        words[0] = words[0].capitalize() # capitalize the first word
    capital_words.append(' '.join(words)) # add the words to the list

final_text = '. '.join(capital_words) # form the text from the capital_words list

# replace the 'iz' with 'is' where needed
final_text = re.sub(r'\biz\b', 'is', final_text, flags=re.I) # replace all separate "iz" words to "is" 
final_text = re.sub('Fix“is”', 'Fix“iz”', final_text) # in this case "iz" should not be replaced, as it is 
                                                      # a part of a task. so specified the condition to
                                                      # replace it back in particular case

print(final_text) # print the final version of the text
