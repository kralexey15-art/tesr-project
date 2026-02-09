a = float(input("цыфра1: "))
o = input("+ или - или * или / : ")
b = float(input("цыфра2: "))

if o == "+":
     print(a, o, b,"=", a + b)
elif o == "-":
     print(a, o, b,"=", a - b)
elif o == "*":
     print(a, o, b,"=", a * b)
elif o == "/":
     print(a, o, b,"=", a / b)
else:
     print("Иза того что вы написали не +, -, *, / а чтото тругое мы будем плюсовать.")
     print(a, o, b,"=", a + b)