# 20. Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]



class Sum:

    def SumTOZero(self,input_list):
        lst =[]
        for i in input_list:
            for j in input_list[1:]:
                for k in input_list[2:]:
                    lst1=[]
                    if (i+j+k) == 0:
                        lst1.append(i)
                        lst1.append(j)
                        lst1.append(k)
                    else:
                        continue
                    
                    if sorted(lst1) in lst:
                        continue

                    lst.append(lst1)
        
        print(lst)
        
            


array = [-25, -10, -7, -3, 2, 4, 8, 10]

a = Sum()
a.SumTOZero(array)

    




