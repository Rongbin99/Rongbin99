#calculator
num1 = float(input("First number: ")) #obtain first number
num2 = float(input("Second number: ")) #obtain second number
op = input("What operation do you wish to perform? (+ for add, - for sub, x for multiply, / for div) ") #which operation they wish to perform

if op == "+" : #if add, do this
    ans = num1 + num2 #add the two numbers
    print("The answer is " + str(ans)) #print the final answer

elif op == "-" : #if sub, do this
    ans = num1 - num2 #sub the two numbers
    print("The answer is " + str(ans)) #print the final answer

elif op == "x" : #if multiply, do this
    ans = num1 * num2 #multiply the two numbers
    print("The answer is " + str(ans)) #print the final answer

elif op == "/" : #if divide, do this
    ans = num1 / num2 #divide the two numbers
    print("The answer is " + str(ans)) #print the final answer

else: #otherwise, do this
    print("Something went wrong, try again :(") #print the error message
