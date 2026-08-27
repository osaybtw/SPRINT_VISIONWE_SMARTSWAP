# frontend
import tkinter as tk
import SmartSwap

janela = tk.Tk()

janela.title("SmartSwap")
janela.geometry("800x600")

titulo = tk.Label(
    janela,
    text="SMARTSWAP",
    font=("Arial", 24)
)

titulo.pack(pady=30)

status = tk.Label(
    janela,
    text=f"Baterias disponíveis: {SmartSwap.baterias_disponiveis}\n"
         f"Baterias carregando: {len(SmartSwap.baterias_carregando)}",
    font=("Arial", 16)
)

status.pack(pady=20)

janela.mainloop()