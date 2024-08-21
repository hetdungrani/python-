def check_devisible(number):
    if number%5==0 and number%11==0:
        return 1
    else:
        return 0

number=int(input("enter a number:"))
if check_devisible(number):
        print("number is devisible...")
else:
        print("number is not devisible...")
            


