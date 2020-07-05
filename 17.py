# 17. Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.

def calculation(num1,num2,option):
    if option == 1:
        return num1+num2
    
    elif option == 2:
        return num1 - num2
    
    elif option == 3:
        return num1 * num2
    
    elif option == 4:
        return 'Error' if num2<1 else (num1/num2)
    
    else:
        return "Invalid Option"


options = ['ADD','SUBTRACT','MULTIPLY','DIVIDE']



for _ , action in enumerate(options,start=1):
    print(f"{_}. {action}")

option = int(input("Choose Your Option::"))
num1 = int(input("Enter 1st number::"))
num2 = int(input("Enter 2nd number::"))
print(calculation(num1,num2,option))


