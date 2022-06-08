def main():

    number1 = float(input("Digite o primeiro numero a ser multiplicado: "))
    number2 = float(input("Digite o segundo numero a ser multiplicado: "))

    mult = number1 * number2

    #using the f method to format variables.

    print(f"{number1:.0} vezes {number2:.0} é igual a {mult:.2}")

main()