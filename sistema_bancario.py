menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
comando = ''

log_depositos = []
log_saques = []

while True:
    opcao = input(menu)

    if opcao == '1':
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        while valor_deposito <= 0:
            valor_deposito = float(input("Valor para depósito inválido. Digite novamente: "))

        saldo += valor_deposito
        log_depositos.append(valor_deposito)

        print("Valor depositado com sucesso!\n"
        f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == '2':
        while comando != 'n':
            if numero_saques < LIMITE_SAQUES:
                valor_saque = float(input("Digite o valor a ser retirado: "))

                while valor_saque <= 0:
                    valor_saque = float(input("Valor para saque inválido. Digite novamente: "))
                while valor_saque > saldo:
                    valor_saque = float(input("Valor para saque inválido. Digite novamente: "))
                while valor_saque > limite:
                    valor_saque = float(input("Limite de 500 reais por saque. Tente novamente: "))
                
                saldo -= valor_saque
                log_saques.append(valor_saque)

                print("Valor retirado com sucesso!\n"
                f"Saldo atual: R$ {saldo:.2f}")

                numero_saques += 1

                comando = input("Realizar outro saque? [s/n] => ")
            else:
                print("Limite de saques diários atingido. Tente novamente amanhã!")
                comando = 'n'

    elif opcao == '3':
        print(" EXTRATO ".center(15, "="))
        for i in log_depositos:
            print(f"+ R$ {i:.2f}")
        for j in log_saques:
            print(f"- R$ {j:.2f}")

        print(f"=> SALDO ATUAL: R$ {saldo:.2f}")

    elif opcao == '4':
        print("Agradecemos por utilizar nosso serviço! Volte sempre ;)")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
