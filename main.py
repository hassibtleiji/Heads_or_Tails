import random

heads_or_tails = random.randint(0, 1)

if (heads_or_tails == 0):
    heads_or_tails = "Tails"
    print(heads_or_tails)
else:
    heads_or_tails = "Heads"
    print(heads_or_tails)
