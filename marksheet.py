rno=input("Enter Student Roll Number :")
sname=input("Enter Student Name :")
sub1=int(input("Enter marks of Physics: "))
sub2=int(input("Enter marks of Chemistry: "))
sub3=int(input("Enter marks of Biology: "))
sub4=int(input("Enter marks of Mathematics: "))
sub5=int(input("Enter marks of Computer: "))
tot=sub1 + sub2 + sub3 + sub4 + sub5
avg=tot / 5
print("Student Roll No is : ",rno)
print("Student Name is :",sname)
print("Marks of Physics:",sub1)
print("Marks of Chemistry:",sub2)
print("Marks of Biology:",sub3)
print("Marks of Mathematics:",sub4)
print("Marks of Computer:",sub5)
print("Total Marks : ",tot)
print("Percentage Marks : ",avg)
if(avg>=90):
         print("grade:A")
elif(avg>=80):
         print("Grade: B")
elif(avg>=70):
          print("Grade: C")
elif(avg>=60):
         print("Grade: D")
elif(avg>=40):
         print("Grade: E")
else:
         print("Grade: F")

      



 





 
