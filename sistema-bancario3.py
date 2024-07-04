from datetime import date
from abc import ABC, abstractmethod
from typing import Type

#CRIANDO A CLASSE CONTAS
class Conta:
    def __init__(self, saldo : float, agencia : str , numero : int, historico : 'Historico'):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._historico = historico
   
    @property
    def saldo(self):
        return self._saldo
    
    #Criar nova conta
    @classmethod
    def nova_conta(self,cls, saldon, agencian, numeron, clienten):
        return cls(saldo = saldon, agencia = agencian, numero = numeron, cliente = clienten)
    
    #Confere se houve saque
    def sacar(self, saque : 'Saque'):
        saque.Registrar(self)
        self._historico.adicionar_transacao(saque)
        return True

    #Confere se houve depósito
    def depositar(self, deposito : 'Deposito'):
        deposito.Registrar(self)
        self._historico.adicionar_transacao(deposito)
        return True
    
class ContaCorrente(Conta):
    def __init__(self, limite: int, limite_saque : float, saldo, numero, cliente ):
        super().__init__(saldo, numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

#CRIANDO A CLASSE CLIENTE e sua filha PESSOAFISICA
class Cliente:
    def __init__(self,endereco : str):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta: 'Conta'):
        self.contas.append(conta)

    def realizar_transacao(self, conta: 'Conta', transacao : 'Transacao'):
        pass

class PessoaFisica(Cliente):
    def __init__(self, cpf : str, nome: str, data_nascimento: date, endereco):
        super().__init__(self, endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

#CRIANDO A CLASSE TRANSAÇÃO
class Transacao(ABC):
    @abstractmethod
    def Registrar(self, ):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def Registrar(self, conta: 'Conta'):
        conta._saldo += self._valor

    @property
    def valor(self):
        return self._valor

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def Registrar(self, conta: 'Conta'):
        conta._saldo -= self._valor

    @property
    def valor(self):
        return self._valor
    
#CRIANDO CLASSE HISTÓRICO
class Historico:
    def __init__(self):
        self.historico_saques = []
        self.historico_depositos = []

    def adicionar_transacao(self, transacao : 'Transacao'):
        if isinstance(transacao, Saque): 
            self.historico_saques.append(transacao.valor)
        elif isinstance(transacao, Deposito):
            self.historico_depositos.append(transacao.valor)
    
    @property
    def saques(self):
        return self.historico_saques

    @property
    def depositos(self):
        return self.historico_depositos
