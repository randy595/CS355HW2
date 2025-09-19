import numpy as np

N = 100000
count_cond = 0
count_first_red = 0

for i in range(N):
	balls = ['B'] * 7 + ['R'] * 5
	draw = np.random.choice(balls, 2, replace = False)
	if draw[0] == 'R':
		count_first_red += 1
		if draw[1] == 'B':
			count_cond += 1

print("Simulated probability:", count_cond / count_first_red)
print("Theoretical probability: 7/11 =", 7.0/11.0)