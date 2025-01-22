def receberNumero(quantContasString):
    while True:
        try:
            numero = int(quantContasString)  
            return numero  
        except ValueError:
            print("Por favor, digite apenas números.")
        quantContasString = input("Informe quantas contas deseja criar : ")


import sys, funcaoCriacaoEControleDeContas
def escolherAtendente (controleAtendente, contas, senhaDasContas, saldoDaconta):
  while True :
    if (controleAtendente == "1" ):
      p1Etapa = input("Saudações! Agradecemos por escolher nossos serviços! \nAntes de prosseguirmos, você já possui uma conta em nosso banco ? ").upper()
      break
    elif (controleAtendente == "2"):
      p1Etapa = input("Olá! Agradecemos por confiar em nós! \nAntes de avançarmos, você já é cliente do nosso banco ? ").upper()
      break
    elif (controleAtendente == "3"):
      p1Etapa = input("Bem-vindo! Agradecemos por sua escolha! \nAntes de começarmos, você já tem uma conta conosco ? ").upper()
      break
    elif (controleAtendente == "4"):
      p1Etapa = input("Olá! Obrigado por optar por nossos serviços! \nAntes de continuarmos, você já possui uma conta bancária aqui ? ").upper()
      break
    elif (controleAtendente == "5"):
      p1Etapa = input("Saudações! Agradecemos sua preferência! \nAntes de seguirmos em frente, já está cadastrado como cliente do banco ? ").upper()
      break
    elif (controleAtendente == "6"):
      p1Etapa = input("Olá! Estamos felizes por você ter escolhido nossos serviços! \nAntes de procedermos, você já fez parte da nossa instituição bancária ? ").upper()
      break
    else:
      print("Digite apenas números declarados na lista.")
      controleAtendente = (input("\nDigite 1 para falar com Raffael; \nDigite 2 para falar com Jarlis; \nDigite 3 para falar com Jenny; \nDigite 4 para falar com Matheus; \nDigite 5 para falar com Athur; \nDigite 6 para falar com Felipe. \n"))
      continue
               
  if(p1Etapa == "SIM"):
      return
  elif (p1Etapa == "NÃO" or p1Etapa == "NAO"):
    while True :
      p1EtapaAcaso = input("Deseja criar uma conta ? ").upper()
      if(p1EtapaAcaso == "SIM"):
        quantContas = 1
        funcaoCriacaoEControleDeContas.criarContas(quantContas, contas, senhaDasContas, saldoDaconta)
        break
      elif(p1EtapaAcaso == "NÃO" or p1EtapaAcaso == "NAO"):
        print("Certo, tenha um bom dia !!")
        sys.exit()
      else :
        print("Responda com (sim) ou (não).")
      
  else :
    print("Responda com (sim) ou (não).")
  escolherAtendente(controleAtendente, [], [], [])
    
                            