nota_01 = int(input("informe a nota 1;"))
nota_02 = int(input("informe a nota 2;"))
nota_03 = int(input("Informe a nota 3;"))
nota_04 = int(input("infrom a note  4;"))
notas = [nota_01, nota_02, nota_03, nota_04]

maxima = (max(notas))
minimo = (min(notas))
soma = (sum(notas))

print(f"Informo que sua nota maxima é {maxima}, nota minima é {minimo} soma é {soma}")


media = sum(notas)/len(notas)
# print(f"A média é igual a {media}")
if media >= 6 ,
    print("Parabens! Você está aprovado!")    
else    