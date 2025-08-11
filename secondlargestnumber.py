a=[]
n=int(input("Enter the range :"))
for i in range(0, n+1):
    b=int(input(f"Enter the {i} number"))
    a.append(b)

a.sort()
print(f"The list is {a}")
print(f"THE SECOND Largest number is {a[-2]}")