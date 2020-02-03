# DONE

a = [20, 44, 30, 6]

# Start at last index of list a
# Increment down by step size of 1 aka -1
# Continue this until we get to -1, this is so we include index 0
# Print each element
for i in range(len(a)-1, -1, -1):
	print(a[i]),