__author__ = 'junlingwang'

import random  # random is a model
import operator
import worditem

l = ['ab', 'bcd', 'c', 'ddeff', 'ed']
d = {'a': 8, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 5, 'g': 5}

n = random.randint(1, 5)  # randint means random int
# index_list = []
# for key, value in d.items():
#     index_list.append(value)
# index_list.sort()  # sort the list according to values

# key_list = []
# for i in index_list:
#     for key, value in d.items():
#         if value == i:
#            key_list.append(key)
# key_list = sorted(d.items(), key=operator.itemgetter(1))
# d.items() is a list containing tuples
# key=operator.itemgetter(1) means sort the list by the second element of each tuple.
# items with same values will be automatically sorted randomly

# print (key_list)
# print(d[random.choice(l)])

# sorted_list = sorted(l, key=lambda string: len(string))
#  lambda function. Before the colon is parameter, after the colon is the result.
print()
