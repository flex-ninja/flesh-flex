def issame(a,b):
       
    flag = 0
   
    for i in range(len(a)):
       
        if(a[i] == b[i]):
            flag = 1
            break
       
   
    if(flag == 1):
        print('Argumnets are identical.\nNo need of Unification.')
    else:
        print("Unification can be done.")

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
       
        print("Arguments are of different type.\nUnification can't be done.")
    else:
        issame(a,b)
   
   
   
# Predicates

a = []
b = []

na = int(input("Enter number of arguments - a : "))
nb = int(input("Enter number of arguments - b : "))
print("Enter arguments for a : ")
for i in range(na):
    t = input(f"\t{i+1}. Enter argument : ")
    a.append(t)

print("Enter arguments for b : ")
for i in range(nb):
    t = input(f"\t{i+1}. Enter argument : ")
    b.append(t)

if(na != nb):
    print("Number of arguments are not equal.\nUnification can't be done.")

if(na == nb):
    find(a,b,na,nb)


# Tools Used: AWS
# Algorithm:
# 1. If Ψ1 or Ψ2 is a variable or constant, then:
#     a) If Ψ1 or Ψ2 are identical, then returnNIL.
#     b) Else if Ψ1is a variable,
#         a. then if Ψ1 occurs in Ψ2, then return FAILURE
#         b. Else return { (Ψ2/ Ψ1)}.
#     c) Else if Ψ2 is a variable,
#         a. If Ψ2 occurs in Ψ1 then returnFAILURE,
#         b. Else return {( Ψ1/ Ψ2)}.
#     d) Else return FAILURE.
# 2: If the initial Predicate symbol in Ψ1 and Ψ2 are not same, then return FAILURE. 
# 3: IF Ψ1 and Ψ2 have a different number of arguments, then return FAILURE.
# 4: Set Substitution set(SUBST) to NIL.
# 5: For i=1 to the number of elements in Ψ1.
#     a) Call Unify function with the ith element of Ψ1 and ith element of Ψ2, and put the
#     result into S.
#     b) If S = failure then returns Failure
#     c) If S ≠ NIL then do,
#         a. Apply S to the remainder of both L1 and L2.
#         b. SUBST= APPEND(S, SUBST).
# 6: Return SUBST.
# 7.Conversion of facts into first-order logic. 
# 8.Convert FOL statements into CNF
# 9.Negate the statement which needs to prove (proof by contradiction) 
# 10.Print resolution (unification)