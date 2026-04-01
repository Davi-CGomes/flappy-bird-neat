import pygame
import os

# Dimensões da tela
TELA_LARGURA = 570
TELA_ALTURA = 800

# Carregamento das imagens
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png'))),
]

# Fonte
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

# Configurações do pássaro
PASSARO_ROTACAO_MAXIMA = 25
PASSARO_VELOCIDADE_ROTACAO = 20
PASSARO_TEMPO_ANIMACAO = 5

# Configurações do cano
CANO_DISTANCIA = 200
CANO_VELOCIDADE = 5

# Configurações do chão
CHAO_VELOCIDADE = 5

# IA
AI_JOGANDO = True
