#To find the greatest number from the user given three numbers.
p=int(input("Enter the 1st number: "))
q=int(input("Enter the 2nd number: "))
r=int(input("Enter the 3rd number: "))

if (p>q):
    if(p>r):
        print("\nThe greatest number is: ", p)
    elif(r>p):
        print("\nThe greatest number is: ", r)
elif(q>p):
    if (q>r):
        print("\nThe greatest number is: ", q)
    elif(r>q):
        print("\nThe greatest number is: ", r)