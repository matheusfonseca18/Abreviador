import customtkinter as ctk
import tkinter as tk
from tkinter import StringVar
import tkinter.font as tkfont
import os
import sys
from abreviar import abreviar_marca, abreviar_versao, anunciante, atualizar_contagem, atualizar_contagem_anuncante


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


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

    tamanho = len(anunciante_formatado)
    anunciante_saida_contagem.configure(text=tamanho)


def formatar_marca():
    entrada_marca = pegar_texto(marca_entry)
    marca_abreviada = abreviar_marca(entrada_marca)
    trocar(marca_saida, marca_abreviada)

    copiar(marca_abreviada)

    tamanho = len(marca_abreviada)
    marca_saida_contagem.configure(text=tamanho, text_color='green')


def formatar_versao():
    entrada_versao = pegar_texto(versao_entry)
    versao_formatada = abreviar_versao(entrada_versao)
    trocar(versao_saida, versao_formatada)

    copiar(versao_formatada)

    tamanho = len(versao_formatada)
    versao_saida_contagem.configure(text=tamanho, text_color='green')


ctk.set_appearance_mode("system")

DEFAULT_FG_COLOR = ("black", "white")

root = ctk.CTk()
root.geometry("500x600")
root.title("Abreviador - 1.4.2")
root.iconbitmap(resource_path('icon.ico'))

default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(family="tahoma", size=12)


# Tabs
tabControl = ctk.CTkTabview(root, segmented_button_selected_color="#7E15C0",   # aba ativa (laranja)
                            # abas inativas (cinza)
                            segmented_button_unselected_color="#666666",
                            segmented_button_selected_hover_color="#570D85",
                            segmented_button_unselected_hover_color="#555555")
tabControl.pack(expand=True, fill="both")


janela = tabControl.add("Abreviar")
janela2 = tabControl.add("Instruções")


# --- Aba Abreviar ---
# Anunciante
anunciante_var = StringVar()

anunciante_label = ctk.CTkLabel(
    janela, text="Insira o anunciante:", font=('tahoma', 14, 'bold'))
anunciante_label.pack(pady=(10, 0))

anunciante_input_container = ctk.CTkFrame(janela, fg_color="transparent")
anunciante_input_container.pack()

anunciante_entry = ctk.CTkEntry(anunciante_input_container, width=350, textvariable=anunciante_var)
anunciante_entry.grid(row=0, column=0, padx=(0, 10))

anunciante_input_contagem = ctk.CTkLabel(anunciante_input_container, text="0")
anunciante_input_contagem.grid(row=0, column=1)

anunciante_var.trace_add("write", lambda *args: atualizar_contagem_anuncante(anunciante_entry, anunciante_input_contagem))

anunciante_saida_container = ctk.CTkFrame(janela, fg_color="transparent")
anunciante_saida_container.pack()

anunciante_saida = ctk.CTkTextbox(anunciante_saida_container, width=350, height=10)
anunciante_saida.grid(row=0, column=0, padx=(0, 10))

anunciante_saida.tag_config("center", justify="center")

anunciante_saida.insert("1.0", "Seu texto aparecerá aqui", "center")
anunciante_saida.configure(state="disabled")

anunciante_saida_contagem = ctk.CTkLabel(anunciante_saida_container, text="0")
anunciante_saida_contagem.grid(row=0, column=1)

anunciante_btn = ctk.CTkButton(
    janela, text="Formatar", command=formatar_anunciante, fg_color="#7E15C0", hover_color="#570D85", text_color='white')
anunciante_btn.pack(pady=15)


# Marca
marca_var = StringVar()

marca_label = ctk.CTkLabel(
    janela, text="Insira a marca:", font=('tahoma', 14, 'bold'))
marca_label.pack(pady=(10, 0))

marca_input_container = ctk.CTkFrame(janela, fg_color="transparent")
marca_input_container.pack()

marca_entry = ctk.CTkEntry(marca_input_container, width=350, textvariable=marca_var)
marca_entry.grid(row=0, column=0, padx=(0, 10))

marca_input_contagem = ctk.CTkLabel(marca_input_container, text="0")
marca_input_contagem.grid(row=0, column=1)

marca_var.trace_add("write", lambda *args: atualizar_contagem(marca_entry, marca_input_contagem, DEFAULT_FG_COLOR))

marca_saida_container = ctk.CTkFrame(janela, fg_color="transparent")
marca_saida_container.pack()

marca_saida = ctk.CTkTextbox(marca_saida_container, width=350, height=10)
marca_saida.grid(row=0, column=0, padx=(0, 10))

marca_saida.tag_config("center", justify="center")

marca_saida.insert("1.0", "Seu texto aparecerá aqui", "center")
marca_saida.configure(state="disabled")

marca_saida_contagem = ctk.CTkLabel(marca_saida_container, text="0")
marca_saida_contagem.grid(row=0, column=1)

marca_btn = ctk.CTkButton(janela, text="Formatar", command=formatar_marca,
                          fg_color="#7E15C0", hover_color="#570D85", text_color='white')
marca_btn.pack(pady=15)


# Versão
versao_var = StringVar()

versao_label = ctk.CTkLabel(
    janela, text="Insira a versão:", font=('tahoma', 14, 'bold'))
versao_label.pack(pady=(10, 0))

versao_input_container = ctk.CTkFrame(janela, fg_color="transparent")
versao_input_container.pack() 

versao_entry = ctk.CTkEntry(versao_input_container, width=350, textvariable=versao_var)
versao_entry.grid(row=0, column=0, padx=(0, 10))

versao_input_contagem = ctk.CTkLabel(versao_input_container, text="0")
versao_input_contagem.grid(row=0, column=1)

versao_var.trace_add("write", lambda *args: atualizar_contagem(versao_entry, versao_input_contagem, DEFAULT_FG_COLOR))

versao_saida_container = ctk.CTkFrame(janela, fg_color="transparent")
versao_saida_container.pack() 

versao_saida = ctk.CTkTextbox(versao_saida_container, width=350, height=10)
versao_saida.grid(row=0, column=0, padx=(0, 10))

versao_saida.tag_config("center", justify="center")

versao_saida.insert("1.0", "Seu texto aparecerá aqui", "center")
versao_saida.configure(state="disabled")

versao_saida_contagem = ctk.CTkLabel(versao_saida_container, text="0")
versao_saida_contagem.grid(row=0, column=1)

versao_btn = ctk.CTkButton(janela, text="Formatar", command=formatar_versao,
                           fg_color="#7E15C0", hover_color="#570D85")
versao_btn.pack(pady=15)


# --- Aba Instruções ---
titulo_gerais = ctk.CTkLabel(janela2, text="Como usar", font=(
    'tahoma', 14, 'bold'), justify="center")
titulo_gerais.pack()

instr_gerais = ctk.CTkLabel(janela2, text="Utilize o campo correto para sua necessidade.\nDigite ou cole o dado na entrada correta e clique no botão formatar. O resultado aparecerá no campo abaixo da entrada, “Seu texto aparecerá aqui“, e já estará no seu CTRL + V.", wraplength=400,
                            justify="center")
instr_gerais.pack(pady=(0, 20))

titulo_anunciante = ctk.CTkLabel(janela2, text="Anunciante", font=(
    'tahoma', 14, 'bold'), justify="center")
titulo_anunciante.pack()

instr_anunciante = ctk.CTkLabel(
    janela2,
    text="Remove os espaços excedentes, acentos e caracteres especiais, formata a frase deixando a primeira letra de cada palavra em maiúsculo, não possui limite de caracteres.",
    wraplength=400,
    justify="center"
)
instr_anunciante.pack(pady=(0, 20))

titulo_marca = ctk.CTkLabel(janela2, text="Marca", font=(
    'tahoma', 14, 'bold'), justify="center")
titulo_marca.pack()

instr_marca = ctk.CTkLabel(janela2, text="Remove os espaços excedentes, acentos, caracteres especiais e preposições. Abrevia até o limite de 30 caracteres, abreviação sempre termina com consoante, saída com toda a frase em maiúscula. mantem a marca principal (primeira palavra) integra o máximo possível, caso contrário, é a última a ser abreviada.", wraplength=400,
                           justify="center")
instr_marca.pack(pady=(0, 20))

titulo_versao = ctk.CTkLabel(janela2, text="Versão", font=(
    'tahoma', 14, 'bold'), justify="center")
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
    justify="center")

instr_versao.pack(pady=(0, 20))

root.mainloop()
