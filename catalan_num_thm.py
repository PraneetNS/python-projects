n = int(input("Enter n: "))
cat = [0] * (n + 1)
cat[0] = cat[1] = 1

for i in range(2, n + 1):
    for j in range(i):
        cat[i] += cat[j] * cat[i - j - 1]

print("Catalan number:", cat[n])
