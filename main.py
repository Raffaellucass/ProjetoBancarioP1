contas = []
senhaDasContas = []
saldoDaconta = []

import funcoesDeEntrada, funcaoCriacaoEControleDeContas, funcaoAutenticacao 

print("\n========================================================================================================================================== Antes de começar, aqui estão os nomes dos participantes do grupo : Raffael Lucas Pereira Andrade, Jennifer Caroline Maurino da Silva, Felipe Cunha de Lima, Jarlis de Souza Cunha, Matheus Henrique Mendonça do Nascimento, Arthur Vinícius Silva Câmara. \n========================================================================================================================================== ")

quantContasString = (input("O input foi modificado para permitir um quantitativo de testes menor que o pedido no documento principal, pois realizar o teste de 10 contas seria massante a longo prazo, então foi estabelecido que o programa iria perguntar a quantidade de contas a serem feitas antes de rodar. \nInforme quantas contas deseja criar : "))
quantContas = funcoesDeEntrada.receberNumero(quantContasString)
funcaoCriacaoEControleDeContas.criarContas(quantContas, contas, senhaDasContas, saldoDaconta)
print(f"{contas, senhaDasContas}")

controleAtendente = (input("================================================================================================================== \nOlá, Bom dia !!! Bem vindo ao Banco Bom Todo. \nVocê sera redirecionado a um dos nossos atendentes, se houver preferência, digite o número referente ao atendente. \nDigite 1 para falar com Raffael; \nDigite 2 para falar com Jarlis; \nDigite 3 para falar com Jenny; \nDigite 4 para falar com Matheus; \nDigite 5 para falar com Athur; \nDigite 6 para falar com Felipe. \n================================================================================================================== \n"))
funcoesDeEntrada.escolherAtendente(controleAtendente, contas, senhaDasContas, saldoDaconta)
funcaoAutenticacao.autenticador(contas, senhaDasContas, saldoDaconta)