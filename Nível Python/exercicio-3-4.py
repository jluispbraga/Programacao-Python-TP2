horas = []
temperaturas = []

def validar_hora(hora):
  return 0 <= hora <= 23

def validar_temperatura(temperatura):
  return -15 <= temperatura <= 60

def calcular_media_ponderada(horas, temperaturas):
  soma_ponderada = 0
  soma_intervalos = 0

  for i in range(1, len(horas)):
    intervalo = horas[i] - horas[i - 1]
    soma_ponderada += temperaturas[i - 1] * intervalo
    soma_intervalos += intervalo

  if soma_intervalos > 0:
    return soma_ponderada / soma_intervalos
  else:
    return 0

def avaliar_temperaturas(horas , temperaturas):
  media = calcular_media_ponderada(horas, temperaturas)
  menor_temperatura = min(temperaturas)
  maior_temperatura = max(temperaturas)
  hora_menor = horas[temperaturas.index(menor_temperatura)]
  hora_maior = horas[temperaturas.index(maior_temperatura)]

  print(f"Média ponderada das temperaturas: {media:.2f}°C")
  if 20 <= media <= 30:
    print("Temperatura dentro do intervalo de segurança")
  else:
    print("Temperatura fora do intervalo de segurança")

  print(f"Temperatura mais baixa: {menor_temperatura}°C - Hora: {hora_menor}")
  print(f"Temperatura mais baixa: {maior_temperatura}°C - Hora: {hora_maior}")

while True:
  entrada = input("Digite a hora do registro ou 'Fim' para encerrar: ")

  if entrada.lower() == 'fim':
    break

  try:
    hora = int(entrada)
    if not validar_hora(hora):
      print("Hora inválida. Digite um valor entre 0h e 23h.")
      continue
  except ValueError:
    print("Entrada inválida. Digite um valor numérico inteiro.")
    continue

  try:
    temperatura = int(input("Ddigite a temperatura registrada: "))
    if not validar_temperatura(temperatura):
      print("Temperatura inválida. Digite um valor entre -15°C e 60")
      continue
  except ValueError:
    print("Entrada inválida. Digite um valor numérico inteiro.")
    continue

  horas.append(hora)
  temperaturas.append(temperatura)

if horas and temperaturas:
  avaliar_temperaturas(horas, temperaturas)
else:
  print("Nenhum dado foi registrado.")