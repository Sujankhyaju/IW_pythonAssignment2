# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

def binary_search(sequence,key):
    for i in range(len(sequence)):
        if sequence[i] == key:
            return i
        
    else:
        return -1

sequence=input("Enter a string::")
key = input("Enter a key to search::")
print("search found!!") if (binary_search(sorted(sequence),key) !=-1) else print("search not found")
