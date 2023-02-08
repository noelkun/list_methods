list2=eval(input("Enter list2: "))
element=eval(input("Enter search element: "))
index=0
if element in list2:
    for i in list2:
        if element==i:
           break
        index+=1
else:
    print("Index = -1")
print("Index =",index)