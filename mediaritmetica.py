def calculo(x):
    soma = sum(x)
    media = soma / len(x)
    return media

print('insira os valores:\n')

lista = []

while True:
    notas = float(input())
    if notas < 0:
        break
    lista.append(notas)

media = calculo(lista)
if media > 5:
    print('A média {:.3f} está acima do limiar estabelecido'.format(media))
else:
    print('{:.3f}'.format(media))