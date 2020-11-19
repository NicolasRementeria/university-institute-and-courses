def sentence_maker(phrase):
    interrogatives = ("how", "where", "why", "what", "when")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        capitalized += "?"
        return capitalized
    else:
        capitalized += "."
        return capitalized

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\\end":
        break
    else:
        results.append(sentence_maker(user_input))

results = " ".join(results)

print(results)