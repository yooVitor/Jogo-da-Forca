# 🎯 Jogo da Forca - Interface Gráfica em Python

Um jogo da forca interativo com interface gráfica desenvolvida em Python usando **Tkinter**. O jogador tenta adivinhar uma palavra secreta, com feedback visual, contagem de erros e sistema de pontuação persistente.
<video controls style="width: 100%; max-width: 100%; height: auto;"><source src="assets/Jogo da Forca.mp4" type="video/mp4"></video>

---

## 🖥️ Funcionalidades

- Interface gráfica intuitiva com **modo claro/escuro**
- Escolha de palavras aleatórias a partir de um arquivo externo (`palavras.txt`)
- Exibição da palavra oculta com letras reveladas corretamente
- Mensagens de feedback para tentativas válidas e inválidas
- Contagem de erros restantes
- Registro de **vitórias e derrotas** em um arquivo `pontuacoes.txt`
- Botão para visualizar pontuações anteriores
- Suporte a múltiplos jogadores (por nome)

---

## 📸 Capturas de Tela

### Tema Claro
![Tema Claro](assets/tema%20claro.png)

### Tema Escuro
![Tema Escuro](assets/tema%20escuro.png)

---

## 📂 Estrutura de Arquivos

- `jogo.py` — Código fonte principal do jogo
- `palavras.txt` — Arquivo de texto com a lista de palavras para o jogo
- `pontuacoes.txt` — Arquivo gerado automaticamente para armazenar pontuações

## 🚀 Como executar

1. Tenha o Python 3 instalado no seu sistema.
2. Certifique-se de que os arquivos `main.py` e `palavras.txt` estão na mesma pasta.

## 💡 Personalizações

- Modo escuro/claro: Clique em Alternar Tema

- Pontuações: São salvas automaticamente em pontuacoes.txt e podem ser visualizadas ao final do jogo ou com o botão `Ver Pontuações`

## 📦 Recursos Técnicos

- Linguagem: Python 3
- Interface gráfica: Tkinter
- Armazenamento local: arquivos .txt
- Organização em classes e funções modulares

## ✍️ Autor
Desenvolvido por:
Vitor Gomes e Raian Souza

## 📜 Observações

Este projeto foi desenvolvido como parte de um trabalho acadêmico para a disciplina de **Processamento de Dados** no curso de **Engenharia de Computação** / **Bacharelado em Ciência, Engenharia e Tecnologia (BCET)** da **UFRB – Universidade Federal do Recôncavo da Bahia**.

Seu uso é voltado para fins educacionais, podendo ser reutilizado ou adaptado com os devidos créditos.
