# backend

total_baterias = 20
baterias_disponiveis = 20
baterias_carregando = []
historico_valor = []

capacidade_bateria = 60
preco_kwh = 2.00
taxa_servico = 10.00

lista_baterias = []

for i in range(1, total_baterias + 1):
    lista_baterias.append([i, 100])


def mostrar_status():
    return {
        "total_baterias": total_baterias,
        "baterias_disponiveis": baterias_disponiveis,
        "baterias_carregando": len(baterias_carregando),
        "estoque_critico": baterias_disponiveis <= 1
    }


def consultar_bateria(escolha):

    if escolha < 1 or escolha > len(lista_baterias):
        return None

    for bateria in lista_baterias:

        if bateria[0] == escolha:
            return bateria

    return None


def registrar_troca(energia_restante):

    if baterias_disponiveis <= 0:
        return None

    if energia_restante < 0 or energia_restante > 100:
        return None

    percentual_utilizado = 100 - energia_restante

    energia_utilizada_kwh = ( percentual_utilizado / 100) * capacidade_bateria

    valor_energia = energia_utilizada_kwh * preco_kwh
    valor_total = valor_energia + taxa_servico

    for bateria in lista_baterias:

        if bateria[1] == 100:

            bateria[1] = energia_restante
            baterias_carregando.append(bateria)

            baterias_disponiveis -= 1

            break

        return {
    "numero_da_bateria": bateria[0],
    "carga_restante": energia_restante,
    "energia_utilizada": energia_utilizada_kwh,
    "valor_energia": valor_energia,
    "taxa_servico": taxa_servico,
    "valor_total": valor_total
}