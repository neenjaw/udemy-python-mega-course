# Building an interactive dictionary

# 1. enter a word
# 2a. If word exists then print entry
# 2b. If word doesnt exist, but similar does, then suggest it
# 2c. If word doesnt exist, but no similar does, quit
# 3. If 2a or 2b, ask if want another word.

import json
from difflib import SequenceMatcher

#---------------------------
def load_json_from_file(filename):
    with open(filename) as f:
        return json.load(f)
#---------------------------

#---------------------------
def get_definition(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    else: 
        return None
#---------------------------

#---------------------------
def find_similar(word, dictionary, threshold = 0.8):
    similar = []

    for entry in dictionary.keys():
        if SequenceMatcher(None, word, entry).ratio() > threshold:
            similar.append(entry)

    return similar
#---------------------------

#---------------------------
def print_word_definition(word, definitions):
    print("%s:" % (word))
    
    for index, definition in enumerate(definitions):
        print("  %i. %s" % ((index+1),definition))
#---------------------------

dictionary_data = load_json_from_file('data.json')

loop_condition = True
while loop_condition:

    word = input("Enter word: ")
    search_word = word.lower()
    answers = get_definition(search_word, dictionary_data)

    if answers is None:
        suggestions = find_similar(search_word, dictionary_data)

        if len(suggestions) == 0:
            print("The word doesn't exist.  Please double check it.")
        else:
            print("'%s' could not be found, did you mean: %s" % (search_word, suggestions[0]))
            if (input("[Y / N]: ")).lower() == "y":
                new_answers = get_definition(suggestions[0], dictionary_data)
                print_word_definition(suggestions[0], new_answers)
    else: 
        print_word_definition(search_word, answers)

    # determine whether to continue looping
    if (input("Another definition? ").lower() != "y"):
        loop_condition = False

