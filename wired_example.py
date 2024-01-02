
#based on the Wired article by Rhett Allain
import random

n = 0
N = 1000

n1win = 0

while n<N:
    prize = random.randint(0,2)
    choice = random.randint(0,2)
    if prize == choice:
        n1win += 1
    n += 1

print(f"Number of trials: {n}")
print(f"Percentage of wins: {n1win*100/n}")