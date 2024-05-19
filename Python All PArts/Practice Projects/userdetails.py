# data = [name, age, address, country, salary]

data = []
print("Enter Your Data :")
# a = input("Enter Your Name")
# data.append(a)
 
data.append(input("Enter Your Name"))
data.append(int(input("Enter Age")))
data.append(input("Enter Your Address"))
data.append(input("Enter Your Country"))
data.append(int(input("Enter Your Salary")))

print("Your Name is ",data[0])
print("Your Age is ",data[1])
print("Your Address is ",data[2])
print("Your Country is ",data[3])
print(f"Your Salary is {data[4]}")
