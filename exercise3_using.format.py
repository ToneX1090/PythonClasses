def main():

    number1 =  float(input ("Digite o primeiro numero a ser dividido: " ))
    number2 =  float(input ("Digite o pelo qual deseja dividir: " ))

    division = number1 / number2

    #{:.2} using to show only 2 decimals
    
    print("A divisão de {0} por {1} é {2:.2}" .format(number1, number2, division))

main()