while True:
    try:
        print("Welcome to the Canadian to Euro converter! \n===========================")
        name = input("Please enter your name: ")
        operation = input("Convert CAD to Euro or Euro to CAD? ")
        if operation == "CAD to Euro" or operation == "cad to euro":
            cad = float(input("Enter your amount in CAD: "))
            final = cad * 0.68
            rounded = round(final, 2)
            print(name, "your $", cad, "CAD is worth $",rounded, "in Euros. ")
            break

        elif operation == "Euro to CAD" or operation == "euro to cad":
            euro = float(input("Enter your amount in Euro: "))
            final = euro * 1.48
            rounded = round(final, 2)
            print(name, "your $", euro, " Euro is worth $",rounded, "in CAD. ")
            break

        else:
            print("Invalid operation, try again. ")
            continue
    
    except ValueError:
        print("Invalid entry, try again. ")
        continue

    except:
        print("418 I'm a teapot")
        break
