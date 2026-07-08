def ChkSquare(Value):
    Square = Value*Value #Value**2
    return Square


def main():
    No1 = int(input("Enter The Number:"))
    
    Ret = ChkSquare(No1)
    print(f"Square of {No1} is {Ret}")


if __name__ == "__main__":
    main()