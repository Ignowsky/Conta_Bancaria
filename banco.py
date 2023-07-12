menu = """

[d] deposito
[s] saque
[e] extrato
[q] sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito realizado: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Digite o valor que deseja sacar: "))
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"Operação falhou! Você não possui saldo.")

        elif excedeu_limite:
            print(
                "Operação falhou! Você excedeu seu limite de saque, contate seu gerente para aumentar. ")

        elif excedeu_saques:
            print("Operação falhou! Você excedeu seu número de saques diarios.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque realizado: {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! valor informado inválido.")

    elif opcao == "e":
        print("=============== Extrato ===============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=======================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
