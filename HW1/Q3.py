# DONE

user_quit_flag = 1
list_of_strings = []
user_input = ''
string_found_flag = 0

while user_quit_flag == 1:
	user_input = raw_input("Enter string to be inserted into a list of strings, enter q to terminate: ")

	if user_input != 'q':
		list_of_strings.append(user_input)
		user_input = ''

	elif user_input	== 'q':
		user_quit_flag = 0

print(list_of_strings)

user_input = raw_input("Enter a string to be searched for in the list of strings: ")

for i in range(0, len(list_of_strings)):
	if user_input == list_of_strings[i]:
		string_found_flag = 1

if string_found_flag == 1:
	print("String matched at index: " + str(i))
elif string_found_flag == 0:
	print("String not found.")