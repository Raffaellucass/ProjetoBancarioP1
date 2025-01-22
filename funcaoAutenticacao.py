
import sys, funcaoCriacaoEControleDeContas, funcoesDoMenu
def autenticador (contas, senhaDasContas, saldoDaConta):
    for tentativaDaConta in range(5, 0 , -1):
        codigo = input("Digite o código da conta : ")
        codigoVerificado = funcaoCriacaoEControleDeContas.controlarCodigo(codigo)
        if codigoVerificado in contas :
            indiceDaConta = contas.index(codigoVerificado)
            print("Conta encontrada.")
            for tentativaDeSenha in range(5, 0 , -1):
                senha = input("Digite a senha da conta : ")
                senhaVerificada = funcaoCriacaoEControleDeContas.controlarSenha(senha)
                if senhaVerificada == senhaDasContas[indiceDaConta] :
                    print("Acesso concedido.")
                    conta = contas[indiceDaConta]
                    print(f"\n================================================================================================================== \nConta logada : {conta} \n==================================================================================================================")
                    controleMenu = (input("================================================================================================================== \n1. Realizar Depósito; \n2. Realizar Saque; \n3. Realizar Transferência; \n4. Consultar o ativo bancário, ou seja, o somatório dos saldos de todos os clientes; \n5. Mudar/sair da conta. \n6. Finalizar Programa \n================================================================================================================== \n"))
                    funcoesDoMenu.menu(controleMenu, contas, senhaDasContas, saldoDaConta, codigoVerificado, senhaVerificada, indiceDaConta, conta)
                    return
                else:
                    print(f"Senha incorreta. \nVocê tem apenas {tentativaDeSenha-1} tentativas.")
                
        else : 
            print(f"Conta não encontrada. \nVocê tem apenas {tentativaDaConta-1} tentativas.")
        
    print("O programa será fechado por segurança.")
    sys.exit()

def autenticadorDeConta (codigo, contas):
    while True :
        codigoVerificado = funcaoCriacaoEControleDeContas.controlarCodigo(codigo)
        if codigoVerificado in contas :
            indiceDaConta = contas.index(codigoVerificado)
            print("Conta encontrada.")
            return indiceDaConta
        else :
            print(f"Conta não encontrada")
        codigo = input("Digite o código da conta : ")
 
def autenticadorDeSenha (senha, senhaDasContas, indiceDaConta):
    for tentativaDeSenha in range(5, 1 , -1):
        if senha.strip() == "":
            print("O campo não pode ficar vazio..")
        elif not senha.isdigit():
            print("A senha deve conter apenas números.")
        if senha == senhaDasContas[indiceDaConta] :
            print("Acesso concedido.")
            return (indiceDaConta)
        else:
            print(f"Senha incorreta. \nVocê tem apenas {tentativaDeSenha-1} tentativas.")
        senha = input("Digite a senha novamente : ")
    print("O programa será fechado por segurança.")
    sys.exit()

def autenticadorDeValor (valor):
    while True :
        if valor.strip() == "":
            print("O campo não pode ficar vazio.")
        elif not valor.isdigit():
            print("Apenas números, a formatação do valor será feita automáticamente. \n(Não coloque nenhuma pontuação.)")
        else : 
            valor = float(valor)
            valorFormatado = round(valor, 2)
            return valorFormatado
        valor = input("Digite o valor novamente : ")
    
    