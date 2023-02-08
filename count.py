s=input("enter any string") 
c=input("enter any char:") 
n=int(input("enter no of elements in string")) 
Count=0
for i in range (n):
    if s[i]==c:
         Count+=1
print (Count)