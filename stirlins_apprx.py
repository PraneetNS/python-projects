import math

n = int(input("Enter n: "))
approx = math.sqrt(2 * math.pi * n) * (n / math.e) ** n
print("Approx factorial:", approx)
