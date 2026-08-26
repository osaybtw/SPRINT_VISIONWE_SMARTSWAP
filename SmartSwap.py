import tkinter as tk

janela = tk.Tk()

janela.title("ChargeGrid")
janela.geometry("800x600")

titulo = tk.Label(
    janela,
    text="CHARGEGRID",
    font=("Arial", 24)
)

titulo.pack(pady=30)

janela.mainloop()

baterias_disponiveis = 20
baterias_carregando = []
historico_valor = []

capacidade_bateria = 60
preco_kwh = 2.00
taxa_servico = 10.00

baterias = []

for i in range(1, baterias_disponiveis + 1):
    baterias.append([i, 100])


def mostrar_status():
    print("===== STATUS =====\n")
    print(f"Baterias disponíveis: {baterias_disponiveis}")
    print(f"Baterias carregando: {len(baterias_carregando)}")

    if baterias_disponiveis <= 1:
        print("ALERTA: ESTOQUE CRÍTICO")


def consultar_bateria():

    print("\n===== CONSULTAR BATERIA =====")

    if len(baterias_carregando) > 0:
        print("\nBaterias em recarga:\n")

        for bateria in baterias_carregando:
            print(f"Bateria {bateria[0]}: {bateria[1]}% de carga")

    try:
        escolha = int(input("\nDigite o número da bateria: "))

        if escolha < 1 or escolha > len(baterias):
            print("Bateria não encontrada.")
            return

        for bateria in baterias:

            if bateria[0] == escolha:
                print(f"\nBateria {bateria[0]}")
                print(f"Carga: {bateria[1]}%")
                return

    except ValueError:
        print("Digite um número válido.")


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

            for bateria in baterias:

                if bateria not in baterias_carregando:

                    bateria[1] = energia_restante
                    baterias_carregando.append(bateria)

                    break

            baterias_disponiveis -= 1
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

        for bateria in baterias_carregando:
            print(f"{bateria[0]} - Bateria com {bateria[1]}% de carga")

        try:

            escolha = int(
                input(
                    "Digite o número da bateria que terminou de carregar: \n"
                )
            )

            bateria_encontrada = None

            for bateria in baterias_carregando:

                if bateria[0] == escolha:
                    bateria_encontrada = bateria
                    break

            if bateria_encontrada is None:
                print("Número inválido.\n")
                continue

            bateria_encontrada[1] = 100
            baterias_carregando.remove(bateria_encontrada)
            baterias_disponiveis += 1

            print("Bateria recarregada com sucesso!\n")

            mostrar_status()

        except ValueError:
            print("Digite um número válido.\n")

    elif opcao == "3":
        mostrar_status()
        consultar_bateria()

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