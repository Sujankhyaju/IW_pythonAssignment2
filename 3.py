# 3. Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text

paragraph = "He listen silent cat act people eye dog god use sue "

anagrams = []
lst = paragraph.lower().split()


for i in lst:
    for j in lst:
        if sorted(i) == sorted(j) and i !=j:
            anagrams.append(i)

print(anagrams)