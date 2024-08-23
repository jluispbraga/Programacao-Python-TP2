def calcular_consumo_medio(viagens):
  consumos = []
  total_d =  0
  total_c = 0

  for viagem in viagens:
    distancia, combustivel = viagem
    consumo_medio = distancia / combustivel if combustivel else 0
    consumos.append(consumo_medio)
    total_d += distancia
    total_c += combustivel

  consumo_medio_total = total_d / total_c if total_c else 0

  return consumos, consumo_medio_total

viagens = []

while True:
  distancia = float(input("Distancia percorrida (km) ou '0' para sair: "))
  if distancia == 0:
    break
  combustivel = float(input("Combustivel gasto (l): "))
  viagens.append((distancia, combustivel))

consumos, consumo_medio_total = calcular_consumo_medio(viagens)

for i, consumo in enumerate(consumos, start=1):
  print(f"Consumo medio de viagem {i}: {consumo:.2f} km/l")

print(f"Consumo medio total de todas as viagens: {consumo_medio_total:.2f} km/l")