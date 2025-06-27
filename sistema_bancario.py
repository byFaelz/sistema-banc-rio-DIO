saldo = 0
extrato = ""

while True:
    entrada_de_dados = input("""
    -------------------
    Escolha a sua opção:
       [1] Depósito
       [2] Saque   
       [3] Extrato
       [4] Sair
    -------------------
        """)
    
    if entrada_de_dados == "1":
        valor_do_deposito = float(input("Digite o valor do depósito: "))

        if valor_do_deposito <= 0:
            print("Digite um valor válido para o depósito.")
        else:
            saldo += valor_do_deposito
            extrato += f"Depósito: R${valor_do_deposito:.2f}\n"
            print(f"Depósito de R${valor_do_deposito:.2f} realizado com sucesso.")

    elif entrada_de_dados == "2":
        valor_do_saque = float(input("Digite o valor do saque: "))

        if valor_do_saque <= 0:
            print("Digite um valor válido para o saque.")
        elif valor_do_saque > saldo:
            print("Saque indisponível. Saldo insuficiente.")
        else:
            saldo -= valor_do_saque
            extrato += f"Saque: R${valor_do_saque:.2f}\n"
            print(f"Saque de R${valor_do_saque:.2f} realizado com sucesso.")

    elif entrada_de_dados == "3":
        print("\n========== EXTRATO ==========")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"Saldo atual: R${saldo:.2f}")
        print("=============================\n")

    elif entrada_de_dados == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
