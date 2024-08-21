def create_list_of_numbers(N): 
 num_list = [] 
for i in range(N): 
num = float(input(f"Enter number {i + 1}: ")) 
num_list.append(num) 
return num_list
N = int(input("Enter the number of elements you want to input: ")) 
user_numbers = create_list_of_numbers(N) 
print("List of user-inputted numbers:", user_numbers)
