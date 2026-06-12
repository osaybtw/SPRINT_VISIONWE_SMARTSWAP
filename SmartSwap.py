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
                "Informe a porcentagem restante da bateria devolvida (0-100): \n"
            )
        )

        energia_utilizada = 100 - energia_restante
        valor = energia_utilizada * TARIFA

        print("===== COBRANÇA =====\n")
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
    else:
        print("Opção inválida.\n")