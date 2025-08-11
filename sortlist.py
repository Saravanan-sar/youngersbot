n= int(input("ENTER THE  RANGE : "))
a=[]
for i in range(0, n):
    c= int(input(f"Enter the firstlist {i} number : "))
    a.append(c)

b=[]
m = int(input("Enter the second list Range :"))
for i in range(0,m):
    d=int(input(f"Enter the  {i} elemet of second list :"))
    b.append(d)
a.sort()
b.sort()

print(f"the 1st sorted list is : {a}")
print(f"the 2nd  sorted list is : {b}")

c= a+b
c.sort()
print(f"The merged list is :{c}")