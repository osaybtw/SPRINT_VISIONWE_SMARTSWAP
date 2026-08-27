# frontend
import tkinter as tk
import SmartSwap

# Janela da interface

janela = tk.Tk()

janela.title("SmartSwap")
janela.geometry("800x600")

# Caixa do título

titulo = tk.Label(
    janela,
    text="SMARTSWAP",
    font=("Arial", 24)
)

titulo.pack(pady=30)

# Caixa de status

status = tk.Label(
    janela,
    text=f"Baterias totais: {SmartSwap.total_baterias}\n"
         f"Baterias disponíveis: {SmartSwap.baterias_disponiveis}\n"
         f"Baterias carregando: {len(SmartSwap.baterias_carregando)}",
    font=("Arial", 16)
)

status.pack(pady=20)

# Caixa para digitar o numero da bateria
entrada = tk.Entry(janela, font=("Arial", 16))
entrada.pack(pady=10)


# Função executada quando o botão for clicado
def clicar_consultar():

    escolha = int(entrada.get())

    bateria = SmartSwap.consultar_bateria(escolha)

    if bateria is not None:
        resultado.config(
            text=f"Bateria {bateria[0]}\n"
                 f"Carga: {bateria[1]}%"
        )
    else:
        resultado.config(
            text="Bateria não encontrada."
        )


# Botão
botao = tk.Button(
    janela,
    text="Consultar bateria",
    font=("Arial", 14),
    command=clicar_consultar
)

botao.pack(pady=10)


# Texto onde mostrar o resultado
resultado = tk.Label(
    janela,
    text="",
    font=("Arial", 16)
)

resultado.pack(pady=20)

janela.mainloop()