def maior_valor(x, y, z):
  if x > y and x > z:
    return x
  elif y > x and y > z:
    return y
  else:
    return z


x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))
lista_numbers = sorted([x, y, z], reverse=True)
print(f"O maior valor é: {maior_valor(x, y, z)}")
print(lista_numbers)
