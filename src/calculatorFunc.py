a = float(input("цыфра1: "))
c = input("+ или - или * или / : ")
b = float(input("цыфра2: "))

def testor():
    if o == "+":
        print(a, c, b,"=", a + b)
    elif o == "-":
        print(a, c, b,"=", a - b)
    elif o == "*":
        print(a, c, b,"=", a * b)
    elif o == "/":
        print(a, c, b,"=", a / b)
    else:
        print("Иза того что вы написали не +, -, *, / а чтото тругое мы будем плюсовать.")
        print(a, "+", b,"=", a + b)

testor()