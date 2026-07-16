No = int(input("Enter the Number:"))

Num1 = No
Num2 = 0

while No > 0:
    iDigit = No % 10 
    Num2 = (Num2    * 10)+ iDigit 
    No = No //  10 

if Num1 == Num2:
    print("Number is palindrome")
else:
    print("Not a Palindrome")


