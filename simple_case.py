### simple case of Monty hall game based on Youtuber baraltech example

import matplotlib.pyplot as plt
import random

prizecount1 = 0
choicecount1 = 0

iterations1 = 10000

prize_iteration_counts1 =[]



for i in range(iterations1):
    doors1 = ["Choice","Choice","Choice"]
    doors1[random.randint(0,2)] = "Prize"

    chosen_door1 = doors1[random.randint(0,2)]

    if chosen_door1 == "Prize":
        prizecount1 += 1
    else:
        choicecount1 += 1

    prize_iteration_counts1.append(prizecount1)


win_percentages = [prize_iteration_counts1 / (i + 1) * 100 for i, prize_iteration_counts1 in enumerate(prize_iteration_counts1)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(range(iterations1), win_percentages, label='Percentage of Wins', color='red')
plt.xlabel('Iterations')
plt.ylabel('Percentage of Wins (%)')
plt.title('Percentage of Wins Over Iterations in Simple case')
plt.legend()
plt.grid(True)
plt.show()

print(f"Simple case - Prize: {prizecount1} = {round(prizecount1/iterations1*100,1)}%")
print(f"Simple case - Choice: {choicecount1} = {round(choicecount1/iterations1*100,1)}%")

