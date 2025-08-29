# 💰 Sistema Bancário em Python

Este projeto foi desenvolvido como parte do **Bootcamp Santander 2025 - Backend com Python**, promovido pela [DIO (Digital Innovation One)](https://dio.me/).
O sistema simula um banco no terminal, permitindo ao usuário realizar **depósitos**, **saques** e **consultar extrato**, além de **cadastrar usuários e contas**.

---

## 🧠 Objetivo

Aplicar os fundamentos de programação em Python, incluindo entrada e saída de dados, estruturas de controle, laços de repetição, lógica de negócio e manipulação de strings, criando um projeto funcional com propósito real.

---

## 🚀 Funcionalidades

- [x] Depositar valores com confirmação
- [x] Sacar valores com regras:
  - Limite de R$ 500 por saque
  - Máximo de 3 saques por sessão
  - Não pode exceder o saldo
- [x] Visualizar extrato com todas as movimentações
- [x] Cadastro de usuário (com CPF único)
- [x] Cadastro de conta bancária vinculada a um usuário existente
- [x] Listagem de contas cadastradas
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
[1] Depositar
[2] Sacar
[3] Extrato
[4] Listar Contas
[5] Novo Usuário
[6] Nova Conta
[0] Sair
======================================

=> 5
Informe o CPF (somente números): 12345678900
Informe o nome completo: João Silva
Informe a data de nascimento (dd-mm-aaaa): 01-01-1990
Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): Rua A, 123 - Centro - Belém/PA
Usuário cadastrado com sucesso!

=> 6
Informe o CPF do usuário: 12345678900
Conta criada com sucesso!

=> 1
Informe o valor do depósito: 1000
Depósito realizado com sucesso!

=> 2
Informe o valor do saque: 300
Saque realizado com sucesso!

=> 3
================ EXTRATO ================
Depósito: R$ 1000.00
Saque: R$ 300.00

Saldo: R$ 700.00
==========================================

=> 4
==========================================
        Agência:        0001
        C/C:            1
        Titular:        João Silva

=> 0
Obrigado por usar nosso Sistema Bancário!

```

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram colocados em prática:

- Lógica de programação aplicada a regras de negócio
- Uso de funções para organizar o código
- Estruturas de repetição (while) e condicionais (if, elif, else)
- Controle de estado com variáveis (saldo, extrato, usuarios, contas)
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
