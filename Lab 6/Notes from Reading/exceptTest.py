def main():
    try:
        num1 = int(input("number 1: "))
        num2 = int(input("number 2: "))
        result = num1 / num2
        print(result)
    except ZeroDivisionError:
        print("Cannot Divide by Zero.")
        num2 = int(input("number 2: "))
        

main()
