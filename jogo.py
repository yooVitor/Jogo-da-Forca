import random
import os
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox

# -------- Classe Palavra --------
class Palavra:
    def __init__(self, palavra_secreta):
        self.palavra_secreta = palavra_secreta.lower()
        self.representacao = ['_' for _ in self.palavra_secreta]
        self.erros_restantes = 6
        self.letras_certas = set()
        self.letras_erradas = set()
        self.pontos = 0  # Pontuação removida da lógica fixa

    def tentar_letra(self, letra):
        letra = letra.lower()

        if letra in self.letras_certas or letra in self.letras_erradas:
            return "Letra já tentada."

        if letra in self.palavra_secreta:
            self.letras_certas.add(letra)
            for i, l in enumerate(self.palavra_secreta):
                if l == letra:
                    self.representacao[i] = letra
            return "Acertou!"
        else:
            self.letras_erradas.add(letra)
            self.erros_restantes -= 1
            return "Errou!"

    def palavra_atual(self):
        return " ".join(self.representacao)

    def jogo_terminado(self):
        return self.erros_restantes == 0 or '_' not in self.representacao

    def venceu(self):
        return '_' not in self.representacao

# -------- Funções auxiliares --------
def carregar_palavras(arquivo):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, 'r', encoding='utf-8') as f:
        return [linha.strip() for linha in f if linha.strip()]

def salvar_pontuacao(nome, venceu):
    pontuacoes = {}

    if os.path.exists("pontuacoes.txt"):
        with open("pontuacoes.txt", "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha: 
                    continue
                partes = linha.split(":")
                jogador = partes[0].strip()
                dados = partes[1].strip().split("|")
                vitorias = int(dados[0].strip().split()[1])
                derrotas = int(dados[1].strip().split()[1])
                pontuacoes[jogador] = {"vit": vitorias, "der": derrotas}

    if nome not in pontuacoes:
        pontuacoes[nome] = {"vit": 0, "der": 0}
    if venceu:
        pontuacoes[nome]["vit"] += 1
    else:
        pontuacoes[nome]["der"] += 1

    with open("pontuacoes.txt", "w", encoding="utf-8") as f:
        for jogador, valores in pontuacoes.items():
            f.write(f"{jogador}: Vitórias {valores['vit']} | Derrotas {valores['der']}\n")

def mostrar_pontuacoes_popup():
    if not os.path.exists("pontuacoes.txt"):
        messagebox.showinfo("Pontuações", "Nenhuma pontuação registrada ainda.")
        return
    with open("pontuacoes.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
    messagebox.showinfo("Pontuações", conteudo)

def mostrar_pontuacoes_fim():
    if not os.path.exists("pontuacoes.txt"):
        return "Nenhuma pontuação registrada ainda."
    with open("pontuacoes.txt", "r", encoding="utf-8") as f:
        return f.read()

# -------- Funções do Jogo --------
def iniciar_jogo():
    global jogo, nome
    palavras = carregar_palavras("palavras.txt")
    if not palavras:
        messagebox.showerror("Erro", "Arquivo 'palavras.txt' não encontrado ou vazio.")
        return
    nome = entrada_nome.get().strip() or "Jogador"
    palavra_escolhida = random.choice(palavras)
    jogo = Palavra(palavra_escolhida)
    atualizar_tela()
    status_var.set(f"{nome}, o jogo começou! Boa sorte!")
    entrada_letra.config(state="normal")
    entrada_letra.focus()
    botao_tentar.config(state="normal")

def tentar_letra():
    global jogo
    letra = entrada_letra.get().lower()
    entrada_letra.delete(0, 'end')

    if not letra.isalpha() or len(letra) != 1:
        status_var.set("Digite apenas uma letra válida.")
        return

    resultado = jogo.tentar_letra(letra)
    atualizar_tela()
    status_var.set(resultado)

    if jogo.jogo_terminado():
        entrada_letra.config(state="disabled")
        botao_tentar.config(state="disabled")

        if jogo.venceu():
            salvar_pontuacao(nome, True)
            pontuacoes = mostrar_pontuacoes_fim()
            messagebox.showinfo("Vitória!", f"Parabéns {nome}, você venceu!\n\nPontuações:\n{pontuacoes}")
        else:
            salvar_pontuacao(nome, False)
            pontuacoes = mostrar_pontuacoes_fim()
            messagebox.showinfo("Derrota", f"{nome}, você perdeu!\nA palavra era: {jogo.palavra_secreta}\n\nPontuações:\n{pontuacoes}")

def reiniciar_jogo():
    entrada_letra.config(state="disabled")
    botao_tentar.config(state="disabled")
    palavra_var.set("")
    erros_var.set("")
    letras_var.set("")
    pontos_var.set("")
    status_var.set("Clique em Iniciar Jogo para começar.")

def atualizar_tela():
    palavra_var.set(jogo.palavra_atual())
    erros_var.set(f"Erros restantes: {jogo.erros_restantes}")
    letras_var.set(f"Erradas: {' '.join(sorted(jogo.letras_erradas))}")
    pontos_var.set(f"Pontos: {jogo.pontos}")

# -------- Funções do Aparência --------
def aplicar_tema():
    bg = "#121212" if tema_escuro else "#f0f0f0"
    fg = "#EEEEEE" if tema_escuro else "#000000"
    entrada_bg = "#1E1E1E" if tema_escuro else "white"
    entrada_fg = "#EEEEEE" if tema_escuro else "black"
    azul = "#1E88E5"
    verde = "#43A047"
    vermelho = "#E53935"

    janela.configure(bg=bg)

    titulo.config(bg=bg, fg=fg)
    nome_label.config(bg=bg, fg=fg)
    palavra_label.config(bg=bg, fg=fg)
    status_label.config(bg=bg, fg=azul)
    erros_label.config(bg=bg, fg=vermelho)
    letras_label.config(bg=bg, fg=fg)
    pontos_label.config(bg=bg, fg=verde)

    entrada_nome.config(bg=entrada_bg, fg=entrada_fg, insertbackground=entrada_fg)
    entrada_letra.config(bg=entrada_bg, fg=entrada_fg, insertbackground=entrada_fg)

    botao_tentar.config(bg=verde, fg="white", activebackground="#388E3C")
    botao_iniciar.config(bg=azul, fg="white", activebackground="#1565C0")
    botao_tema.config(bg="#888888", fg="white", activebackground="#555555")

def alternar_tema():
    global tema_escuro
    tema_escuro = not tema_escuro
    aplicar_tema()

# -------- Interface gráfica --------
janela = Tk()
janela.geometry("900x600")
janela.title("Jogo da Forca")

# Centralizar janela
largura = 900
altura = 600
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura // 2)
pos_y = (altura_tela // 2) - (altura // 2)
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

# Variáveis
palavra_var = StringVar()
status_var = StringVar()
erros_var = StringVar()
letras_var = StringVar()
pontos_var = StringVar()
nome = ""
jogo = None
tema_escuro = False

# Widgets
titulo = Label(janela, text="🎯 Jogo da Forca", font=("Arial Black", 26))
titulo.pack(pady=20)

nome_label = Label(janela, text="Digite seu nome:", font=("Arial", 12))
nome_label.pack()

entrada_nome = Entry(janela, font=("Arial", 12), justify="center", width=20)
entrada_nome.pack()

palavra_label = Label(janela, textvariable=palavra_var, font=("Courier New", 32))
palavra_label.pack(pady=20)

entrada_letra = Entry(janela, font=("Arial", 12), width=5, justify='center', state="disabled")
entrada_letra.pack()
entrada_letra.bind("<Return>", lambda event: tentar_letra())

botao_tentar = Button(janela, text="Tentar letra", font=("Arial", 11), width=15, command=tentar_letra, state="disabled")
botao_tentar.pack(pady=5)

botao_iniciar = Button(janela, text="Iniciar Jogo", font=("Arial", 11), width=15, command=iniciar_jogo)
botao_iniciar.pack(pady=10)

botao_reiniciar = Button(janela, text="Reiniciar", font=("Arial", 11), bg="#888888", fg="white", command=reiniciar_jogo, width=15)
botao_reiniciar.pack(pady=5)

botao_pontuacoes = Button(janela, text="Ver Pontuações", font=("Arial", 11), bg="#6666cc", fg="white", command=mostrar_pontuacoes_popup, width=15)
botao_pontuacoes.pack(pady=5)

status_label = Label(janela, textvariable=status_var, font=("Arial", 12))
status_label.pack(pady=5)

erros_label = Label(janela, textvariable=erros_var, font=("Arial", 12))
erros_label.pack()

letras_label = Label(janela, textvariable=letras_var, font=("Arial", 12))
letras_label.pack(pady=5)

pontos_label = Label(janela, textvariable=pontos_var, font=("Arial", 12))
pontos_label.pack(pady=5)

botao_tema = Button(janela, text="Alternar Tema", font=("Arial", 10), command=alternar_tema)
botao_tema.pack(pady=15)

aplicar_tema()
status_var.set("Digite seu nome e clique em Iniciar Jogo.")


janela.mainloop()