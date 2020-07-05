# 7. Create a list of tuples of first name, last name, and age for your friends and colleagues. If you don't know the age, put in None. Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the average age

sample_list= [('nabin','hyan',22),('ajit','nakarmi',23),('sagar','koju',21),('subash','shrestha',20)]
sum =0
for i in sample_list:
    sum += i[-1]
else:
    avg = sum/len(sample_list)

for i in sample_list:
    if i[-1] < avg:
        print(f"-->> {i[0].title()} is younger than the average age {avg}\n")
    else:
        print(f"-->> {i[0].title()} is older than the average age {avg}\n")





