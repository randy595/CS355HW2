#I/We _____Rand Ashour__________ declare that I/We have completed 
# this computer code in accordance with the UAB Academic Integrity Code and the UAB CS Honor Code.  
# I/We have read the UAB Academic Integrity Code and understand that any breach of the Code may result in severe 
#penalties.	
#Student signature(s)/initials: _____R.A_______	
#Date: ______9/19/2025______*/


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