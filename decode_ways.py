s = input()
dp1 = dp2 = 1

for i in range(1, len(s)):
    cur = 0
    if s[i] != '0':
        cur += dp2
    if "10" <= s[i-1:i+1] <= "26":
        cur += dp1
    dp1, dp2 = dp2, cur

print(dp2)
