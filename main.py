import importlib.util
import os
"""
 Arquivo main.py 
 Objetivo - Executar os arquivos.py do TP2 de programção python
 Apertar Ctrl + Enter para executar
"""


def listar_pastas(caminho):
  """
    Listagem dos diretorios
  """
  return [
      f for f in os.listdir(caminho)
      if os.path.isdir(os.path.join(caminho, f)) and not f.startswith(".")
  ]


def listar_arquivos(caminho):
  """
    Listagem dos arquivos
  """
  return sorted([
      f for f in os.listdir(caminho)
      if os.path.isfile(os.path.join(caminho, f)) and f.endswith(".py")
  ])


def executar_arquivo(arquivo):
  """
    Executação dos arquivos
  """
  spec = importlib.util.spec_from_file_location("module_name", arquivo)
  if spec is not None:
    mod = importlib.util.module_from_spec(spec)
    if spec.loader is not None:
      spec.loader.exec_module(mod)
    else:
      print(f"Erro não foi possível executar o arquivo {arquivo}")
  else:
    print(f"""Erro: não foi possível criar a especificação do módulo para
    o arquivo {arquivo}""")


def main():
  caminho_base = os.getcwd()
  pastas = listar_pastas(caminho_base)

  if not pastas:
    print("Nenhuma pasta encontrada")
    return

  print("Escolha uma pasta:")
  for i, pasta in enumerate(pastas, 1):
    print(f"{i}. {pasta}")

  try:
    escolha_pasta = int(input("Digite o número da pasta: "))
    if escolha_pasta < 0 or escolha_pasta > len(pastas):
      print("Escolha invalida!")
      return
  except ValueError:
    print("Escolha invalida!")
    return

  pasta_escolhida = pastas[escolha_pasta - 1]
  caminho_pasta = os.path.join(caminho_base, pasta_escolhida)
  arquivos = listar_arquivos(caminho_pasta)

  if not arquivos:
    print("Nenhum arquivo encontrado")
    return

  print(f"\nArquivos na pasta {pasta_escolhida}:")
  for i, arquivo in enumerate(arquivos, 1):
    print(f"{i}. {arquivo}")

  try:
    escolha_arquivo = int(input("Digite o número do arquivo: "))
    if escolha_arquivo < 0 or escolha_arquivo > len(arquivos):
      print("Escolha invalida!")
      return
  except ValueError:
    print("Escolha invalida!")
    return

  arquivo_escolhido = arquivos[escolha_arquivo - 1]
  caminho_arquivo = os.path.join(caminho_pasta, arquivo_escolhido)
  print(f"\nExecutando arquivo {arquivo_escolhido}... \n")
  executar_arquivo(caminho_arquivo)


if __name__ == "__main__":
  while True:
    main()
    print("\nFim da execução \n")
    continuar = input(
        "Deseja verificar outro arquivo? (s/n): ").strip().lower()
    if continuar not in ("s", "sim"):
      break
