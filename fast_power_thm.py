a, b = map(int, input("Enter base and power: ").split())
result = 1

while b > 0:
    if b % 2 == 1:
        result *= a
    a *= a
    b //= 2

print("Power:", result)
