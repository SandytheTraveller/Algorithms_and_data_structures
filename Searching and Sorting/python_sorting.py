# standard sorting of a list
alist = [5, 2, 3, 1, 4]
alist.sort() # sort in ascending order
print(alist)
alist.sort(reverse=True)
print(alist)


# sorting the list using a lambda function
student_list = [('john', 14, 'B'), ('claire', 10, 'C'), ('dave', 10, 'B'), ('matt', 15, 'A')]
# sort using the second element of the tuple as key
student_list.sort(key=lambda x: x[1])
print(student_list)

# we can specify multiple keys, the criteria will be applied in order
student_list.sort(key=lambda x:(x[1], x[2]))
print(student_list)


# sorting a list using a lambda function referred to another structure
student_age_dict = {"john": 14, "claire": 10, "dave": 10, "matt": 15}
student_name_list = ["john", "claire", "dave", "matt"]

# sort the list using the data in the dictionary
# the values in the list are keys for the dictionary so that
# we can use the value stored in the
# dictionary to order the list
student_name_list.sort(key=lambda x: student_age_dict[x])
print(student_name_list)

# sort the list using the data in the dictionary in reverse order
student_name_list.sort(key=lambda x:-student_age_dict[x])
print(student_name_list)