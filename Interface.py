# frontend
import tkinter as tk
import SmartSwap

# Janela do programa

janela = tk.Tk()

janela.title("SmartSwap")
janela.geometry("1000x750")

# Caixa do título

label_titulo = tk.Label(
    janela,
    text="SMARTSWAP",
    font=("Arial", 24)
)

label_titulo.pack(pady=30)

# Área do conteúdo
frame_conteudo = tk.Frame(janela)
frame_conteudo.pack(pady=20)

# Caixa de status
label_status_baterias = tk.Label(
    janela,
    text=f"Baterias totais: {SmartSwap.total_baterias}\n"
         f"Baterias disponíveis: {SmartSwap.baterias_disponiveis}\n"
         f"Baterias carregando: {len(SmartSwap.baterias_carregando)}",
    font=("Arial", 16)
)

label_status_baterias.pack(pady=20)


# Função para atualizar o status

def atualizar_status():
    status = SmartSwap.mostrar_status()

    label_status_baterias.config(
        text=f"Baterias totais: {status['total_baterias']}\n"
             f"Baterias disponíveis: {status['baterias_disponiveis']}\n"
             f"Baterias carregando: {status['baterias_carregando']}"
    )

# Troca de bateria
label_entrada_energia = tk.Label(
    frame_conteudo,
    text="Porcentagem restante da bateria:",
    font=("Arial", 14)
)

entrada_energia = tk.Entry(
    frame_conteudo,
    font=("Arial", 16)
)

# Resultado da troca/recarga
label_resultado_troca = tk.Label(
    frame_conteudo,
    text="",
    font=("Arial", 14)
)


# Recarga de bateria

label_entrada_recarga = tk.Label(
    frame_conteudo,
    text="Número da bateria que terminou de carregar:",
    font=("Arial", 14)
)

entrada_recarga = tk.Entry(
    frame_conteudo,
    font=("Arial", 16)
)

# Consulta de bateria específica
label_entrada_bateria = tk.Label(
    frame_conteudo,
    text="Número da bateria:",
    font=("Arial", 14)
)

entrada_bateria = tk.Entry(
    frame_conteudo,
    font=("Arial", 16)
)

label_resultado_bateria = tk.Label(
    frame_conteudo,
    text="",
    font=("Arial", 14)
)

# Resultado do relatório financeiro
label_resultado_financeiro = tk.Label(
    frame_conteudo,
    text="",
    font=("Arial", 14)
)

# Função para mostrar tela de troca
def mostrar_tela_troca():

    label_resultado_financeiro.pack_forget()

    label_entrada_recarga.pack_forget()
    entrada_recarga.pack_forget()
    botao_recarga.pack_forget()

    label_entrada_bateria.pack_forget()
    entrada_bateria.pack_forget()
    botao_consultar_bateria.pack_forget()
    label_resultado_bateria.pack_forget()

    label_entrada_energia.pack(pady=5)
    entrada_energia.pack(pady=10)
    botao_troca.pack(pady=10)
    label_resultado_troca.pack(pady=20)

# Função para mostrar tela de recarga
def mostrar_tela_recarga():

    label_resultado_financeiro.pack_forget()

    label_entrada_energia.pack_forget()
    entrada_energia.pack_forget()
    botao_troca.pack_forget()

    label_entrada_bateria.pack_forget()
    entrada_bateria.pack_forget()
    botao_consultar_bateria.pack_forget()
    label_resultado_bateria.pack_forget()

    label_entrada_recarga.pack(pady=5)
    entrada_recarga.pack(pady=10)
    botao_recarga.pack(pady=10)
    label_resultado_troca.pack(pady=20)

# Função para mostrar tela de consulta
def mostrar_tela_consulta():

    label_resultado_financeiro.pack_forget()

    # Esconde os elementos da troca
    label_entrada_energia.pack_forget()
    entrada_energia.pack_forget()
    botao_troca.pack_forget()

    # Esconde os elementos da recarga
    label_entrada_recarga.pack_forget()
    entrada_recarga.pack_forget()
    botao_recarga.pack_forget()
    label_resultado_troca.pack_forget()

    # Mostra os elementos da consulta
    label_entrada_bateria.pack(pady=5)
    entrada_bateria.pack(pady=10)
    botao_consultar_bateria.pack(pady=10)
    label_resultado_bateria.pack(pady=20)

# Função executada quando o botão de troca for clicado
def registrar_troca_interface():

    try:

        energia_restante = float(
            entrada_energia.get()
        )

    except ValueError:

        label_resultado_troca.config(
            text="Digite uma porcentagem válida."
        )

        return

    if energia_restante < 0 or energia_restante > 100:

        label_resultado_troca.config(
            text="Digite uma porcentagem entre 0% e 100%."
        )

        return

    resultado_troca = SmartSwap.registrar_troca(
        energia_restante
    )

    if resultado_troca is not None:

        label_resultado_troca.config(
            text=f"Bateria {resultado_troca['numero_da_bateria']} registrada!\n"
                 f"Carga restante: {resultado_troca['carga_restante']}%\n"
                 f"Energia utilizada: {resultado_troca['energia_utilizada']:.2f} kWh\n"
                 f"Valor da energia: R$ {resultado_troca['valor_energia']:.2f}\n"
                 f"Taxa de serviço: R$ {resultado_troca['taxa_servico']:.2f}\n"
                 f"Total: R$ {resultado_troca['valor_total']:.2f}"
        )

        atualizar_status()

    else:

        label_resultado_troca.config(
            text="Não foi possível realizar a troca."
        )


# Botão para registrar a troca
botao_troca = tk.Button(
    frame_conteudo,
    text="Registrar troca",
    font=("Arial", 14),
    command=registrar_troca_interface
)


# Função para consultar bateria
def consultar_bateria_interface():

    try:

        escolha = int(
            entrada_bateria.get()
        )

    except ValueError:

        label_resultado_bateria.config(
            text="Digite um número de bateria válido."
        )

        return

    bateria = SmartSwap.consultar_bateria(escolha)

    if bateria is None:

        label_resultado_bateria.config(
            text="Bateria não encontrada."
        )

        return

    if bateria[1] == 100:

        status_bateria = "Disponível"

    else:

        status_bateria = "Carregando"

    label_resultado_bateria.config(
        text=f"Bateria {bateria[0]}\n"
             f"Carga: {bateria[1]}%\n"
             f"Status: {status_bateria}"
    )

# Função para mostrar o relatório financeiro
def mostrar_tela_financeiro():

    # Esconde os elementos da troca
    label_entrada_energia.pack_forget()
    entrada_energia.pack_forget()
    botao_troca.pack_forget()
    label_resultado_troca.pack_forget()

    # Esconde os elementos da recarga
    label_entrada_recarga.pack_forget()
    entrada_recarga.pack_forget()
    botao_recarga.pack_forget()

    # Esconde os elementos da consulta
    label_entrada_bateria.pack_forget()
    entrada_bateria.pack_forget()
    botao_consultar_bateria.pack_forget()
    label_resultado_bateria.pack_forget()

    # Busca os dados do relatório
    relatorio = SmartSwap.mostrar_relatorio_financeiro()

    # Mostra o relatório
    label_resultado_financeiro.pack(pady=20)

    label_resultado_financeiro.config(
    text=f"RELATÓRIO FINANCEIRO\n\n"
         f"Trocas realizadas: {relatorio['quantidade']}\n"
         f"Receita total: R$ {relatorio['total']:.2f}\n"
         f"Média por troca: R$ {relatorio['media']:.2f}"
    )

# Função executada quando finalizar a recarga
def finalizar_recarga_interface():

    try:

        escolha = int(
            entrada_recarga.get()
        )

    except ValueError:

        label_resultado_troca.config(
            text="Digite um número de bateria válido."
        )

        return

    resultado_recarga = SmartSwap.finalizar_recarga(
        escolha
    )

    if resultado_recarga is not None:

        label_resultado_troca.config(
            text=f"Bateria {resultado_recarga[0]} recarregada!\n"
                 f"Carga atual: {resultado_recarga[1]}%"
        )

        atualizar_status()

    else:

        label_resultado_troca.config(
            text="Bateria não encontrada ou não está em recarga."
        )


# Botão para consultar bateria
botao_consultar_bateria = tk.Button(
    frame_conteudo,
    text="Consultar bateria",
    font=("Arial", 14),
    command=consultar_bateria_interface
)

# Botão para finalizar a recarga
botao_recarga = tk.Button(
    frame_conteudo,
    text="Finalizar recarga",
    font=("Arial", 14),
    command=finalizar_recarga_interface
)

# Menu principal
botao_trocar = tk.Button(
    janela,
    text="Trocar bateria",
    font=("Arial", 14),
    command=mostrar_tela_troca
)

botao_trocar.pack(pady=5)


botao_recarregar = tk.Button(
    janela,
    text="Recarregar bateria",
    font=("Arial", 14),
    command=mostrar_tela_recarga
)

botao_recarregar.pack(pady=5)

botao_consultar = tk.Button(
    janela,
    text="Consultar baterias",
    font=("Arial", 14),
    command=mostrar_tela_consulta
)

botao_consultar.pack(pady=5)

botao_financeiro = tk.Button(
    janela,
    text="Relatorio financeiro",
    font=("Arial", 14),
    command=mostrar_tela_financeiro
)

botao_financeiro.pack(pady=5)

janela.mainloop()