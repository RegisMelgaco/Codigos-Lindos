import functools

delete_nth = lambda order = [],max_e = 99: functools.reduce(lambda a, e: a + [e] if a.count(e) < max_e else a, order, [])

print(delete_nth ([1,1,1,1],2))
print(delete_nth ([20,37,20,21],1))