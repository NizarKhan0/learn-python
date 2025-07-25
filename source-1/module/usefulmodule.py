from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sentences = 'This is a sample sentence. This is another sample sentence.'

print(Counter(li))
print(Counter(sentences))

dictionary = defaultdict(lambda: 'Not found', {'a': 1, 'b': 2, 'c': 3})
print(dictionary['a'])
print(int())

# d = OrderedDict()
d = {'c': 100}
d['a'] = 1
d['b'] = 2

d2 = {'c': 100}
d2['b'] = 2
d2['a'] = 1


print(d2 == d)  # False, order matters in OrderedDict
