import math
print("SUPER CALCULADORA DE COEFICIENTE")


while True:
    parcelaspagas = int(input ("Parcelas Pagas:: "))
    parcelasrestantes = int(input("Parcelas Restantes::"))
    valorparcelas = float(input ('valor da parcela ::'))

    resto = parcelasrestantes - parcelaspagas
    total = resto * valorparcelas
    porce = total * 0.2
    
    new = total - porce
    
    print (new)

    
    co1 = 0.024360
    co2 = 0.023491
    co3 = 0.0212019

    valor_red = float(input("Valor parcela que reduzida"))

    um = valor_red / co1
    dos = valor_red / co2
    tres = valor_red / co3



    valor1 = math.ceil(um)
    valor2 = math.ceil(dos)
    valor3 = math.ceil(tres)
    
    print()

   
    print (valor1, valor2, valor3)

    input()
