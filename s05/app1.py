# Building an interactive dictionary

# 1. enter a word
# 2a. If word exists then print entry
# 2b. If word doesnt exist, but similar does, then suggest it
# 2c. If word doesnt exist, but no similar does, quit
# 3. If 2a or 2b, ask if want another word.

import json

def load_json_from_file(filename):
    with open(filename) as f:
        return json.load(f)

def get_definition(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else: 
        return None

dictionary_data = load_json_from_file('data.json')
word = input("Enter word: ")
search_word = word.lower()
answers = get_definition(search_word, dictionary_data)

if answers is None:
    print("The word doesn't exist.  Please double check it.")
else: 
    print("%s:" % (search_word))
    
    for index, answer in enumerate(answers):
        print("%i. %s" % ((index+1),answer))