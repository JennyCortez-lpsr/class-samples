rint("These are the 5 family members I spend the most time with:")

fam = ["Mom","Carlos","Alex","Dad","Danny"]

num = 1

fam.append('Ivett')
fam.append('Jacky')
fam.append('Maria')
fam.append('Andrea')
fam.append('Pilar')

fam.sort()

fam.reverse()

print("Updated list: ", fam)
for current_fam in fam:
	current_fam = str(current_fam)
   	print(str(num) + current_fam) 
   	num = num + 1

