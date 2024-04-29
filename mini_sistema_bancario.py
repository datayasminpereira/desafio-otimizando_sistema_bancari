menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
LIMITE_SAQUES = 3

saldo = 0
limite = 500
extrato = ""
numero_saques = 0

while True:

    opcao = input(menu)

    if opcao == "d":

        try:
            valor_deposito = float(input("Insira o valor que deseja depositar:"))
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            else:
                print("Depósito falhou! Não é possível depositar valor nulo ou negativo!")
        except ValueError:
            print("Erro! Por favor, insira um número!")
        

    elif opcao == "s":

        try:
            valor_saque = float(input("Insira o valor que deseja sacar:"))
            if valor_saque > 0:
                if valor_saque <= 500:
                    if valor_saque <= saldo:
                        if numero_saques < LIMITE_SAQUES:
                            saldo -= valor_saque
                            extrato += f"Saque: R$ {valor_saque:.2f}\n"
                            numero_saques += 1
                        else:
                            print("Saque falhou! Número máximo diario de saques foi atingido.")
                    else:
                        print("Saque falhou! Saldo insuficiente!") 
                else:
                    print("Saque falhou! Limite por saque é de R$500!")
            else:
                print("Saque falhou! Não é possível sacar valor nulo ou negativo!")

        except ValueError:
            print("Erro! Por favor, insira um número!")


    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")