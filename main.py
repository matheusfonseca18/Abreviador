import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkfont
from abreviar import abreviar_marca, abreviar_versao, anunciante


def pegar_texto(entrada):
    return entrada.get()


def copiar(entrada):
    root.clipboard_clear()
    root.clipboard_append(entrada)


def trocar(saida, abreviada):
    saida.configure(state='normal')
    saida.delete(1.0, ctk.END)
    saida.insert("1.0", abreviada, "center")
    saida.configure(state='disabled')


def formatar_anunciante():
    entrada_anunciante = pegar_texto(anunciante_entry)
    anunciante_formatado = anunciante(entrada_anunciante)
    trocar(anunciante_saida, anunciante_formatado)

    copiar(anunciante_formatado)


def formatar_marca():
    entrada_marca = pegar_texto(marca_entry)
    marca_abreviada = abreviar_marca(entrada_marca)
    trocar(marca_saida, marca_abreviada)

    copiar(marca_abreviada)


def formatar_versao():
    entrada_versao = pegar_texto(versao_entry)
    versao_formatada = abreviar_versao(entrada_versao)
    trocar(versao_saida, versao_formatada)

    copiar(versao_formatada)


ctk.set_appearance_mode("system")

root = ctk.CTk()
root.geometry("500x600")
root.title("Abreviador")
root.iconbitmap('icon.ico')

default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(family="tahoma", size=12)

# Tabs
tabControl = ctk.CTkTabview(root, segmented_button_fg_color="#333333",         # fundo do botão
    segmented_button_selected_color="#7E15C0",   # aba ativa (laranja)
    segmented_button_unselected_color="#666666", # abas inativas (cinza)
    segmented_button_selected_hover_color="#570D85",
    segmented_button_unselected_hover_color="#555555")
tabControl.pack(expand=True, fill="both")

janela = tabControl.add("Abreviar")
janela2 = tabControl.add("Instruções")

# --- Aba Abreviar ---
# Anunciante
anunciante_label = ctk.CTkLabel(janela, text="Insira o anunciante:", font=('tahoma', 14, 'bold'), text_color='white')
anunciante_label.pack(pady=(10, 0))

anunciante_entry = ctk.CTkEntry(janela, width=400)
anunciante_entry.pack()

anunciante_saida = ctk.CTkTextbox(janela, width=400, height=10)
anunciante_saida.pack(pady=10)

anunciante_saida.tag_config("center", justify="center")

anunciante_saida.insert("1.0", "Seu texto aparecerá aqui", "center")
anunciante_saida.configure(state="disabled")

anunciante_btn = ctk.CTkButton(
    janela, text="Formatar", command=formatar_anunciante, fg_color="#7E15C0", hover_color="#570D85", text_color='white')
anunciante_btn.pack(pady=15)

# Marca
marca_label = ctk.CTkLabel(janela, text="Insira a marca:", font=('tahoma', 14, 'bold'), text_color='white')
marca_label.pack(pady=(10, 0))

marca_entry = ctk.CTkEntry(janela, width=400)
marca_entry.pack()

marca_saida = ctk.CTkTextbox(janela, width=400, height=10)
marca_saida.pack(pady=10)

marca_saida.tag_config("center", justify="center")

marca_saida.insert("1.0", "Seu texto aparecerá aqui", "center")
marca_saida.configure(state="disabled")

marca_btn = ctk.CTkButton(janela, text="Formatar", command=formatar_marca, fg_color="#7E15C0", hover_color="#570D85", text_color='white')
marca_btn.pack(pady=15)

# Versão
versao_label = ctk.CTkLabel(janela, text="Insira a versão:", font=('tahoma', 14, 'bold'), text_color='white')
versao_label.pack(pady=(10, 0))

versao_entry = ctk.CTkEntry(janela, width=400)
versao_entry.pack()

versao_saida = ctk.CTkTextbox(janela, width=400, height=10)
versao_saida.pack(pady=10)

versao_saida.tag_config("center", justify="center")

versao_saida.insert("1.0", "Seu texto aparecerá aqui", "center")
versao_saida.configure(state="disabled")

versao_btn = ctk.CTkButton(janela, text="Formatar", command=formatar_versao, fg_color="#7E15C0", hover_color="#570D85", text_color='white')
versao_btn.pack(pady=15)


# --- Aba Instruções ---
titulo_gerais = ctk.CTkLabel(janela2, text="Como usar", font=('tahoma', 14, 'bold'), justify="center", text_color='white')
titulo_gerais.pack()

instr_gerais = ctk.CTkLabel(janela2, text="Utilize o campo correto para sua necessidade.\nDigite ou cole o dado na entrada correta e clique no botão formatar. O resultado aparecerá no campo abaixo da entrada, “Seu texto aparecerá aqui“, e já estará no seu CTRL + V.", wraplength=400,
    justify="center", text_color='white')
instr_gerais.pack(pady=(0, 20))

titulo_anunciante = ctk.CTkLabel(janela2, text="Anunciante", font=('tahoma', 14, 'bold'), justify="center", text_color='white')
titulo_anunciante.pack()

instr_anunciante = ctk.CTkLabel(
    janela2,
    text="Remove os espaços excedentes, acentos e caracteres especiais, formata a frase deixando a primeira letra de cada palavra em maiúsculo, não possui limite de caracteres.",
    wraplength=400,
    justify="center", text_color='white'
)
instr_anunciante.pack(pady=(0, 20))

titulo_marca = ctk.CTkLabel(janela2, text="Marca", font=('tahoma', 14, 'bold'), justify="center", text_color='white')
titulo_marca.pack()

instr_marca = ctk.CTkLabel(janela2, text="Remove os espaços excedentes, acentos, caracteres especiais e preposições. Abrevia até o limite de 30 caracteres, abreviação sempre termina com consoante, saída com toda a frase em maiúscula. mantem a marca principal (primeira palavra) integra o máximo possível, caso contrário, é a última a ser abreviada.", wraplength=400,
    justify="center", text_color='white')
instr_marca.pack(pady=(0, 20))

titulo_versao = ctk.CTkLabel(janela2, text="Versão", font=('tahoma', 14, 'bold'), justify="center", text_color='white')
titulo_versao.pack()

instr_versao = ctk.CTkLabel(
    janela2,
    text="Remove os espaços excedentes, acentos, caracteres especiais e preposições. "
         "Abrevia até o limite de 30 caracteres, abreviação sempre termina com consoante, "
         "saída com toda a frase em maiúscula.\n"
         "Não abrevia palavras \"blindadas\", são elas:\n"
         "'GLOBO', 'SBT', 'RECORD', 'REDETV', 'BAND', 'CULTURA', 'ESPN', "
         "'SPORTV', 'TNT', 'MAT', 'VES', 'NOT', 'MAD', 'FUT', 'BOLETIM'.\n"
         "Em casos de BOLETIM, troca para BOL apenas se não for possível abreviar nenhuma outra palavra.",
    wraplength=400,
    justify="center", text_color='white'
)

instr_versao.pack(pady=(0, 20))

root.mainloop()
