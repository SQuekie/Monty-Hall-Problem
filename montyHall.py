# Monty Hall Problem #
"""
Suppose you are on a game show, and you are given the choice of three doors
Behind one door is a car; behind the others, goats. 
You pick a door, say No. 1, and the host, who knows what is behind the doors, opens another door, say No. 3, which has a goat. 
He then says to you, “Do you want to pick door No. 2?” 
Is it to your advantage to switch your choice? 
"""

import random
import time

item = ["goat", "goat", "car"]
sample_size = int(input("Enter sample size: "))
switch_win = 0
stay_win = 0

random.seed(time.time())

for i in range(sample_size):
    choice = random.choice(item)

    # Player picks the car on first try
    if choice == "car":
        # Player that switch will lose

        # Player that sticks to his choice will win
        stay_win +=1
    
    if choice == "goat":
        """
        Monty will open the other door that contains the goat.
        """
        # Player that switch will win
        switch_win +=1

        # Player that stay will lose

print("  ---Probability of winning the Montal Hall problem---")
print("Number of simulation: ", sample_size)
print("---------------------------------------------------------")
print("Always switch: ", float(switch_win/sample_size))
print("Always stay: ", float(stay_win/sample_size))