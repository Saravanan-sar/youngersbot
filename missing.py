n = int(input("Enter a range :"))
list = []
for i in range(1, n):
    list.append(i)
print(list)
new= [1, 3, 3, 5]

for i in range(0, len(list)):
    for j in range(0, len(new)):
        if n[i]== new[j]:
            continue
        else:
            print(f"the missing Number is in  {i} postion")
            print(n(i))
        