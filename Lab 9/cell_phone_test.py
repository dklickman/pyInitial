import cellphone

def main():
    man = input("Enter the manufacturer: ")

    mod = input("Enter the model number: ")

    retail = float(input("Enter the retail price: "))

    phone = cellphone.CellPhone(man, mod, retail)

    print(phone.get_manufact())
    print(phone.get_model())
    print(phone.get_retail_price())

main()

                
