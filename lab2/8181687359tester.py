import subprocess
import random
import math

# Initialize lists for the 10000 random x,y pairs and d values
xlist = []
ylist = []
dlist = []

# Create results.txt file for writing
f = open("8181687359results.txt", "w")

# For 10000 times
for i in range(10000):
	# Create random x that ranges from -100 to 100, add to list
	x = random.uniform(-100, 100)
	xlist.append(x)

	# Create random y that ranges from -100 to 100, add to list
	y = random.uniform(-100, 100)
	ylist.append(y)

	# Create random d that ranges from 0 to 100
	d = random.uniform(0, 100)
	dlist.append(d)

	# Compute Zblackbox using subprocess.check_output to use our C code from part 1
	# Arguments passed are the call to use ./blackbox, current x, y and d value for main line arguments
	Zblackbox = subprocess.check_output(["./8181687359blackbox", str(xlist[i]), str(ylist[i]), str(dlist[i])])

	# Compute Zcomputed which is only z = x^2 + y^2
	Zcomputed = math.pow(xlist[i],2) + math.pow(ylist[i],2)

	# Compute the difference between Zblackbox and Zcomputed
	difference = abs(float(Zblackbox)-Zcomputed)

	# Write the difference to results.txt
	f.write(str(difference) + "\n")




