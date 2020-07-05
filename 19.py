# 19. Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,


class Paranthesis:     

    def CheckValidityOfParanthesis(self,para):
        count =[]
        # print(para)
        for paran in para:

            if paran=='[' or paran =='{' or paran =='(':
                count.append(paran)
            
            else:
                top_count =count[-1]

                if (top_count =='[' and paran==']') or (top_count=='{' and paran=='}') or (top_count=='(' and paran==')'):
                    count.pop()
        
        if not count:
            print("Valid Paranthesis")
        
        else:
            print("Invalid")

input_p = "[{()()}]"
input1="[]{}()"
test = Paranthesis()
test.CheckValidityOfParanthesis(input_p)
test.CheckValidityOfParanthesis(input1)


                