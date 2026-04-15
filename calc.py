def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"
print(f"\nKalkulator:")
input_a = float(input("Podaj pierwszą liczbę: "))
input_b = float(input("Podaj drugą liczbę: "))    
input_operator = input("Podaj operator (+, -, *, /): ")
if input_operator == "+":
    print(f"{input_a} + {input_b} = {dodaj(input_a, input_b)}")
elif input_operator == "-":
    print(f"{input_a} - {input_b} = {odejmij(input_a, input_b)}")
elif input_operator == "*":
    print(f"{input_a} * {input_b} = {pomnoz(input_a, input_b)}")
elif input_operator == "/":
    print(f"{input_a} / {input_b} = {podziel(input_a, input_b)}")
else:
    print("Nieznany operator!") 
