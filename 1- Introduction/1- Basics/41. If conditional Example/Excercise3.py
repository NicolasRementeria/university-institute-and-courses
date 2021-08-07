# Hot, Warm, Cold (E)

# Define a function that:
# 1- takes a temperature as parameter
# 2- Returns Hot if the temperature is greater than 25
# 3- Returns Warm if the temperature is between 15 and 25, including both
# 4- Returns Cold if the temperature is less than 15

def myFunc(temp):
    if temp > 25:
        return "Hot"
    elif temp < 15:
        return "Cold"
    else:
        return "Warm"