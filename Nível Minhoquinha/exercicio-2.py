number = int(input("Digite um número: "))
list_of_numbers = []
while number != 0:
  list_of_numbers.append(number)
  number = int(input("Digite outro número (Digite 0 para parar): "))

print(list_of_numbers)
