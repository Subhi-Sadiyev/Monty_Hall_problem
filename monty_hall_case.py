### Monty hall problem simulation based on the example by Youtuber baraltech

import matplotlib.pyplot as plt
import random

### Monthy Hall case

prizecount = 0
choicecount = 0

iterations = 10000
prize_counts = []


for i in range(iterations):
    doors = ["Choice","Choice","Choice"]
    doors[random.randint(0,2)] = "Prize"

    if doors[1] == "Choice":
        doors.pop(1)
    elif doors[2] == "Choice":
        doors.pop(2)

    chosen_door = doors[1]

    if chosen_door == "Prize":
        prizecount += 1
    else:
        choicecount += 1
  # 
  # Store the count of wins at each iteration
    prize_counts.append(prizecount)

# Calculating the percentage of wins
win_percentages = [prize_count / (i + 1) * 100 for i, prize_count in enumerate(prize_counts)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(range(iterations), win_percentages, label='Qalib gəlmə faizi', color='red')
plt.xlabel('İterasiyalar')
plt.ylabel('Qalib gəlmə faizi (%)')
plt.title('Seçim dəyişikliyi edildikə iterasiyalar üzrə qalib gəlmə faizi')
plt.legend()
plt.grid(True)
plt.show()

print(f"Monty hall case - Prize: {prizecount} = {round(prizecount/iterations*100,1)}%")
print(f"Monty hall case - Choice: {choicecount} = {round(choicecount/iterations*100,1)}%")


