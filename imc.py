#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

# Função para calcular o IMC e atualizar a interface
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        label_resultado.config(text=f"Seu IMC é: {imc:.2f}")
        atualizar_barra(imc)
        atualizar_categoria(imc)
    except ValueError:
        label_resultado.config(text="Por favor, insira valores válidos.")
        label_categoria.config(text="")

# Função para atualizar a barra indicadora de IMC
def atualizar_barra(imc):
    if imc < 18.5:
        barra_indicadora.config(value=imc, style="AbaixoDoPeso.Horizontal.TProgressbar")
    elif imc < 25:
        barra_indicadora.config(value=imc, style="PesoNormal.Horizontal.TProgressbar")
    elif imc < 30:
        barra_indicadora.config(value=imc, style="Sobrepeso.Horizontal.TProgressbar")
    elif imc < 35:
        barra_indicadora.config(value=imc, style="ObesidadeLeve.Horizontal.TProgressbar")
    elif imc < 40:
        barra_indicadora.config(value=imc, style="ObesidadeModerada.Horizontal.TProgressbar")
    else:
        barra_indicadora.config(value=imc, style="ObesidadeMorbida.Horizontal.TProgressbar")

# Função para atualizar a categoria de IMC
def atualizar_categoria(imc):
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso Normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    elif imc < 35:
        categoria = "Obesidade Leve"
    elif imc < 40:
        categoria = "Obesidade Moderada"
    else:
        categoria = "Obesidade Mórbida"
    label_categoria.config(text=categoria)

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("300x300")

# Estilo e temas (foco no tema escuro)
style = ttk.Style(root)
style.theme_use("clam")

# Configurações do tema escuro
style.configure("TFrame", background="#2C2C2C")
style.configure("TLabel", background="#2C2C2C", foreground="white", font=('Arial', 10))
style.configure("TButton", background="#1C1C1C", foreground="white", font=('Arial', 10))
style.configure("TEntry", foreground="black", font=('Arial', 10))
style.configure("TProgressbar", troughcolor="#4D4D4D", background="green")

style.configure("AbaixoDoPeso.Horizontal.TProgressbar", background="white")
style.configure("PesoNormal.Horizontal.TProgressbar", background="green")
style.configure("Sobrepeso.Horizontal.TProgressbar", background="blue")
style.configure("ObesidadeLeve.Horizontal.TProgressbar", background="yellow")
style.configure("ObesidadeModerada.Horizontal.TProgressbar", background="orange")
style.configure("ObesidadeMorbida.Horizontal.TProgressbar", background="red")

# Widgets da interface
frame_principal = ttk.Frame(root, padding="10")
frame_principal.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

label_peso = ttk.Label(frame_principal, text="Peso (kg):")
label_peso.grid(row=0, column=0, sticky=tk.W, pady=5)

entry_peso = ttk.Entry(frame_principal, width=10)
entry_peso.grid(row=0, column=1, pady=5)

label_altura = ttk.Label(frame_principal, text="Altura (m):")
label_altura.grid(row=1, column=0, sticky=tk.W, pady=5)

entry_altura = ttk.Entry(frame_principal, width=10)
entry_altura.grid(row=1, column=1, pady=5)

botao_calcular = ttk.Button(frame_principal, text="Calcular", command=calcular_imc)
botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)

label_resultado = ttk.Label(frame_principal, text="")
label_resultado.grid(row=3, column=0, columnspan=2, pady=5)

label_categoria = ttk.Label(frame_principal, text="")
label_categoria.grid(row=4, column=0, columnspan=2, pady=5)

barra_indicadora = ttk.Progressbar(frame_principal, length=200, maximum=40, mode="determinate")
barra_indicadora.grid(row=5, column=0, columnspan=2, pady=10)

frame_principal.columnconfigure(0, weight=1)
frame_principal.columnconfigure(1, weight=1)

root.mainloop()
