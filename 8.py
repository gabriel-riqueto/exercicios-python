nomeVend= (input("Nome do vendedor: "))
carros= float(input("Quant de carros vendidos: "))
valorTot= float(carros*60000)
salario= float(2500+200*carros+2/100*valorTot)
print(f"O {nomeVend} vendeu {carros} carros e seu salario foi de {salario}")