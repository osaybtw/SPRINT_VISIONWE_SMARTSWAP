baterias_disponiveis = 5
baterias_carregando = []

TARIFA = 0.80

def mostrar_status():
    print("===== STATUS =====\n")
    print(f"Baterias disponíveis: {baterias_disponiveis}")
    print(f"Baterias carregando: {len(baterias_carregando)}")

    if len(baterias_carregando) > 0:
        print("Baterias em recarga:\n")
        for i, carga in enumerate(baterias_carregando, start=1):
            print(f"Bateria {i}: {carga}% de carga")

while True:

    print("===== CHARGEGRID =====\n")
    print("1 - Registrar troca de bateria")
    print("2 - Finalizar recarga de uma bateria")
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

        energia_utilizada = 100 - energia_restante
        valor = energia_utilizada * TARIFA

        print("\n===== COBRANÇA =====\n")
        print(f"Energia utilizada: {energia_utilizada:.1f}%")
        print(f"Valor a pagar: R$ {valor:.2f}")

        pagamento = input(
            "\nPagamento realizado?\n1 - Sim\n2 - Não\nEscolha: "
        )

        if pagamento == "1":
            baterias_disponiveis -= 1
            baterias_carregando.append(energia_restante)

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
            print("Adicionada ao estoque de baterias disponíveis.")

            mostrar_status()

        except ValueError:
            print("Digite um número válido.\n")

    else:
        print("Opção inválida.\n")