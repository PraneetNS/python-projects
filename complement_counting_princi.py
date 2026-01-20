import math

n = int(input())
unique = math.perm(26, n)
total = 26 ** n

print(1 - unique / total)
