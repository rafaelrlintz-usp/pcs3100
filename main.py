import pygame
import sys
import queue
from gpiozero import Button, LED, PWMOutputDevice, LEDCharDisplay

# Inicialização do pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visual Novel - Emoções")
clock = pygame.time.Clock()

# Cores e fontes
BLACK = (0, 0, 0)
DIALOG_BG = (240, 240, 240)
BACKGROUND_CORES = {
    "praia": (135, 206, 235),      # azul claro
    "floresta": (34, 139, 34)      # verde escuro
}
font_texto = pygame.font.SysFont("arial", 28)
font_nome = pygame.font.SysFont("arial", 24, bold=True)

# Emoções e GPIOs
emocoes = {
    "alegria": Button(12),
    "tristeza": Button(13),
    "raiva": Button(14),
    "medo": Button(15),
    "surpresa": Button(16)
}
avancar = Button(17)
led_verde = LED(9)
led_vermelho = LED(10)
buzzer = PWMOutputDevice(11)

# Display de 7 segmentos
# Segmentos: A, B, C, D, E, F, G
display = LEDCharDisplay(2, 3, 4, 5, 6, 7, 8)

current_background = "praia"

class Personagem:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

personagens = {
    "Ana": Personagem("Ana", (255, 120, 120)),
    "Léo": Personagem("Léo", (120, 150, 255))
}

# Caixa de diálogo
def mostrar_dialogo(nome, frase):
    pygame.draw.rect(screen, DIALOG_BG, (40, HEIGHT - 140, WIDTH - 80, 100), border_radius=8)
    pygame.draw.rect(screen, BLACK, (40, HEIGHT - 140, WIDTH - 80, 100), 2, border_radius=8)
    if nome in personagens:
        p = personagens[nome]
        nome_render = font_nome.render(p.nome, True, p.cor)
        screen.blit(nome_render, (60, HEIGHT - 130))
    texto_render = font_texto.render(frase, True, BLACK)
    screen.blit(texto_render, (60, HEIGHT - 90))

def mudar_background(bg):
    global current_background
    if bg in BACKGROUND_CORES:
        current_background = bg

def mostrar_fala(nome, texto):
    screen.fill(BACKGROUND_CORES[current_background])
    mostrar_dialogo(nome, texto)
    pygame.display.flip()

# Controle de fluxo
etapa = 0
esperando_emocao = False
emocao_correta = None
acertos = 0
comandos_pendentes = queue.Queue()

def avancar_fala():
    global etapa, esperando_emocao, emocao_correta

    if etapa == 0:
        mostrar_fala("Ana", "Ei! Que bom te ver por aqui.")
        etapa += 1

    elif etapa == 1:
        mostrar_fala("?", "Qual emoção foi expressa?")
        emocao_correta = "alegria"
        esperando_emocao = True

    elif etapa == 2:
        mostrar_fala("Léo", "Vem comigo, vou te mostrar um lugar especial.")
        etapa += 1

    elif etapa == 3:
        mudar_background("floresta")
        mostrar_fala("?", "Qual emoção foi expressa?")
        emocao_correta = "surpresa"
        esperando_emocao = True

    elif etapa == 4:
        mostrar_fala("Ana", "Vamos trocar o cenário. Prepare-se!")
        etapa += 1

    elif etapa == 5:
        mostrar_fala("Léo", "Chegamos. Olha só essa floresta!")
        etapa += 1

    elif etapa == 6:
        mostrar_fala("?", f"Fim da história. Você acertou {acertos}.")
        display.value = str(acertos)[-1]  # Exibe 0-9 no display
        etapa += 1

def apito(frequencia, duracao_ms):
    buzzer.frequency = frequencia
    buzzer.value = 0.5
    pygame.time.wait(duracao_ms)
    buzzer.off()

def melodia_acerto():
    notas = [880, 1046, 1318]  # Lá, Dó, Mi (agudo)
    duracoes = [200, 200, 600]  # total = 1 segundo
    for f, d in zip(notas, duracoes):
        buzzer.frequency = f
        buzzer.value = 0.5
        pygame.time.wait(d)
        buzzer.off()
        pygame.time.wait(50)  # pequena pausa entre as notas

def processar_emocao(resposta):
    global esperando_emocao, etapa, acertos
    if esperando_emocao:
        if resposta == emocao_correta:
            print("Acertou!")
            acertos += 1
            led_verde.on()
            melodia_acerto()
            led_verde.off()
        else:
            print("Errou!")
            led_vermelho.on()
            apito(200, 500)   # apito grave
            led_vermelho.off()

        esperando_emocao = False
        etapa += 1
        avancar_fala()

# Liga botões físicos às emoções usando fila
for nome, botao in emocoes.items():
    botao.when_pressed = lambda n=nome: comandos_pendentes.put(n)

# Botão de avançar
avancar.when_pressed = lambda: comandos_pendentes.put("avancar")

# Início
avancar_fala()

# Loop principal
rodando = True
while rodando:
    clock.tick(60)

    # Processa comandos da fila
    while not comandos_pendentes.empty():
        resposta = comandos_pendentes.get()
        if resposta == "avancar" and not esperando_emocao:
            avancar_fala()
        elif resposta in emocoes:
            processar_emocao(resposta)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

pygame.quit()
sys.exit()
