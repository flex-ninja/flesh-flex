def issame(a,b):
   
    flag = 0
   
    for i in range(len(a)):
       
        if(a[i] == b[i]):
            flag = 1
            break
       
   
    if(flag == 1):
        print('Argumnets are same, unification cannot be done.')
    else:
        print("unification can be done")

def find(a,b,na,nb):
    flag = 0
    for i in range(na):
       
        if(a[i] >= '0' and a[i] <='9'):
           
            if(b[i] >= '0' and b[i] <= '9'):
                flag = 0
            else:
                flag = 1
       
        elif(a[i] >= 'a' and a[i] <= 'z'):
           
            if(b[i] >= 'a' and b[i] <= 'z'):
                flag = 0
            else:
                flag = 1
   
    if flag == 1:
       
        print("arguments are of different type")
    else:
        issame(a,b)
   
   
   

a = []
b = []

na = int(input("enter number of arguments: "))
nb = int(input("enter number of arguments: "))
print("Enter arguments for a")
for i in range(na):
    t = input("enter argument ")
    a.append(t)

print("Enter arguments for b")
for i in range(nb):
    t = input("enter argument ")
    b.append(t)

if(na != nb):
    print("number of parameters are not equal")

if(na == nb):
    find(a,b,na,nb)