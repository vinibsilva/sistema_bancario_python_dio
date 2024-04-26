#Declaração de todas as variáveis a serem utilizadas
saldo = 0
LIMITE_SAQUE = 500
quantia_saque = 0
saques_feitos = 0

#Variável Menu para orientar o cliente
menu = """
Bem-vindo ao menu de nosso sistema bancário. Leia todas as funcionalidades abaixo:

(s) para realizar saques.
(d) para realizar depósitos.
(e) para conferir o extrato.
(s) para sair.

Insira sua opção: 
"""
opcao = input(menu)

while True:

    if opcao == 's':
        saque = float(input("Insira a quantidade que deseja sacar: "))
    #Fazendo as restrições do saque   
        if saque > 500  or quantia_saque == 500:
            print("O limite de saque é de 500 reais por dia...")
        elif saque > saldo:
            print("Você não possui saldo suficiente para realizar esse saque. Por favor, tente novamente...")
        elif saques_feitos == 3:
            print("Você ja realizou o máximo de saques no dia...")
        else:
            quantia_saque = quantia_saque + saque
            saques_feitos += 1
        continue 
    elif opcao == 'd':
        deposito = float(input("Informe a quantia que quer depositar: "))
        saldo = saldo + deposito

