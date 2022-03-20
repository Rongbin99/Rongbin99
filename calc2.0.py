#calculator v2
def calculator(): #function of calc
    global num1, num2, op, ans #variables used in this function
    #input commands
    num1 = float(input("First number: ")) #obtain first number
    num2 = float(input("Second number: ")) #obtain second number
    op = input("What operation do you wish to perform? (+ for add, - for sub, x for multiply, / for div) ") #obtain which operation the user wishes to perform
    
    while True: #while loop 
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

        else: #otherwise, print the error message
            print("Something went wrong, try again.")
            break


calculator()