'''Essas funções foram criadas com o propósito de realizar a criação das contas, além de controlar as entradas, aceitando apenas números onde são necessários e o mesmo se vale para strings.'''
import funcoesDeEntrada
def criarContas (quantContas, contas, senhaDasContas, saldoDaconta):
  for i in range(quantContas):
    codigo = input("Digite um código de identificação : ")
    while True :
      if codigo.strip() == "":
        print("O campo não pode ficar vazio.")
      elif not codigo.isdigit():
        print("O código deve conter apenas números.")
      elif codigo in contas:
        print("Erro! Conta já cadastrada.")
      else : 
        break
      codigo = input("Digite outro código : ")
    contas.append(codigo)
    
    senha = input("Digite sua nova senha : ")
    while True :
      if senha.strip() == "":
        print("O campo não pode ficar vazio.")
      elif not senha.isdigit():
        print("A senha deve conter apenas números.")
      else :
        break
      senha = input("Digite outra senha : ")
    senhaDasContas.append(senha)
    saldoDaconta.append(0)
    
    print("Conta criada com sucesso.")
    
    
def controlarCodigo (codigo):
  while True :
    if codigo.strip() == "":
      print("O campo não pode ficar vazio.")
    elif not codigo.isdigit():
      print("O código deve conter apenas números.")
    else : 
      return codigo
    codigo = input("Digite outro código : ")
    
def controlarSenha (senha):
    while True :
      if senha.strip() == "":
        print("O campo não pode ficar vazio.")
      elif not senha.isdigit():
        print("A senha deve conter apenas números.")
      else :
        return senha
      senha = input("Digite outra senha : ")