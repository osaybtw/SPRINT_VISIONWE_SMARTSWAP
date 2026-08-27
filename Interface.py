# frontend
import tkinter as tk
import SmartSwap

# Janela da interface

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

# Caixa de status

label_status_baterias = tk.Label(
    janela,
    text=f"Baterias totais: {SmartSwap.total_baterias}\n"
         f"Baterias disponíveis: {SmartSwap.baterias_disponiveis}\n"
         f"Baterias carregando: {len(SmartSwap.baterias_carregando)}",
    font=("Arial", 16)
)

label_status_baterias.pack(pady=20)

# Caixa label digite energia restante

label_entrada_energia = tk.Label(
    janela,
    text="Porcentagem restante da bateria:",
    font=("Arial", 14)
)

label_entrada_energia.pack(pady=5)

# Caixa para digitar a carga restante
entrada_energia = tk.Entry(
    janela,
    font=("Arial", 16)
)

entrada_energia.pack(pady=10)

# Função para atualizar o status depois da troca

def atualizar_status():
    status = SmartSwap.mostrar_status()

    label_status_baterias.config(
        text=f"Baterias totais: {status['total_baterias']}\n"
             f"Baterias disponíveis: {status['baterias_disponiveis']}\n"
             f"Baterias carregando: {status['baterias_carregando']}"
    )

# Função executada quando o botão for clicado
def registrar_troca_interface():

    energia_restante = float(entrada_energia.get())

    resultado_troca = SmartSwap.registrar_troca(energia_restante)

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
    janela,
    text="Registrar troca",
    font=("Arial", 14),
    command=registrar_troca_interface
)

botao_troca.pack(pady=10)


# Texto onde mostrar o resultado
label_resultado_troca = tk.Label(
    janela,
    text="",
    font=("Arial", 14)
)

label_resultado_troca.pack(pady=20)

# Caixa para digitar o número da bateria que terminou de carregar

label_entrada_recarga = tk.Label(
    janela,
    text="Número da bateria que terminou de carregar:",
    font=("Arial", 14)
)

label_entrada_recarga.pack(pady=5)


entrada_recarga = tk.Entry(
    janela,
    font=("Arial", 16)
)

entrada_recarga.pack(pady=10)


# Função executada quando finalizar a recarga

def finalizar_recarga_interface():

    escolha = int(entrada_recarga.get())

    resultado_recarga = SmartSwap.finalizar_recarga(escolha)

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


# Botão para finalizar a recarga

botao_recarga = tk.Button(
    janela,
    text="Finalizar recarga",
    font=("Arial", 14),
    command=finalizar_recarga_interface
)

botao_recarga.pack(pady=10)

janela.mainloop()