#Create a dictionary where the keys are numbers from 0 to 20 inclusive, and the values are
#1. -1 if the key value is divisible by 5
#2. 1 otherwisemy_dict = {i: -1 if i % 5 == 0 else 1 for i in range(21)}
my_dict = {i: -1 if i % 5 == 0 else 1 for i in range(21)}
print(my_dict)
