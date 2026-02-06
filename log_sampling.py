import random

def should_log(prob=0.1):
    return random.random() < prob

for i in range(20):
    if should_log():
        print("LOG EVENT", i)
