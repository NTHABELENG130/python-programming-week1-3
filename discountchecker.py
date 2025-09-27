age=int(input("enter your age:"))
is_student=input("are you a student?(yes/no:").lower()=="yes"

if age<=18:
	print("you qualify for 60% discount.")
	
elif age>=60:
	print("you qualify for a 30% discount.")
	
elif age <60 and is_student:
	print("you qualify for a 20% discount.")
	
else:
	print("sorry , no discont available")