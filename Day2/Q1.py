def addition(num1,num2=200): #ex of default function arguments
    return(num1+num2)

n1=input("Enter first number: ")
n2=input("Enter second number: ")
ans_add=addition(num1=n1, num2=n2)
print "Addition of %f and %f is %f"%(n1,n2,ans_add)
