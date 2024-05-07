class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.saques_realizados = 0
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor} realizado. Novo saldo: R$ {self.saldo}')
        else:
            print('Valor inválido para depósito.')
    
    def sacar(self, valor):
        if valor > 0:
            if self.saques_realizados < 3 and valor <= 500:
                if self.saldo >= valor:
                    self.saldo -= valor
                    self.saques_realizados += 1
                    print(f'Saque de R$ {valor} realizado. Novo saldo: R$ {self.saldo}')
                else:
                    print('Saldo insuficiente.')
            else:
                print('Limite diário de saques atingido ou valor excede R$ 500.')
        else:
            print('Valor inválido para saque.')
    
    def extrato(self):
        print(f'Saldo atual: R$ {self.saldo}')
        print(f'Saques realizados hoje: {self.saques_realizados}')

def menu():
    print("Bem-vindo ao sistema bancário!")
    print("Escolha uma opção:")
    print("1.Sacar")
    print("2.Depositar")
    print("3.Extrato")
    print("4.Sair")

conta = ContaBancaria()

while True:
    menu()
    opcao = input("Escolha uma opção:")

    if opcao == "1":
        valor = float(input("Digite o valor para sacar:"))
        conta.sacar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor para depositar:"))
        conta.depositar(valor)
    elif opcao == "3":
        conta.extrato()
    elif opcao == "4":
        print("Obrigado por utilizar o nosso sistema bancário. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
