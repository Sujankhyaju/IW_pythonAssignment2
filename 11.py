# Create a variable, filename. Assuming that it has a three-letter
# extension, and using slice operations, find the extension. For
# README.txt, the extension should be txt. Write code using slice
# operations that will give the name without the extension. Does your
# code work on filenames of arbitrary length?

def file_name(filename):
    return filename[:len(filename)-4]


filename =input("Enter file name with three-letter extension::")

print(f"Extension of given file is {filename[-3:]}")
print("file name without extension::",file_name(filename))

