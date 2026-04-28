import pygame
pygame.mixer.init()
pygame.mixer.music.load("stand_by_me.mp3")
pygame.mixer.music.play()
from rich.console import Console
import time
import os

console = Console()

def typewriter(lines, default_char_delay=0.08, default_line_delay=0.5):
    for line in lines:
        if isinstance(line, list):  
            line_delay = default_line_delay

            for segment in line:
                if len(segment) == 2:
                    text, color = segment
                    char_delay = default_char_delay

                elif len(segment) == 3:
                    text, color, char_delay = segment

                else:
                    raise ValueError("Segmento inválido")

                for ch in text:
                    console.print(ch, style=color, end="")
                    if console.file:
                        console.file.flush()
                    time.sleep(char_delay)

            console.print()

            if isinstance(line_delay, (int, float)):
                time.sleep(line_delay)
            else:
                time.sleep(default_line_delay)

        else:  
            if len(line) != 4:
                raise ValueError("Linha inválida, precisa de 4 valores")

            text, char_delay, line_delay, color = line

            for ch in text:
                console.print(ch, style=color, end="")
                if console.file:
                    console.file.flush()
                time.sleep(char_delay)

            console.print()

            if isinstance(line_delay, (int, float)):
                time.sleep(line_delay)
            else:
                time.sleep(default_line_delay)

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    linhas = [
        # 🎸 INTRODUÇÃO
        ("", 0.01, 15.9, "#000000"),

        # 🌙 Início 
        [
            ("When the ", "#6CA6CD", 0.04),
            ("night", "bold #1E90FF", 0.35),
            (" has come", "#6CA6CD", 0.06),
        ],

        # Pausa longa instrumental
        ("", 0.01, 2.0, "#000000"),
        
        [
            ("And the land is ", "#87CEFA", 0.05),
            ("dark", "bold #4682B4", 0.16),
        ],

        # ⏳ PAUSA REDUZIDA PARA ALCANÇAR A MÚSICA (De 3.5 para 2.5)
        ("", 0.01, 1.4, "#000000"),

        # 🌕 (0:25) - Digitação mais rápida no começo da frase
        [
            ("And the moon ", "#E4E4E4", 0.03), # Velocidade acelerada!
            ("is the only ", "#E4E4E4", 0.03),  # Velocidade acelerada!
            ("light", "bold #FFFFFF", 0.13),
            (" we'll see", "#E4E4E4", 0.05),
        ],

        # Pausa antes da mudança de tom (Reduzida de 4.0 para 3.0)
        ("", 0.01, 3.0, "#000000"),

        # 💪 Confiança 
        [
            ("No, I won't ", "#FFD700", 0.04),
            ("be afraid", "bold #FFA500", 0.10),
        ],

        # Pausa instrumental (Reduzida para manter o ritmo)
        ("", 0.01, 2.8, "#000000"),

        [
            ("Oh, I won't ", "#FFD700", 0.04),
            ("be afraid", "bold #FFA500", 0.10),
        ],

        # Pausa menor
        ("", 0.01, 2.5, "#000000"),

        # ❤️ Emoção 
        [
            ("Just as long ", "#DA70D6", 0.04),
            ("as you stand", "bold #FF69B4", 0.06),
            (", stand by me", "#FF1493", 0.08),
        ],

        # Preparação pro refrão
        ("", 0.01, 1.5, "#000000"),

        # 🔥 Refrão 
        [
            ("So darlin', darlin', ", "#FF69B4", 0.05),
            ("stand ", "bold #FF0000", 0.10),
            ("by me", "bold #FF0000", 0.08),
        ],

        # Pausa curta 
        ("", 0.01, 1.0, "#000000"),

        [
            ("Oh, ", "#FFFFFF", 0.05),
            ("stand ", "bold #FF0000", 0.10),
            ("by me", "bold #FF0000", 0.08),
        ],

        # Pausa curta 
        ("", 0.01, 1.0, "#000000"),

        [
            ("Oh, ", "#FFFFFF", 0.06),
            ("stand...", "italic #AAAAAA", 0.14),
        ],

        # Pausa de batida 
        ("", 0.01, 0.6, "#000000"),

        # 💥 Impacto 
        [
            ("STAND BY ME", "bold #FF0000", 0.09),
        ],

        # Pausa de batida 
        ("", 0.01, 0.6, "#000000"),

        [
            ("stand by me", "bold #FF4C4C", 0.09),
        ],

        # Pausa dramática para a surpresa final 
        ("", 0.01, 2.5, "#000000"),

        # 💌 Mensagem final
        [
            ("this part made me think of ", "#CCCCCC", 0.06),
            ("you", "bold #FF69B4", 0.20), 
        ],
    ]

    typewriter(linhas)