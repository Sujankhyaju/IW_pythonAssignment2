# 10. Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

def to_snake(string):
    snake_case = ""
    for i in string:
        if i.isupper()==True:
            snake_case += '_' + i.lower()
        else:
            snake_case += i
        
    return snake_case[1:]

def to_kebab(sep,snake_case):
    kebab_case = snake_case.replace('_',sep)
    return kebab_case

camel_case = input("Enter a Camel cased string ::")
snake_case = to_snake(camel_case)
print(snake_case)
print(to_kebab('-',snake_case))