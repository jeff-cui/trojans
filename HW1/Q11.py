# DONE 

a = [2, 8, 10, 15, 17, 7]

# Get the max value of the list a
max_a = max(a)

# Iterate through list a
for i in range(0, len(a)):
	# If modulus 2 of the index is 1 then it's an odd number
	# Print out the summation of the index and max
	if a[i] % 2 == 1:
		summation = a[i] + max_a
		print(summation)


