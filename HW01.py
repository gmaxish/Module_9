import random

print(random.__name__)
print(random.__doc__)
print(random.__file__)

l = []

while len(l) < 50:
    k = random.randrange(100, 1000, 5)
    l.append(k)

print(l)
print(len(l))
print(sum(l) / len(l))
