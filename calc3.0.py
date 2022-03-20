#calculator v3
def calculator(): #function of calc
    global num1, num2, op, ans, start #variables used in this function
#    start = input("Start calculator? (Yes/No) ")
#    if start == "yes" or "Yes" or "YES":
#        start = "yes"
#        
#    else:
#        start == "no"
#                
#
    while True: #while loop
        try: #input commands
            num1 = float(input("First number: ")) #obtain first number
            num2 = float(input("Second number: ")) #obtain second number
            op = input("What operation do you wish to perform? (+ for add, - for sub, x for multiply, / for div) ")
            #obtain which operation the user wishes to perform

            if op == "+": #if add, add the two numbers
                ans = num1 + num2 #command to perform the operation
                print("The answer is " + str(ans)) #prints the final answer
                break #stops the program

            elif op == "-": #if sub, sub the two numbers
                ans = num1 - num2
                print("The answer is " + str(ans))
                break

            elif op == "x": #if multiply, multiply the two numbers
                ans = num1 * num2
                print("The answer is " + str(ans))
                break

            elif op == "/": #if divide, divide the two numbers
                ans = num1 / num2
                print("The answer is " + str(ans))
                break

            else: #if anything else is given, print invalid operation
                print("Invalid operation. ")
                continue #tries the loop again

        except ValueError: #when user input is incorrect, prints this message
            print("Invalid input, try again. ")
            continue

        except ZeroDivisionError: #when its devide by 0, prints this message
            print("Cannot divide by 0. ")
            continue

        except: #prints error message
            print("Something went wrong. ")
            break

calculator()
