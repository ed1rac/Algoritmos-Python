import tkinter as tk
from tkinter import messagebox


class JogoDaVelha:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jogo da Velha")

        self.jogador_atual = 'X'
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.botoes = []

        self.criar_interface()
        self.root.mainloop()

    def criar_interface(self):
        # Cria os botões e organiza-os em um grid
        tamanho_largura = 12
        cor_fundo_botao = "lightblue"
        cor_fonte_botao = "black"
        for i in range(3):
            linha_botoes = []
            for j in range(3):
                botao = tk.Button(self.root, text=" ", font=("Helvetica", tamanho_largura), width=tamanho_largura, height=tamanho_largura//2,
                                  command=lambda row=i, col=j: self.clicar_botao(row, col), bg=cor_fundo_botao, fg=cor_fonte_botao)
                botao.grid(row=i, column=j)
                linha_botoes.append(botao)
            self.botoes.append(linha_botoes)
        # Botão para reiniciar o jogo
        botao_reiniciar = tk.Button(self.root, text="Reiniciar", command=self.reiniciar_jogo)
        botao_reiniciar.grid(row=3, column=0, columnspan=3)

    def reiniciar_jogo(self):
        # Limpa o tabuleiro
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

        # Limpa os botões
        for linha in self.botoes:
            for botao in linha:
                botao.config(text=" ")

        # Reinicia o jogador atual
        self.jogador_atual = 'X'

        # Mostra uma mensagem de reinício (opcional)
        messagebox.showinfo("Novo Jogo", "Um novo jogo começou!")
    def clicar_botao(self, row, col):
        if self.tabuleiro[row][col] == ' ':
            self.tabuleiro[row][col] = self.jogador_atual
            self.botoes[row][col].config(text=self.jogador_atual)

            if self.verificar_vitoria():
                self.mostrar_mensagem_vitoria()
            elif self.verificar_empate():
                self.mostrar_mensagem_empate()
            else:
                self.alternar_jogador()

    # ... outras funções para verificar vitória, empate, etc.

    def verificar_vitoria(self):
        # Verifica linhas
        for linha in self.tabuleiro:
            if all(celula == linha[0] and celula != ' ' for celula in linha):
                return True

        # Verifica colunas
        for col in range(3):
            if all(self.tabuleiro[linha][col] == self.tabuleiro[0][col] and self.tabuleiro[linha][col] != ' ' for linha
                   in range(3)):
                return True

        # Verifica diagonais
        if all(self.tabuleiro[i][i] == self.tabuleiro[0][0] and self.tabuleiro[i][i] != ' ' for i in range(3)) or \
                all(self.tabuleiro[i][2 - i] == self.tabuleiro[0][2] and self.tabuleiro[i][2 - i] != ' ' for i in
                    range(3)):
            return True

        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            for celula in linha:
                if celula == ' ':
                    return False
        return True

    def alternar_jogador(self):
        self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'

    def mostrar_mensagem_vitoria(self):
        messagebox.showinfo("Fim do Jogo", f"O jogador {self.jogador_atual} venceu!")

    def mostrar_mensagem_empate(self):
        messagebox.showinfo("Fim do Jogo", "Empate!")


if __name__ == "__main__":
    jogo = JogoDaVelha()
