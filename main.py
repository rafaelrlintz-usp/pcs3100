# main.py
import pygame
import sys
import os

# Inicialização
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minha Visual Novel")
clock = pygame.time.Clock()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DIALOG_BG = (240, 240, 240)
FLORESTA_COR = (34, 139, 34)  # verde
PRAIA_COR = (238, 214, 175)   # areia clara

# Fontes
font_texto = pygame.font.SysFont("arial", 28)
font_nome = pygame.font.SysFont("arial", 24, bold=True)

# Cria superfícies sólidas para os fundos
backgrounds = {
    "praia": pygame.Surface((WIDTH, HEIGHT)),
    "floresta": pygame.Surface((WIDTH, HEIGHT)),
    "cidade": pygame.Surface((WIDTH, HEIGHT)),
    "noite": pygame.Surface((WIDTH, HEIGHT)),
    "montanha": pygame.Surface((WIDTH, HEIGHT))
}
backgrounds["praia"].fill(PRAIA_COR)
backgrounds["floresta"].fill(FLORESTA_COR)
backgrounds["cidade"].fill((200, 200, 255))  # azul acinzentado
backgrounds["noite"].fill((20, 20, 60))       # azul escuro
backgrounds["montanha"].fill((160, 160, 160)) # cinza claro

current_background = "praia"

# Função para fazer fade entre fundos com fundo negro entre transições (sem escurecer o fundo inicial)
def fade_para(novo_background, nova_fala=None):
    global current_background, fala_em_andamento
    black_surface = pygame.Surface((WIDTH, HEIGHT))
    black_surface.fill((0, 0, 0))

    # Fade out atual
    for alpha in range(0, 255, 15):
        screen.blit(backgrounds[current_background], (0, 0))
        ident, fala = fala_em_andamento
        if fala:
            mostrar_dialogo(ident, fala)
        black_surface.set_alpha(alpha)
        screen.blit(black_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(30)

    # Quando tela está escura, troca o fundo e limpa fala
    current_background = novo_background
    fala_em_andamento = nova_fala if nova_fala else (None, "")

    # Exibe fundo novo com fade in
    for alpha in range(255, -1, -15):
        screen.blit(backgrounds[current_background], (0, 0))
        ident, fala = fala_em_andamento
        if fala:
            mostrar_dialogo(ident, fala)
        black_surface.set_alpha(alpha)
        screen.blit(black_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(30)

# Personagens com identificadores
class Personagem:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

personagens = {
    "a": Personagem("Ana", (255, 120, 120)),
    "l": Personagem("Léo", (120, 150, 255)),
    "c": Personagem("Clara", (200, 100, 255)),
    "m": Personagem("Miguel", (255, 200, 100)),
    "v": Personagem("Valentina", (100, 200, 150))
}

# Caixa de diálogo
def mostrar_dialogo(ident, frase):
    pygame.draw.rect(screen, DIALOG_BG, (40, HEIGHT - 140, WIDTH - 80, 100), border_radius=8)
    pygame.draw.rect(screen, BLACK, (40, HEIGHT - 140, WIDTH - 80, 100), 2, border_radius=8)
    if ident in personagens:
        p = personagens[ident]
        nome_render = font_nome.render(p.nome, True, p.cor)
        screen.blit(nome_render, (60, HEIGHT - 130))
    texto_render = font_texto.render(frase, True, BLACK)
    screen.blit(texto_render, (60, HEIGHT - 90))

# Carrega o roteiro de um arquivo externo
with open(os.path.join("assets", "roteiro.txt"), encoding="utf-8") as f:
    roteiro = []
    for linha in f:
        linha = linha.strip()
        if not linha or linha.startswith("#"):
            continue
        if linha.startswith("personagem"):
            _, pid, nome, rgb = linha.split(None, 3)
            r, g, b = map(int, rgb.split(","))
            personagens[pid] = Personagem(nome, (r, g, b))
        elif linha.startswith("background"):
            _, bid, rgb = linha.split(None, 2)
            r, g, b = map(int, rgb.split(","))
            surf = pygame.Surface((WIDTH, HEIGHT))
            surf.fill((r, g, b))
            backgrounds[bid] = surf
        else:
            roteiro.append(linha)

index = 0
fala_em_andamento = (None, "")

# Processador de ações
def executar_linha(linha):
    global current_background, fala_em_andamento, index
    if linha.startswith("scene"):
        partes = linha.split()
        nome = partes[1]
        fade = partes[2].lower() == "true"
        # Captura a próxima fala (se houver)
        proxima_fala = None
        if index + 1 < len(roteiro):
            proxima = roteiro[index + 1]
            if not proxima.startswith("scene"):
                ident, texto = proxima.split(" ", 1)
                proxima_fala = (ident, texto.strip().strip('"'))

        if nome in backgrounds:
            if fade:
                fade_para(nome, proxima_fala)
            else:
                current_background = nome
                fala_em_andamento = proxima_fala if proxima_fala else (None, "")

        index += 1
    else:
        ident, fala = linha.split(" ", 1)
        fala = fala.strip().strip('"')
        fala_em_andamento = (ident, fala)

# Loop principal
rodando = True
executar_linha(roteiro[index])
while rodando:
    clock.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            index += 1
            if index < len(roteiro):
                executar_linha(roteiro[index])
            else:
                index = len(roteiro) - 1

    screen.blit(backgrounds[current_background], (0, 0))
    ident, fala = fala_em_andamento
    if fala:
        mostrar_dialogo(ident, fala)
    pygame.display.flip()

pygame.quit()
sys.exit()
