list = [1,1,2]
n= len(list)
print(n)
a = []
b=[]
c=[]
for i in range(0, n):
    a.append(list[i])
print(a)

for i in range(1, n):
    b.append(list[i])
    
b.append(list[0])
print(b)

c= (list[::-1])
print(c)
