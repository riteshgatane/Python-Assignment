def RevDigits(Value):
    iDigit = 0 
    count = 0 
    Sum = 0 
    Rev = 0
    while(Value != 0 ):
        iDigit = Value % 10
        Rev =Rev* 10 +iDigit
        Value = Value // 10 
    return Rev

def main():
    No = int(input("Enter the Number to Check:"))
    Ret = RevDigits(No)
    print("Reverse of Digits of the Number :",Ret)

if __name__ == "__main__":
    main()