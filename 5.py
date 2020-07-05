# 5. Create a tuple with your first name, last name, and age. Create a list, people, and append your tuple to it. Make more tuples with the corresponding information from your friends and append them to the list. Sort the list. When you learn about sort method, you can use the key parameter to sort by any field in the tuple, first name, last name, or age.

name= ("firstName","lastName","age")
people = []
people.append(name)

name1=("nabin","hyan",22)
name2=("babin","khyaj",20)
name3=("sabin","shres",19)
name4=("nabina","nakara",26)

people.append(name1)
people.append(name2)
people.append(name3)
people.append(name4)

print(people)

print(sorted(people,key:age)) 

