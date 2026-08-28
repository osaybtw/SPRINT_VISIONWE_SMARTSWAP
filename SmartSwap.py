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

# Mostrar status das baterias
def mostrar_status():
    return {
        "total_baterias": total_baterias,
        "baterias_disponiveis": baterias_disponiveis,
        "baterias_carregando": len(baterias_carregando),
        "estoque_critico": baterias_disponiveis <= 1
    }


# Buscar alguma bateria específica
def consultar_bateria(escolha):

    if escolha < 1 or escolha > len(lista_baterias):
        return None

    for bateria in lista_baterias:

        if bateria[0] == escolha:
            return bateria

    return None


# Função para registrar a troca de baterias
def registrar_troca(energia_restante):

    global baterias_disponiveis

    if baterias_disponiveis <= 0:
        return None

    if energia_restante < 0 or energia_restante > 100:
        return None

    percentual_utilizado = 100 - energia_restante

    energia_utilizada_kwh = ( percentual_utilizado / 100) * capacidade_bateria

    valor_energia = energia_utilizada_kwh * preco_kwh
    valor_total = valor_energia + taxa_servico

    for bateria in lista_baterias:

        if bateria[1] == 100 and bateria not in baterias_carregando:

            bateria[1] = energia_restante
            baterias_carregando.append(bateria)

            baterias_disponiveis -= 1

            historico_valor.append({
                "bateria": bateria[0],
                "energia_utilizada": energia_utilizada_kwh,
                "valor_energia": valor_energia,
                "taxa_servico": taxa_servico,
                "valor_total": valor_total
            })
            
            return {
                "numero_da_bateria": bateria[0],
                "carga_restante": energia_restante,
                "energia_utilizada": energia_utilizada_kwh,
                "valor_energia": valor_energia,
                "taxa_servico": taxa_servico,
                "valor_total": valor_total
            }

    return None

def mostrar_relatorio_financeiro():

    quantidade = len(historico_valor)

    total = 0

    for troca in historico_valor:
        total += troca["valor_total"]

    if quantidade > 0:
        media = total / quantidade
    else:
        media = 0

    return {
        "quantidade": quantidade,
        "total": total,
        "media": media
    }


# Função para recarregar a bateria
def finalizar_recarga(escolha):

    global baterias_disponiveis

    bateria_encontrada = None

    for bateria in baterias_carregando:

        if bateria[0] == escolha:
            bateria_encontrada = bateria
            break

    if bateria_encontrada is None:
        return None

    bateria_encontrada[1] = 100
    baterias_carregando.remove(bateria_encontrada)
    baterias_disponiveis += 1

    return bateria_encontrada