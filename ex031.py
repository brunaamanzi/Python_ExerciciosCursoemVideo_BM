#desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km, e R$0,45 para viagens mais longas.
distancia_km = float(input('Informe a distância da viagem em km: '))
print('Você está prestes a iniciar uma viagem de {}km.'.format(distancia_km))
#outra forma de fazer a condição composta
#preço = distancia_km * 0.5 if distancia_km <= 200 else distancia_km * 0.45
if distancia_km <= 200:
    print('Sua viagem é de até 200km. O preço da passagem é de R${:.2f}.' .format(distancia_km*0.5))
else:
    print('Sua viagem ultrapassa os 200km. O preço da passagem é de R${:.2f}.' .format(distancia_km*0.45))