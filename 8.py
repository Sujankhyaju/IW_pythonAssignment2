def is_prime(num):
    if num<=2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False

            else:
                return True

num = int(input("Enter a number::"))
print(f"{num} is not prime") if is_prime(num)==False else print(f"{num} is prime")