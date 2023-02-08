list=eval(input("enter list1: "))
len=0
for i in list:
    len+=1
pos=int(input("enter the position (positive):"))
l2=[]
x=0
for k in range (len):
    l3=[list[k]]
    if k!=pos:
        l2+=l3
list=l2
print(list)
    
