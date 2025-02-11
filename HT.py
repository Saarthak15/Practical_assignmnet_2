import random

print("Flip the coin for Head or Tails")

a = int(input("1 for Head and 2 for Tails:"))

b = random.randint(1,2)

if a == 1:
    result="Head"
elif a== 2:
    result="Tails"

if b == result:
    print("You have won the Toss:", result)
else:
    print("You have lost the Toss:", result)
