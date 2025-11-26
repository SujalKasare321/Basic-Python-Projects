print("PALINDROME CHECKER!!!")

x=input("Enter the word you want to check:")

clean_x=x.replace(" ","").lower()
l=list(clean_x)

copy_l=l.copy()
copy_l.reverse()

if(l==copy_l):
    print("Its a Palindrome")
else:
    print("Its Not a Palindrome")