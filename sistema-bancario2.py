
#Declaração de todas as variáveis a serem utilizadas
LIMITE_SAQUE = 500

verificacao_login = False
verificacao_cadastro = False
verificacao_ContaCorrente = False
num_conta = 1

#Declaração de dicionário para armazenar os usuários e seus dados
usuarios = {
    "01928374852" : {"nomeCompleto": "Testudo da Silva", 
                    "dataNascimento" : "21/06/1999",  
                    "endereço" : "Rua das Flores, 123 - Jardim Primavera - São Paulo/SP"}
}
#Declaração de dicionário para armazenar as contas corrente e seus dados
contas_corrente = {
    1 : {"numeroAgencia" : "0001", 
         "titular" : "01928374852",
         "saldo" : 0,
         "quantia_saque" : 0,
         "saques_feitos" : 0,
         "quantia_deposito" : 0,
         "depositos_feitos" : 0}
}

#Funções do programa

def imprimir_extrato(saldo, saques_feitos, quantia_saque, depositos_feitos, quantia_deposito):
    return f"""----------EXTRATO BANCÁRIO----------\n 
Saldo Atual da conta: {saldo}
Total de Saques efetuados: {saques_feitos}
Valor total sacado: {quantia_saque}
Total de depositos efetuados: {depositos_feitos}
Valor total depositado: {quantia_deposito}\n 
            """

def sacar(*, saldof, valor_saquef):
    saldof = saldof - valor_saquef
    return saldof

def depositar(saldo, valor_deposito, /):
    saldo = saldo + valor_deposito
    return saldo

def criarUsuario(nomeCompleto, data_nascimentoNovo, cpfNovo, enderecoNovo):
       return  {cpfNovo : {"nomeCompleto" : nomeCompleto ,"dataNascimento" : data_nascimentoNovo, "endereço" : enderecoNovo}}   

def criarContaCorrente(add_conta, add_agencia, add_titular):
    return {add_conta : {"numeroAgencia" : add_agencia, "titular" : add_titular, "saldo" : 0, "quantia_saque" : 0, "saques_feitos" : 0, "quantia_deposito" : 0, "depositos_feitos" : 0 }}

#Variáveis Menu para orientar o cliente
menu1 = """
Bem-vindo ao nosso sitemas bancário.

Para ter acesso as nossas funcionalidades por favor escolha uma opção:

(1) Para entrar.
(2) Para criar um usuário.
(3) Para criar uma conta corrente.
(0) Para sair 

Insira sua opção: 
"""

menu2 = """
Bem-vindo ao menu de nosso sistema bancário. Leia todas as funcionalidades abaixo:

(1) para realizar saques.
(2) para realizar depósitos.
(3) para conferir o extrato.
(0) para sair.

Insira sua opção: 
"""

#Parte executável

while True:
    opcao1 = int(input(menu1))

    if opcao1 == 1:
        login_usuario = input("Informe o CPF de usuário: ")
        login_conta = int(input("Informe o número da conta: "))
        
        #Checagem se o usuario existe no sistema.
        for usuarios_cpf in usuarios:
            if login_usuario == usuarios_cpf:
                verificacao_login = True
                break
            else:
                verificacao_login = False
    
        for contas in contas_corrente:
            if login_conta == contas:
                verificacao_login = True
                break
            else:
                verificacao_login = False
        #conferir se o cpf e a conta informados estão de fato associados
        if not contas_corrente[login_conta]["titular"] == login_usuario:
            verificacao_login = False
        
        
        if verificacao_login == True: 
            while True:
                opcao2 = int(input(menu2))
                #Variaveis relacionadas com a conta 
                
                if opcao2 == 1:
                    valor_saque = float(input("Insira a quantidade que deseja sacar: "))
                    #Fazendo as restrições do saque   
                    if valor_saque > LIMITE_SAQUE or contas_corrente[login_conta]["quantia_saque"] == 500:
                        print("\nO limite de saque é de 500 reais por dia...", end = "\n")
                        continue
                    elif valor_saque > contas_corrente[login_conta]["saldo"]:
                        print("\nVocê não possui saldo suficiente na conta para realizar esse saque. Por favor, tente novamente...", end = "\n")
                        continue
                    elif contas_corrente[login_conta]["saques_feitos"] == 3:
                        print("\nVocê ja realizou o máximo de saques no dia para essa conta, que são 3...", end = "\n")
                        continue
                    else:
                        contas_corrente[login_conta]["saldo"] = sacar(saldof = contas_corrente[login_conta]["saldo"], valor_saquef = valor_saque)
                        contas_corrente[login_conta]["quantia_saque"] = contas_corrente[login_conta]["quantia_saque"] + valor_saque
                        contas_corrente[login_conta]["saques_feitos"] = contas_corrente[login_conta]["saques_feitos"] + 1
            
                elif opcao2 == 2:
                    valor_deposito = float(input("Informe a quantia que quer depositar: "))
                    contas_corrente[login_conta]["quantia_deposito"] = contas_corrente[login_conta]["quantia_deposito"] + valor_deposito
                    contas_corrente[login_conta]["depositos_feitos"] += 1
                    contas_corrente[login_conta]["saldo"] = depositar(contas_corrente[login_conta]["saldo"], valor_deposito)
        
                elif opcao2 == 3:
                    extrato = imprimir_extrato(contas_corrente[login_conta]["saldo"], contas_corrente[login_conta]["saques_feitos"], contas_corrente[login_conta]["quantia_saque"], contas_corrente[login_conta]["depositos_feitos"], contas_corrente[login_conta]["quantia_deposito"] )
                    print(extrato)
                elif opcao2 == 0:
                    break
                    
        elif verificacao_login == False:
            print("\n-----Usuário ou Conta não identificados(ou Nenhuma relação entre eles)-----")
            continue
    elif opcao1 == 2:
        nome_completo_cadastro = input("Informe o nome completo: ")
        data_nascimento_cadastro = input("Informe a data de nascimento: ")
        cpf_cadastro = input("Insira seu CPF: ")
        endereco_cadastro = input("Insira seu endereço: ")
        
        #Checagem se o CPF informado ja está cadastrado
        for atributos in usuarios:
            if cpf_cadastro == atributos:
                verificacao_cadastro = False          
                break
            else:
                verificacao_cadastro = True
                continue
        
        if verificacao_cadastro == False:
            print("\n\n-----O CPF informado já foi cadastrado...-----")
            continue
        else:
            usuarios.update(criarUsuario(nome_completo_cadastro, data_nascimento_cadastro, cpf_cadastro, endereco_cadastro))
            print("\n\n\n----Parabéns, sua conta de usuário foi criada!----")

    elif opcao1 == 3:
        cadastro_numero_conta = num_conta+1
        cadastro_numero_agencia = "0001"
        cadastro_titular = input("Informe o CPF do titular: ")
        
        #Confere se o CPF ja está cadastrado
        for  usuarios_cpf in usuarios:
            if cadastro_titular == usuarios_cpf:
                verificacao_ContaCorrente = True
                break
            else:
                verificacao_ContaCorrente = False

        if verificacao_ContaCorrente == False:
            print("\n\n\n----CPF não cadastrado no sistema. Cadastre esse CPF----")
            continue
        else:
            num_conta += 1
            contas_corrente.update(criarContaCorrente(num_conta, cadastro_numero_agencia, cadastro_titular))
            print(f"\n\n\n----Parabéns, sua conta foi criada com sucesso. O número dela é {num_conta}----")

    elif opcao1 == 0:
        break
