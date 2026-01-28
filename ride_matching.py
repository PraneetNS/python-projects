drivers = list(map(int, input().split()))
riders = list(map(int, input().split()))

drivers.sort()
riders.sort()

i = j = matches = 0
while i < len(drivers) and j < len(riders):
    if drivers[i] >= riders[j]:
        matches += 1
        i += 1
        j += 1
    else:
        i += 1

print(matches)
