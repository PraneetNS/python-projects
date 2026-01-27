chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(n):
    res = ""
    while n:
        res = chars[n % 62] + res
        n //= 62
    return res or "0"

def decode(s):
    num = 0
    for c in s:
        num = num * 62 + chars.index(c)
    return num

print(encode(125))
print(decode("cb"))
