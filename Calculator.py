def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    if(y==0):
        return "ERROR! Cant divide by zero"
    return x/y
print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
n=int(input("Enter Choice(1/2/3/4):"))
num1=float(input("Enter 1st number:"))
num2=float(input("Enter 2nd number:"))
if(n==1):
    print("Result:",add(num1,num2))
elif(n==2):
    print("Result:",sub(num1,num2))
elif(n==3):
    print("Result:",mult(num1,num2))
elif(n==4):
    print("Result:",div(num1,num2))
else:
    print("Invalid Input")