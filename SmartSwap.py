baterias_disponiveis = 5
baterias_carregando = []
historico_valor = []

capacidade_bateria = 60
preco_kwh = 2.00
taxa_servico = 10.00

def mostrar_status():
    print("===== STATUS =====\n")
    print(f"Baterias disponíveis: {baterias_disponiveis}")
    print(f"Baterias carregando: {len(baterias_carregando)}")

    if baterias_disponiveis <= 1:
        print("ALERTA: ESTOQUE CRÍTICO")

    if len(baterias_carregando) > 0:
        print("Baterias em recarga:\n")
        for i, carga in enumerate(baterias_carregando, start=1):
            print(f"Bateria {i}: {carga}% de carga")

while True:

    print("===== CHARGEGRID =====\n")
    print("1 - Registrar troca de bateria")
    print("2 - Finalizar recarga de uma bateria")
    print("3 - Mostrar status")
    print("4 - Relatório financeiro")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "0":
        print("Sistema encerrado.")
        break

    elif opcao == "1":

        if baterias_disponiveis <= 0:
            print("Não há baterias disponíveis.\n")
            continue

        energia_restante = float(
            input(
                "Informe a porcentagem restante da bateria devolvida (0-100): "
            )
        )

        if energia_restante < 0 or energia_restante > 100:
            print("Valor inválido.\n")
            continue

        percentual_utilizado = 100 - energia_restante
        energia_utilizada_kwh = (
            percentual_utilizado / 100
        ) * capacidade_bateria

        valor_energia = energia_utilizada_kwh * preco_kwh
        valor_total = valor_energia + taxa_servico

        print("\n===== COBRANÇA =====\n")
        print(f"Carga restante da bateria: {energia_restante:.1f}%")
        print(f"Energia utilizada: {energia_utilizada_kwh:.2f} kWh")
        print(f"Valor da energia: R$ {valor_energia:.2f}")
        print(f"Taxa de serviço: R$ {taxa_servico:.2f}")
        print(f"Total a pagar: R$ {valor_total:.2f}")

        pagamento = input(
            "\nPagamento realizado?\n1 - Sim\n2 - Não\nEscolha: "
        )

        if pagamento == "1":
            baterias_disponiveis -= 1
            baterias_carregando.append(energia_restante)
            historico_valor.append(valor_total)

            print("Troca realizada com sucesso!\n")
            mostrar_status()

        else:
            print("Operação cancelada.\n")

    elif opcao == "2":

        if len(baterias_carregando) == 0:
            print("Não há baterias em carregamento.\n")
            continue

        print("===== BATERIAS EM CARREGAMENTO =====\n")

        for i, carga in enumerate(baterias_carregando, start=1):
            print(f"{i} - Bateria com {carga}% de carga")

        try:
            escolha = int(
                input(
                    "Digite o número da bateria que terminou de carregar: \n"
                )
            )

            if escolha < 1 or escolha > len(baterias_carregando):
                print("Número inválido.\n")
                continue

            baterias_carregando.pop(escolha - 1)
            baterias_disponiveis += 1

            print("Bateria recarregada com sucesso!\n")

            mostrar_status()

        except ValueError:
            print("Digite um número válido.\n")

    elif opcao == "3":
        mostrar_status()

    elif opcao == "4":

        print("===== RELATÓRIO FINANCEIRO =====\n")
        if len(historico_valor) == 0:
            print("Nenhuma troca registrada ainda.")

        else:
            total = sum(historico_valor)
            quantidade = len(historico_valor)
            media = total / quantidade

            print(f"Trocas realizadas: {quantidade}")
            print(f"Receita total: R$ {total:.2f}")
            print(f"Média por troca: R$ {media:.2f}")

    else:
        print("Opção inválida.\n")