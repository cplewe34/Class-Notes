#numbers = [2,1,2,5,6,5,7]
#list = []
#duplicates = []
#for i in range(0, len(numbers)-1):
#    for j in range(i+1, len(numbers)):
#        if numbers[i] == numbers[j]:
#            duplicates.append(numbers[i])
#        else:
#            list.append(numbers[i])
#print(f"The unique numbers are: {list}")


#list_check = []
#double_number = []
#single_number = []

#for i in numbers:
   # if i in list_check:
  #      double_number.append(i)
 #   else:
#        list_check.append(i)

#for i in list_check:
#    if i not in double_number:
#        single_number.append(i)

#print(f"The unique numbers are: {single_number}")

numbers = [2,1,2,5,6,5,7]
duplicates = []
unique_numbers = []



for i in range(len(numbers)-1):
   for j in range(i+1,len(numbers)):
      if numbers[i] == numbers [j]:
            duplicates.append(numbers[i])
   

for num in numbers:
    if num not in duplicates:
        unique_numbers.append(num)

print(unique_numbers)




         
       