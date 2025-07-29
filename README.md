# 💰 Sistema Bancário em Python

Este projeto foi desenvolvido como parte do **Bootcamp Santander 2025 - Backend com Python**, promovido pela [DIO (Digital Innovation One)](https://dio.me/). O sistema simula um banco no terminal, permitindo ao usuário realizar **depósitos**, **saques** e **consultar o extrato bancário**, com regras simples de negócio.

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
- [x] Saldo atualizado após cada transação
- [x] Validação de entradas (sem valores negativos ou zerados)
- [x] Mensagens de sucesso ou falha claras para o usuário
- [x] Encerramento amigável do sistema

---

## 📋 Regras de negócio

- **Depósito**: deve ser maior que zero.
- **Saque**:
  - Máximo de 3 saques por execução do programa
  - Valor máximo por saque: R$ 500
  - Valor não pode ser maior que o saldo disponível
- Todas as operações válidas são registradas no extrato
- O extrato só é exibido se houver movimentações

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
Escolha uma Opção:
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [0] Sair

=> 1
Informe o valor do depósito: 1000
Depósito realizado com sucesso!

Escolha uma Opção:
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [0] Sair

=> 2
Informe o valor do saque: 300
Saque realizado com sucesso!

Escolha uma Opção:
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [0] Sair

=> 3

================ EXTRATO ================
Depósito: R$ 1000.00
Saque: R$ 300.00

Saldo: R$ 700.00
==========================================

Escolha uma Opção:
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [0] Sair

=> 0
Obrigado por usar nosso Sistema Bancário!
```

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram colocados em prática:

- Lógica de programação aplicada a regras de negócio  
- Uso de variáveis para controle de estado (saldo, saques)  
- Condicionais (`if`, `elif`, `else`)  
- Estruturas de repetição (`while`)  
- Interação com o usuário via `input()` e `print()`  
- Manipulação de strings para criar um extrato detalhado  

---

## 👨‍💻 Autor

Desenvolvido por **Saulo Ribeiro Oliveira da Silva**

- 📧 [sauloribeiro039@gmail.com](mailto:sauloribeiro039@gmail.com)  
- 💼 [LinkedIn](https://www.linkedin.com/in/sauloribeiro039)  
- 🐙 [GitHub](https://github.com/saulo039)

---

🧠 Projeto criado para fins educacionais, como parte da jornada de aprendizado em backend com Python no bootcamp Santander DIO 2025.
