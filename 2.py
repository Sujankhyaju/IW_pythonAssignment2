
#2. Write an if statement to determine whether a variable holding a year is a leap year.

input_year = int(input("Enter a year::"))

if input_year % 4 ==0:
    if input_year %100 ==0:
        print(f"{input_year} is Leap Year.") if input_year %400==0 else print(f"{input_year} is Not Leap Year.")
            
        

    else:
        print(f"{input_year} is Leap Year.")
else:
    print(f"{input_year} is Not Leap Year.")