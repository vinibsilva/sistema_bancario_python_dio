#Declaração de todas as variáveis a serem utilizadas
saldo = 0
LIMITE_SAQUE = 500
quantia_saque = 0
saques_feitos = 0

quantia_deposito = 0
depositos_feitos = 0



#Variável Menu para orientar o cliente
menu = """
Bem-vindo ao menu de nosso sistema bancário. Leia todas as funcionalidades abaixo:

(s) para realizar saques.
(d) para realizar depósitos.
(e) para conferir o extrato.
(q) para sair.

Insira sua opção: 
"""

op = "l"

while True:
    opcao = input(menu)
    
    if opcao == 's':
        saque = float(input("Insira a quantidade que deseja sacar: "))
    #Fazendo as restrições do saque   
        if saque > 500  or quantia_saque == 500:
            print("O limite de saque é de 500 reais por dia...", end = "\n")
            continue
        elif saque > saldo:
            print("Você não possui saldo suficiente para realizar esse saque. Por favor, tente novamente...", end = "\n")
            continue
        elif saques_feitos == 3:
            print("Você ja realizou o máximo de saques no dia que são 3...", end = "\n")
            continue
        else:
            quantia_saque = quantia_saque + saque
            saques_feitos += 1
            saldo = saldo - saque
        
    elif opcao == 'd':
        deposito = float(input("Informe a quantia que quer depositar: "))
        saldo = saldo + deposito

        quantia_deposito = quantia_deposito + deposito
        depositos_feitos += 1
    
    elif opcao == "e":
        extrato = f"""----------EXTRATO BANCÁRIO----------\n 
Saldo Atual da conta: {saldo}
Total de Saques efetuados: {saques_feitos}
Valor total sacado: {quantia_saque}
Total de depositos efetuados: {depositos_feitos}
Valor total depositado: {quantia_deposito}\n 
            """
        print(extrato)
    elif opcao == "q":
        break

print(saldo)