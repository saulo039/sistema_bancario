from abc import ABC, abstractmethod
from datetime import datetime

# ==================== CLASSES ====================

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.historico = Historico()

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido.")
            return False
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Número máximo de saques excedido.")
            return False
        if valor > self.limite:
            print("Valor excede o limite de saque.")
            return False
        if super().sacar(valor):
            self.numero_saques += 1
            return True
        return False


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


# ==================== FUNÇÕES AUXILIARES ====================

clientes = []
contas = []

def encontrar_cliente(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def cadastrar_cliente():
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")

    if encontrar_cliente(cpf):
        print("Cliente já cadastrado.")
        return

    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def cadastrar_conta():
    cpf = input("CPF do titular: ")
    cliente = encontrar_cliente(cpf)
    if not cliente:
        print("Cliente não encontrado.")
        return

    numero_conta = len(contas) + 1
    conta = ContaCorrente(numero_conta, cliente)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print(f"Conta {numero_conta} cadastrada com sucesso!")

def depositar():
    cpf = input("CPF do titular: ")
    cliente = encontrar_cliente(cpf)
    if not cliente:
        print("Cliente não encontrado.")
        return

    if not cliente.contas:
        print("Cliente não possui conta bancária. Cadastre uma conta primeiro.")
        return

    valor = float(input("Valor do depósito: "))
    cliente.realizar_transacao(cliente.contas[0], Deposito(valor))

def sacar():
    cpf = input("CPF do titular: ")
    cliente = encontrar_cliente(cpf)
    if not cliente:
        print("Cliente não encontrado.")
        return

    if not cliente.contas:
        print("Cliente não possui conta bancária. Cadastre uma conta primeiro.")
        return

    valor = float(input("Valor do saque: "))
    cliente.realizar_transacao(cliente.contas[0], Saque(valor))

def exibir_extrato():
    cpf = input("CPF do titular: ")
    cliente = encontrar_cliente(cpf)
    if not cliente:
        print("Cliente não encontrado.")
        return

    if not cliente.contas:
        print("Cliente não possui conta bancária. Cadastre uma conta primeiro.")
        return

    conta = cliente.contas[0]
    print("\n========= EXTRATO =========")
    if not conta.historico.transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in conta.historico.transacoes:
            tipo = transacao.__class__.__name__
            valor = transacao.valor
            print(f"{tipo}: R$ {valor:.2f}")
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("============================")

def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print(f"Conta {conta.numero} - Titular: {conta.cliente.nome} - Saldo: R$ {conta.saldo:.2f}")

# ==================== MENU ====================

def menu():
    opcoes = """
Escolha uma opção:
[1] Cadastrar cliente
[2] Cadastrar conta
[3] Listar contas
[4] Depositar
[5] Sacar
[6] Extrato
[0] Sair
=> """
    while True:
        opcao = input(opcoes)

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_conta()
        elif opcao == "3":
            listar_contas()
        elif opcao == "4":
            depositar()
        elif opcao == "5":
            sacar()
        elif opcao == "6":
            exibir_extrato()
        elif opcao == "0":
            print("Obrigado por usar nosso sistema bancário!")
            break
        else:
            print("Opção inválida, tente novamente.")

# ==================== EXECUÇÃO ====================
if __name__ == "__main__":
    menu()
