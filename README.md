
# Sistema Bancário em Python

Repositório para armazenar os sistemas desenvolvidos baseados no que foi orientado no Bootcamp "Python Backend" da DIO.  [Página da DIO ](www.dio.me)

## 📒Requisitos da versão 1



O sistema deve ter operações de depósito, saque e extrato.

O usuário deve fazer depósitos e esses depósitos devem ser armazenados em uma variável estar presentes no extrato.

O usuário só pode realizar 3 saques no dia e com um limite de R$500. 

Se o usuário não tiver saldo, cabe ao sistema avisá-lo. Os saques devem ser armazenados em uma variável.                       

No extrato devem estar listados todos os saques e depósitos. No final, deve conter o saldo atual.                                                             

## 📒Requisitos da versão 2

1. As operações de depósito, saque e extrato devem ser feitas através de funções;

2. Devem ser feitas duas funções para criar usuário e criar conta corrente;

3. Usar argumentos por posições e nomes;

3.1. Função Saque(keyword only).

3.2. Função Depósito(positional only).

3.3. Função Extrato(positional only e keyword only).

4. O programa deve armazenar os usuários em uma lista

4.1. Cada usuário tem nome, data de nascimento, cpf e endereço.

4.2. O endereço é uma string com o formato: logradouro, número - bairro - cidade/sigla estado.

4.3. Não pode ser permitido o cadastro de mais de um usuário com CPF iguais.

5. O programa deve armazenar a conta corrente em uma lista.

5.1. A conta é composta por agência, número da conta e usuário.

5.2. O número da conta é sequencial e se inicia em 1. Ja o número da agência é fixo: 0001.

5.3. O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário e pra existir precisa de um usuário.
 

