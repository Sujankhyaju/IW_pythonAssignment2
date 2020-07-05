# 6. Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

sample_list = ['James', 'john','nabin','hari','sita','rita']
flag = 1
for i in sample_list:
    if i.title() == 'John':
        print("Search Found!!")
        break

else:
    print("Search Not Found!!")


