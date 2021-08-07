def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

dic = {"first": 1, "second": 2, "third": 3}
lst = [1, 2, 3]
print(mean(dic))
print(mean(lst))