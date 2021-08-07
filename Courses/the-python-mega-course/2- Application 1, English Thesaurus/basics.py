import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("C:\\Users\\nicol\\Git_Repository\\the-python-mega-course\\2- Application 1, English Thesaurus\\JSON+Data+Inside\\data.json"))

#>>> type(data) 
#<class 'dict'>

#>>> data["rain"]
#['Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.', 'To fall from the clouds in drops of water.']

def searchWord(word):
    word = word.lower()
    if word in data:
        return data[word]
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


####### 


searchWord(word="banana")

# searchWord(word="banana")
# ['The fruit of the banana tree.', 'The tropical treelike plant which bears clusters of bananas. The plant, of the genus Musa, has large, elongated leaves.']

user_word = input("Search a word: ")

print(searchWord(user_word))

SequenceMatcher(None, "rainn", "rain").ratio()

# Output: 
# 0.8888888888888888

# Gets the difference between two strings

# help(get_close_matches)

# get_close_matches(word, possibilities, n=3, cutoff=0.6)
# Use SequenceMatcher to return list of the best "good enough" matches.   
# word is a sequence for which close matches are desired (typically a     
# string).

get_close_matches("rainn", ["help", "pyramid", "rain"])

# Output:
# ['rain']

get_close_matches("rainn", data.keys())

# Output:
# ['rain', 'train', 'rainy']

# get_close_matches("rainn", data.keys(), n=1, cutoff=0.8) 
# ['rain']

get_close_matches("rainn", data.keys())[0] 

# Output:
# 'rain'

