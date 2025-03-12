import textwrap


class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = "".join(filter(str.isdigit, cpf))  # Armazena apenas números do CPF

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"


class ContaBancaria:
    AGENCIA = "0001"

    def __init__(self, usuario):
        self.usuario = usuario
        self.numero_conta = len(contas) + 1  # Número sequencial da conta
        self.saldo = 0.0
        self.extrato = []
        self.numero_saques = 0

    def depositar(self, valor):
        if valor <= 0:
            print("Erro: O valor do depósito deve ser positivo.")
            return False

        self.saldo += valor
        self.extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        return True

    def sacar(self, valor):
        limite = 500.0
        limite_saques = 3

        if self.numero_saques >= limite_saques:
            print("Erro: Limite de saques diários atingido.")
            return False

        if valor > limite:
            print("Erro: O valor do saque excede o limite permitido de R$ 500,00.")
            return False

        if valor > self.saldo:
            print("Erro: Saldo insuficiente.")
            return False

        self.saldo -= valor
        self.extrato.append(f"Saque: R$ {valor:.2f}")
        self.numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        return True

    def exibir_extrato(self):
        print("\nExtrato da Conta")
        print("-" * 40)
        
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        
        for transacao in self.extrato:
            print(transacao)
        
        print("-" * 40)
        print(f"Saldo Atual: R$ {self.saldo:.2f}")
        print("-" * 40)


# Lista global para armazenar contas
contas = []


def criar_usuario(nome, data_nascimento, cpf, endereco):
    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    if any(u.cpf == usuario.cpf for u in usuarios):
        print("Erro: Já existe um usuário cadastrado com esse CPF.")
    else:
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
    return usuario


def criar_conta(usuario):
    conta = ContaBancaria(usuario)
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {conta.AGENCIA}, Conta: {conta.numero_conta}")


def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        print("=" * 40)
        print(f"Agência: {conta.AGENCIA}")
        print(f"Número da Conta: {conta.numero_conta}")
        print(f"Titular: {conta.usuario.nome}")
    print("=" * 40)


def menu():
    while True:
        opcao = input(textwrap.dedent("""
            \n========== Sistema Bancário ==========
            [1] Cadastrar Usuário
            [2] Criar Conta Bancária
            [3] Listar Contas Bancárias
            [4] Depositar
            [5] Sacar
            [6] Exibir Extrato
            [7] Sair
            Escolha uma opção: """))

        if opcao == "1":
            nome = input("Nome completo: ")
            data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço (logradouro, número - bairro - cidade/UF): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "2":
            cpf = input("Informe o CPF do usuário: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if not usuario:
                print("Erro: Usuário não encontrado.")
                continue
            
            criar_conta(usuario)

        elif opcao == "3":
            listar_contas()

        elif opcao == "4":
            cpf = input("Informe o CPF do titular da conta: ")
            conta = next((c for c in contas if c.usuario.cpf == cpf), None)
            if not conta:
                print("Erro: Conta não encontrada.")
                continue

            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)

        elif opcao == "5":
            cpf = input("Informe o CPF do titular da conta: ")
            conta = next((c for c in contas if c.usuario.cpf == cpf), None)
            if not conta:
                print("Erro: Conta não encontrada.")
                continue

            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor)

        elif opcao == "6":
            cpf = input("Informe o CPF do titular da conta: ")
            conta = next((c for c in contas if c.usuario.cpf == cpf), None)
            if not conta:
                print("Erro: Conta não encontrada.")
                continue

            conta.exibir_extrato()

        elif opcao == "7":
            print("Saindo do sistema... Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Lista global para armazenar usuários
usuarios = []

if __name__ == "__main__":
    menu()
