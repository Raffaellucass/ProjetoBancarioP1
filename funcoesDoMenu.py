import sys, funcaoAutenticacao
def menu (controleMenu, contas, senhaDasContas, saldoDaconta, codigoVerificado, senhaVerificada, indiceDaConta, conta):
  while True :
    if (controleMenu == "1" ):
      valor = (input("Digite o valor : "))
      valorFormatado = funcaoAutenticacao.autenticadorDeValor(valor)
      senha = input("Para proseguirmos, digite sua senha : ")
      funcaoAutenticacao.autenticadorDeSenha(senha, senhaDasContas, indiceDaConta)
      saldoDaconta[indiceDaConta] += valorFormatado
      break
    elif (controleMenu == "2"):
      print(f"Seu saldo bancário : {saldoDaconta[indiceDaConta]}")
      valor = (input("Digite o valor : "))
      valorFormatado = funcaoAutenticacao.autenticadorDeValor(valor)
      if valorFormatado <= saldoDaconta[indiceDaConta]:
        senha = input("Para proseguirmos, digite sua senha : ")
        funcaoAutenticacao.autenticadorDeSenha(senha, senhaDasContas, indiceDaConta)
        saldoDaconta[indiceDaConta] -= valorFormatado
        print(f"Seu saldo bancário atual : {saldoDaconta[indiceDaConta]}")
        break
      else :
        print("Saldo insuficiente.")
        break
    elif (controleMenu == "3"):
      print(f"Seu saldo bancário : {saldoDaconta[indiceDaConta]}")
      print(f"Não tente sair como esperto, caso digite o código de sua conta, o valor se manterá o mesmo. \nContas disponíveis : {contas}")
      codigo = input("Informe o código da conta que vai receber a transferência : ")
      indiceDaContaRecebedora = funcaoAutenticacao.autenticadorDeConta(codigo, contas)
      valor = (input("Digite o valor :"))
      valorFormatado = funcaoAutenticacao.autenticadorDeValor(valor)
      if valorFormatado <= saldoDaconta[indiceDaConta]:
        senha = input("Para proseguirmos, digite sua senha : ")
        funcaoAutenticacao.autenticadorDeSenha(senha, senhaDasContas, indiceDaConta)
        saldoDaconta[indiceDaConta] -= valorFormatado
        saldoDaconta[indiceDaContaRecebedora] += valorFormatado
        print(f"Seu saldo bancário atual : {saldoDaconta[indiceDaConta]}")
        print(f"Saldo bancário da conta que recebeu a transferência : {saldoDaconta[indiceDaContaRecebedora]}")
        break
      else :
        print("Saldo insuficiente.")
        break
    elif (controleMenu == "4"):
      ativoBancario = sum(saldoDaconta)
      print(f"O ativo bancário é de : {ativoBancario}")
      break
    elif (controleMenu == "5"):
      funcaoAutenticacao.autenticador(contas, senhaDasContas, saldoDaconta)
    elif (controleMenu == "6"):
      print("Certo, tenha um bom dia !!")
      sys.exit()
    else:
      print("Número não registrado. Você deve inserir um número declarado na lista. ")
      print(f"\n================================================================================================================== \nConta logada : {conta} \n==================================================================================================================")
      controleMenu = (input("================================================================================================================== \n1. Realizar Depósito; \n2. Realizar Saque; \n3. Realizar Transferência; \n4. Consultar o ativo bancário, ou seja, o somatório dos saldos de todos os clientes; \n5. Mudar/sair da conta. \n6. Finalizar Programa \n================================================================================================================== \n"))
      continue
  print(f"\n================================================================================================================== \nConta logada : {conta} \n==================================================================================================================")
  controleMenu = (input("================================================================================================================== \n1. Realizar Depósito; \n2. Realizar Saque; \n3. Realizar Transferência; \n4. Consultar o ativo bancário, ou seja, o somatório dos saldos de todos os clientes; \n5. Mudar/sair da conta. \n6. Finalizar Programa \n================================================================================================================== \n"))
  menu(controleMenu, contas, senhaDasContas, saldoDaconta, codigoVerificado, senhaVerificada, indiceDaConta, conta)

