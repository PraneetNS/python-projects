target = int(input())
position = list(map(int, input().split()))
speed = list(map(int, input().split()))

cars = sorted(zip(position, speed), reverse=True)
stack = []

for p, s in cars:
    time = (target - p) / s
    if not stack or time > stack[-1]:
        stack.append(time)

print(len(stack))
