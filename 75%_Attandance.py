'''to allow
student to sit if he/she has medical cause.
Ask user if he/she has medical 
cause or not ( 'Y' or 'N' ) and print accordingly.'''

a = int(input("Number of classes held: "))
b = int(input("Number of classes attended: "))
percentage = (b/a)*100
if(percentage>=75):
    print(f"Your percentage is {percentage}% you are allowed to exam.")
elif(percentage<75):
    c = input("Any medical cause 'Y' or 'N': ")
    if(c=="Y"):
        d = percentage+10
        p = round(d,2)
        if(p>=75):
            print(f"You will get additional 10% now your attendance is {p}% you are allowed in exam")
        else:
            print("You will get 10% additional due to medical cause")
            print("sorry your attandance is still not 75% or above")
    else:
        d = percentage
        p = round(d,2)
        print(f"Your percentage is {p}% you are not allowed exam")
else:
    print(f"Your percentage is {percentage}% you are not allowed to exam")