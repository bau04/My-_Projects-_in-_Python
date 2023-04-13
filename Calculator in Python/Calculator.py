print("Calculator")

sign = input("Choose an operator: + - * / % \n")
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

Sum = float(n1) + float(n2)
Dif = float(n1) - float(n2)
Prod = float(n1) * float(n2)
Quo = float(n1) / float(n2)
Mod = float(n1) % float(n2)

match sign:
    case '+' :
        print("Sum : " , Sum)

    case '-' :
        print("Difference : " , Dif)

    case '*' :
        print("Product : " , Prod)

    case '/' :
        print("Quotient : " , Quo)

    case '%' :
        print("Modulo : " , Mod)
