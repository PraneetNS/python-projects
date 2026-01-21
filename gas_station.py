gas = list(map(int, input().split()))
cost = list(map(int, input().split()))

total = tank = start = 0

for i in range(len(gas)):
    diff = gas[i] - cost[i]
    total += diff
    tank += diff
    if tank < 0:
        start = i + 1
        tank = 0

print(start if total >= 0 else -1)
