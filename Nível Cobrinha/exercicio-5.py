def exibir_mensagem(mensagems, repeticoes=1):
  for i in range(repeticoes):
    print(mensagems)


mensagem = input("Escreva uma mensagem: ")
repeticoes = int(input("Quantas vezes deseja repetir a mensagem? "))

exibir_mensagem(mensagem, repeticoes)
