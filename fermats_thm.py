a, p = map(int, input("Enter a and prime p: ").split())
print(pow(a, p - 1, p))   # should be 1 if p is prime and gcd(a,p)=1
