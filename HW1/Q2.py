# DONE

a = [6, 14, 19, 24, 6, 7, 6, 24, 1, 3]

# Iterate from first element to second to last element of list a
# This is because with our program the last element will always be unique
for i in range(0, len(a)-1):
	# Check value is the value at index i we will compare other elements to
	check_value = a[i]

	# For an index j that goes from range i+1 to last element of list a
	for j in range(i+1, len(a)):
		# See if the check_value = value at index j, if so then the element is not 
		# unique and set that element to 0 and the element at index i
		if a[j] == check_value:
			a[j] = 0
			a[i] = 0

# Print all unique elements
print("The unique elements are: ")

# By this point all unique elements are nonzero so print
for i in range(0, len(a)):
	if a[i] != 0:
		print(a[i]),
