def Sum(No):
    Sum = 0 
    for i in range(1,No+1):
        
        Sum  = Sum + i 
        
    return Sum
    


def main():
    Value = int(input("Enter the NUmber :"))

    Ret = Sum(Value)

    print(f"Sum of First N number is:{Ret}")



if  __name__ =="__main__":
    main()