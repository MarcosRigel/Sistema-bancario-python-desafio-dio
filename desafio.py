menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
contador_saques = 0
primeiro_saque_diario = 0
segundo_saque_diario = 0
terceiro_saque_diario = 0
primeiro_deposito = 0
segundo_deposito = 0
terceiro_deposito = 0
quarto_deposito = 0
quinto_deposito = 0
contador_depositos = 1


while True:
    
    opcao = input(menu)

    if opcao == "d":

        if contador_depositos > 5:
            print("Período de depositos diarios excedidos")
        else:
            valor_deposito = float(input("Digite um valor para depósito: R$"))

            if valor_deposito > 0:

                saldo += valor_deposito
                
                if contador_depositos == 1:

                    primeiro_deposito += saldo
                    contador_depositos += 1

                elif contador_depositos == 2:

                    segundo_deposito += saldo
                    contador_depositos += 1

                elif contador_depositos == 3:

                    terceiro_deposito += saldo
                    contador_depositos += 1

                elif contador_depositos == 4:

                    quarto_deposito += saldo
                    contador_depositos += 1

                elif contador_depositos == 5:
                    
                    quinto_deposito += saldo
                    contador_depositos += 1
            else:
                print("Valor inválido")

    elif opcao == "s":

        if (contador_saques > LIMITE_SAQUES):
            print("Período de saques diarios excedidos")
        
        elif(saldo == 0):
            print("Saldo vazio :( ")
        
        else:
            while(LIMITE_SAQUES > contador_saques):

                valor_saque = float(input("Digite um valor para saque: R$"))
                
                if contador_saques == 0:

                    if valor_saque > 500.00:
                        print("Valor acima do limite")
                    
                    elif valor_saque > valor_deposito:
                        print("valor de saque maior que o valor depositado")
                    
                    elif valor_saque <= 500.00 and valor_saque <= saldo:
                        primeiro_saque_diario = valor_saque
                        saldo -= valor_saque
                        contador_saques += 1
                    break
                
                if contador_saques == 1:
                    
                    if valor_saque > 500.00:
                        print("Valor acima do limite")
                    
                    elif valor_saque > valor_deposito:
                        print("valor de saque maior que o valor depositado")
                    
                    elif valor_saque <= 500.00 and valor_saque <= saldo:
                        segundo_saque_diario = valor_saque
                        saldo -= valor_saque
                        contador_saques += 1
                    break
                
                if contador_saques == 2:
                    
                    if valor_saque > 500.00:
                        print("Valor acima do limite")
                    
                    elif valor_saque > valor_deposito:
                        print("valor de saque maior que o valor depositado")
                    
                    elif valor_saque <= 500.00 and valor_saque <= saldo:
                        terceiro_saque_diario = valor_saque
                        saldo -= valor_saque
                        contador_saques += 1
                    break
    
    elif opcao == "e":

        print("Históricos")
        print(f"valor deposito atual: {saldo}")
        print("===== DEPOSITOS: =======")
        
        if primeiro_deposito != 0:
            print(f"primeiro deposito: {primeiro_deposito}")
        
        if segundo_deposito != 0:
            print(f"segundo deposito: {segundo_deposito}")
        
        if terceiro_deposito != 0:
            print(f"terceiro deposito: {terceiro_deposito}")
        
        if quarto_deposito != 0:
            print(f"quarto deposito: {quarto_deposito}")
        
        if quinto_deposito != 0:
            print(f"quinto deposito: {quinto_deposito}")
        
        print("===== SAQUES: =======")
       
        if primeiro_saque_diario != 0:
            print(f"primeiro saque: {primeiro_saque_diario}")
        
        if segundo_saque_diario != 0:
            print(f"segundo saque: {segundo_saque_diario}")
        
        if terceiro_saque_diario != 0:
            print(f"terceiro saque: {terceiro_saque_diario}")
    
    elif opcao == "q":
        print("Obrigado por ser nosso cliente!")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")