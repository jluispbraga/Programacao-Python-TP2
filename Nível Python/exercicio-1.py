valor_inicial = float(input("Digite o valor inicial: "))
taxa_de_juros = float(input("Digite a taxa de juros: "))
anos = int(input("Digite o numero de anos: "))


def calcular_investimentos(vi, tj, a):
  valores_anuais = []
  for ano in range(1, a + 1):
    vf = round((vi * (1 + tj / 100)**ano), 2)
    valores_anuais.append("R$ " + str(vf))
    print(f"Valor final do ano {ano}: R$ {vf}")
  return valores_anuais


print(calcular_investimentos(valor_inicial, taxa_de_juros, anos))
