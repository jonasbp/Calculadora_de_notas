# Programa para calcular nota de prova
# Comecou dia 18 de junho de 2016 as 08 horas da manha
# Feito por Jonas Bonfa - jonas-bonfa@hotmail.com
# Calculador para : Quimica e biologia
#variaveis
print(" ")
print ("---------------------------")
print ("--- Calculador de notas ---")
print ("---------------------------")
aberta = float(raw_input('Nota total da prova aberta (max 10.00) : '))
teste = float(raw_input('Nota total dos teste (max 10.00) : '))
lab = float(raw_input('Nota total do laboratorio (max 10.00) : '))
print ("---------------------------")
print ('Calculando...')
print ("---------------------------")

#calculador
soma = (aberta) * 5 + (teste) * 4 + (lab) * 1
total = soma / 10
print total
if total > 10 :
    print ("---------------------------")
    print('Confira suas notas,alguma esta errada!')
    print ("---------------------------")
else :

    print ("---------------------------")
    print('Sua nota no bimestre e:')
    print ("---------------------------")
    if total == 10 :
        print ('Parabens voce atingiu a nota maxima! ;)')
        print ("---------------------------")
    print total
