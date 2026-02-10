temps = list(map(int, input().split()))
res = [0]*len(temps)
stack = []

for i in range(len(temps)):
    while stack and temps[i] > temps[stack[-1]]:
        idx = stack.pop()
        res[idx] = i - idx
    stack.append(i)

print(res)
