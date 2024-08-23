def gerar_lista_pares(n):
  lista_pares = []
  for i in range(0, n + 1):
    if i % 2 == 0:
      lista_pares.append(i)
  return lista_pares


number = int(input("Ate qual numero deve ser gerada a lista? "))
print(gerar_lista_pares(number))
