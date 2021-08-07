# No program can be perfect. That's why new versions of every software are released continuously. 
# The current version (1.0) of our program needs to be improved as well.
# 
# Currently, when the user inputs a proper noun, such as Delhi or Paris, the program will 
# 1) convert that string into lowercase and 
# 2) it will look for the lowercase version (i.e., delhi or paris ) in the dataset. 
# However, the dataset doesn't have delhi or paris. It only has Delhi and Paris. 
# Therefore, no definition is currently returned for proper nouns such as Delhi or Paris.
# 
# Please try to fix this issue. You can think of adding another conditional block. 
# You can find the code we currently have attached in this lecture for your convenience.



import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("C:\\Users\\nicol\\Git_Repository\\the-python-mega-course\\2- Application 1, English Thesaurus\\JSON+Data+Inside\\data.json"))

def searchWord(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
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

