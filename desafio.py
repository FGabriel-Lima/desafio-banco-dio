menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
depositos_feitos = []
saques_feitos = []

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0.0:
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f} \n"

    elif opcao == "s":
        print("Saque")
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        if valor_saque > 0.0 and valor_saque <= saldo:
            if valor_saque <= limite:
                if numero_saques < LIMITE_SAQUES:
                    numero_saques += 1
                    saldo -= valor_saque
                    extrato += f"Saque: R${valor_saque:.2f} \n"
        else:
            print("Não foi possível realizar o saque pois a quantia desejada não está disponível")

    elif opcao == "e":
        print("=====================Extrato=====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================================")

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")