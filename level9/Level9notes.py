#a boolean is immutable, meaning that once it is created, it cannot be changed.
#a dictionary is mutable, meaning that it can be changed after it is created.
#immutable is it cant be changed because only 1 variable
#mutable can be a list and stuff like that. Store adress to the value
#stack(LIFO) remove items to get to the bottem
#Queue(FIFO) first one goes out

some_rando_list = []

some_rando_list.append("blah")

print(some_rando_list)

some_rando_list.extend(["yadda", "hello", "ahoy"])


#print(some_rando_list) would print whole list

#-1 would print the last one because it goes back to the list
#2 prints the 3rd one because remember it starts at 0
#print(some_rando_list[2])


#makes last one in pop out when print
#if pop(1) it romeves yadda because it is second
#some_rando_list.pop()

#removes blah from list
#some_rando_list.remove("blah")

#would tell how manyinstances are in the list
#print(some_rando_list.count("blah"))

#looks at list
#if "yadda" in some_rando_list:
    #print("Found the word")
#else:
    #print("word not there")

#some_rando_list.sort()

#.insert() put something in a specific spot

#tuple is a list that you can not change once it is set
#stores smaller and runs faster

#set compares things together

print(some_rando_list)


student_info = {
    "name": "zendaya",
    "age": 30,
    "graduated": False
}

