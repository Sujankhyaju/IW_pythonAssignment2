# 3. Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text

paragraph = "He listen silent cat act people eye dog god use sue "

lst = paragraph.split()

for i in range(len(lst)):
    for j in range(i,len(lst)):
        if sorted(lst[i]) == sorted(lst[j]):
            print(lst[i])
    
