import numpy as np

N = 100000
count_cond = 0
count_first_blue = 0

for i in range(N):
	balls = ['R'] * 5 + ['B'] * 3
	draw = np.random.choice(balls, 2, replace = False)
	if draw[0] == 'B':
		count_first_blue += 1
		if draw[1] == 'R':
			count_cond += 1

print("Simulated probability:", count_cond / count_first_blue)
print("Theoretical probability: 5/7 =", 5.0/7.0)
