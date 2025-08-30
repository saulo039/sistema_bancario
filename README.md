# 💰 Sistema Bancário em Python

Este projeto foi desenvolvido como parte do **Bootcamp Santander 2025 - Backend com Python**, promovido pela [DIO (Digital Innovation One)](https://dio.me/).
O sistema simula um banco no terminal, permitindo ao usuário realizar **depósitos**, **saques** e **consultar extrato**, além de **cadastrar usuários e contas**.

---

## 🧠 Objetivo

Aplicar os fundamentos de programação em Python, incluindo entrada e saída de dados, estruturas de controle, laços de repetição, lógica de negócio e manipulação de strings, criando um projeto funcional com propósito real.

---

## 🚀 Funcionalidades

- [x]  Depositar valores com confirmação
- [x] Sacar valores com regras:
      - Limite de R$ 500 por saque
      - Máximo de 3 saques por sessão
      - Não pode exceder o saldo
- [x] Visualizar extrato com todas as movimentações, incluindo data e hora
- [x] Cadastro de usuário (com CPF único)
- [x] Cadastro de conta bancária vinculada a um usuário existente
- [x] Listagem de contas cadastradas com agência fixa 0001
- [x] Mensagens de sucesso ou falha claras para o usuário
- [x] Encerramento amigável do sistema

---

## 📋 Regras de negócio

- **Depósito**: deve ser maior que zero.  
- **Saque**:
  - Máximo de 3 saques por execução do programa
  - Valor máximo por saque: R$ 500
  - Valor não pode ser maior que o saldo disponível
- **Usuário**:
  - Identificado unicamente por CPF
  - Pode ter **uma ou mais contas** vinculada
- **Conta bancária**:
  - Deve estar vinculada a um usuário existente
  - Número da conta é gerado automaticamente
  - Agência fixa: 0001
- Todas as operações válidas são registradas no extrato

---

## 💻 Tecnologias utilizadas

- Python 3.x (puro, sem bibliotecas externas)

---

## 🏁 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/saulo039/sistema-bancario-python.git
   cd sistema-bancario-python
   ```

2. Execute o script com Python:
   ```bash
   python sistema_bancario.py
   ```

---

## 📝 Exemplo de Uso

```text
================ MENU ================
[1] Cadastrar cliente
[2] Cadastrar conta
[3] Listar contas
[4] Depositar
[5] Sacar
[6] Extrato
[0] Sair
======================================

=> 1
Nome: João Silva
Data de nascimento (dd/mm/aaaa): 01/01/1990
CPF: 12345678900
Endereço: Rua A, 123 - Centro - Belém/PA
Cliente cadastrado com sucesso!

=> 2
CPF do titular: 12345678900
Conta 1 cadastrada com sucesso!

=> 4
CPF do titular: 12345678900
Valor do depósito: 1000
Depósito de R$ 1000.00 realizado com sucesso!

=> 5
CPF do titular: 12345678900
Valor do saque: 300
Saque de R$ 300.00 realizado com sucesso!

=> 6
CPF do titular: 12345678900

========= EXTRATO =========
30/08/2025 13:00:00 - Deposito: R$ 1000.00
30/08/2025 13:02:15 - Saque: R$ 300.00

Saldo atual: R$ 700.00
============================

=> 3
Agência: 0001 - Conta 1 - Titular: João Silva - Saldo: R$ 700.00

=> 0
Obrigado por usar nosso sistema bancário!

```

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram colocados em prática:

- Lógica de programação aplicada a regras de negócio
- Uso de funções para organizar o código
- Estruturas de repetição (while) e condicionais (if, elif, else)
- Controle de estado com variáveis (saldo, historico, clientes, contas)
- Manipulação de strings para formatar extrato e mensagens
- Organização e boas práticas na escrita de código Python

---

## 👨‍💻 Autor

Desenvolvido por **Saulo Ribeiro Oliveira da Silva**

- 📧 [sauloribeiro039@gmail.com](mailto:sauloribeiro039@gmail.com)  
- 💼 [LinkedIn](https://www.linkedin.com/in/sauloribeiro039)  
- 🐙 [GitHub](https://github.com/saulo039)

---

🧠 Projeto criado para fins educacionais, como parte da jornada de aprendizado em backend com Python no bootcamp Santander DIO 2025.
