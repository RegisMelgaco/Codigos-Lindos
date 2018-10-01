# i am following this tutorial, but using Python 3
# https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming

import functools

codefy_names = lambda names : [*map(hash, names)]

# print("agents code names:",codefy_names(['Mary', 'Isla', 'Sam', "Li", "testes"]))

# def average_height (people):
    
# print(average_height([{'name': 'Mary', 'height': 160},
#           {'name': 'Isla', 'height': 80},
#           {'name': 'Sam'}]));