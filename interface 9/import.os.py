import os
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk

class InterfaceEstiloMyRobotLab(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interface Estilo MyRobotLab")
        self.geometry("1366x768")
        self.resizable(True, True)
        
        base = Path(__file__).resolve().parent
        file = base / "A_2D_digital_illustration_depicts_a_user_interface.png.png"

        bg_image = Image.open(file)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.label_image = tk.Label(self, image = self.bg_photo)
        self.label_image.pack(fill = tk.BOTH, expand = True)

        self.canvas = tk.Canvas(self, width=1152, height=768)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.bind("<Configure>", self.redimencionar_imagem)

        self.criar_botoes_icones()

    def redimencionar_imagem(self, event):
        nova_largura = event.width
        nova_altura = event.height

        imagem_redimencionada = self.image_original.resize((nova_largura, nova_altura), Image.ANTIALIAS)
        self_image_tk = ImageTk.PhotoImage(imagem_redimencionada)

        self.label_image.config(image = self.image_tk)

    def criar_botoes_icones(self):
        botoes_info = {
            "Cabeça do Robô": (498, 148),
            "Pescoço do Robô": (498, 200),
            "Tronco Superior do Robô": (498, 255),
            "Tronco Inferior do Robô": (498, 320),
            "Braço Esquerdo do Robô": (405, 250),
            "Braço Direito do Robô": (590, 250),
            "Antebraço Esquerdo do Robô": (340, 300),
            "Antebraço Direito do Robô": (655, 300),
            "Mão Esquerda do Robô": (305, 355),
            "Mão Direita do Robô": (690, 355),
            "Quadril do Robô": (498, 385),
            "Coxa Esquerda do Robô": (445, 450),
            "Coxa Direita do Robô": (550, 450),
            "Perna Esquerda do Robô": (445, 530),
            "Perna Direita do Robô": (550, 530),
            "Pé Esquerdo do Robô": (445, 590),
            "Pé Direito do Robô": (550, 590),
            "Ícone Perfil de Cabeça": (498, 75),
            "Ícone Mão": (620, 130),
            "Ícone Lâmpada": (680, 280),
            "Ícone Gráfico de Barras": (620, 430),
            "Ícone Pé/Sapato": (380, 430),
            "Ícone Microfone": (320, 280),
            "Ícone Porta/Entrada": (380, 130),
            "Ícone Interrogação": (320, 75),
            "Botão Iniciar Servos": (830, 130),
            "Botão Ajustar Configurações do Arduino": (830, 210)
        }
        for nome, (x, y) in botoes_info.items():
            btn = tk.Button(
                self.canvas,
                text=nome,
                command=lambda n=nome: self.abrir_detalhes_parte(n),
                bg="#004466", fg="white",
                activebackground="#00aaff", activeforeground="white",
                font=("Arial", 8, "bold"),
                cursor="hand2",
                relief="raised",
                bd=2
            )
            self.canvas.create_window(x, y, window=btn, width=140, height=25)

    def abrir_detalhes_parte(self, parte):
        janela = Toplevel(self)
        janela.title(f"Detalhes: {parte}")
        janela.geometry("300x400")

        partes_detalhadas = self.obter_subpartes(parte)
        for i, sub in enumerate(partes_detalhadas):
            btn = tk.Button(janela, text=sub, width=25,
                            command=lambda s=sub: self.executar_acao_subparte(parte, s))
            btn.pack(pady=5)

    def obter_subpartes(self, parte):
        detalhes = {
            "Cabeça do Robô": ["Olhos", "Boca", "Testa"],
            "Pescoço do Robô": ["Rotação", "Inclinação"],
            "Tronco Superior do Robô": ["Giro", "Inclinação frontal"],
            "Tronco Inferior do Robô": ["Inclinação lateral"],
            "Braço Esquerdo do Robô": ["Ombro", "Cotovelo"],
            "Braço Direito do Robô": ["Ombro", "Cotovelo"],
            "Antebraço Esquerdo do Robô": ["Rotação", "Flexão"],
            "Antebraço Direito do Robô": ["Rotação", "Flexão"],
            "Mão Esquerda do Robô": ["Polegar", "Indicador"],
            "Mão Direita do Robô": ["Polegar", "Indicador"],
            "Quadril do Robô": ["Rotação esquerda", "Rotação direita"],
            "Coxa Esquerda do Robô": ["Flexão", "Extensão"],
            "Coxa Direita do Robô": ["Flexão", "Extensão"],
            "Perna Esquerda do Robô": ["Joelho", "Rotação"],
            "Perna Direita do Robô": ["Joelho", "Rotação"],
            "Pé Esquerdo do Robô": ["Calcanhar", "Ponta"],
            "Pé Direito do Robô": ["Calcanhar", "Ponta"],
            "Botão Iniciar Servos": ["Todos os motores"],
            "Botão Ajustar Configurações do Arduino": ["Porta COM", "Baudrate"],
            "Ícone Perfil de Cabeça": ["Status Cognitivo"],
            "Ícone Mão": ["Gestos"],
            "Ícone Lâmpada": ["Ideias"],
            "Ícone Gráfico de Barras": ["Desempenho"],
            "Ícone Pé/Sapato": ["Movimento"],
            "Ícone Microfone": ["Reconhecimento de voz"],
            "Ícone Porta/Entrada": ["Entrada/Saída"],
            "Ícone Interrogação": ["Ajuda"]
        }
        return detalhes.get(parte, ["Sem detalhes disponíveis"])

    def executar_acao_subparte(self, parte, subparte):
        print(f"Ação: {parte} -> {subparte}")
        messagebox.showinfo("Comando", f"{parte} > {subparte} ativado!")

if __name__ == "__main__":
    app = InterfaceEstiloMyRobotLab()
    app.mainloop()
