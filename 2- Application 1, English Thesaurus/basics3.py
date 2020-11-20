# Version 1.2 (E)
# A student discovered another issue with the program. 
# The program cannot return the definition of acronyms such as USA or NATO; 
# therefore, add another conditional to make the program return the definition of such words. 

import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("C:\\Users\\nicol\\Git_Repository\\the-python-mega-course\\2- Application 1, English Thesaurus\\JSON+Data+Inside\\data.json"))

def searchWord(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        userAnswer =  input("Did you mean %s instead? Enter Y if yes, or N if no. " % get_close_matches(word, data.keys())[0])
        if userAnswer == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif userAnswer == "N":
            return "The word does not exists."
        else: 
            return "Answer not correct."
    else:
        return "The word does not exists."


word = input("Enter word: ")

output = searchWord(word)

if type(output) == list:
    for result in output:
        print(result)
else:
    print(output)

