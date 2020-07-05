# Create a list. Append the names of your colleagues and friends to it.Has the id of the list changed? Sort the list. What is the first item on the list? What is the second item on the list?

sample_list = []

for _ in range(5):
    name = input("Enter a name::")

    sample_list.append(name)
before_id=id(sample_list)

sample_list.sort()
after_id=id(sample_list)
print("id is same") if before_id == after_id else print("Not same")

print(sample_list[0], sample_list[1])