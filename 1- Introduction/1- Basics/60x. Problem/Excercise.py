# Write a program that does the following:

# Output:

# Say something: Hello
# Say something: My name is Nico
# Say something: How are you
# Say something: \end
# Hello. My name is Nico. How are  you?

def endPhrase(words):
    splitted_words = words.split(" ")
    if splitted_words[0].capitalize() == "How":
        return "?"
    else:
        return "."

def capsFirstLetter(words):
    splitted_words = words.split(" ")
    splitted_words[0] = splitted_words[0].capitalize()
    return " ".join(splitted_words)

result = []

while True:
    phrase = input("Say something: ")
    if phrase == "\\end":
        break
    end_symbol = endPhrase(phrase)
    phrase += end_symbol
    phrase = capsFirstLetter(phrase)
    result.append(phrase)

print(" ".join(result))
    
