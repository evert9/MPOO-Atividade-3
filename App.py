import pygame
import sys
from Gerador import Gerador

pygame.init()

larguraTela = 1000
alturaTela = 600
tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption("Click Formas")

preto = (0, 0, 0)
branco = (255, 255, 255)
cores = [(128, 0, 128), (255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)]

pygame.font.init()
fonte = pygame.font.SysFont(None, 36)

def desenhaTexto(texto, posicao):
    imagemTexto = fonte.render(texto, True, branco)
    tela.blit(imagemTexto, posicao)

gerador = Gerador(tela, larguraTela, alturaTela, cores)
gerador.gerarFormas(5)

clock = pygame.time.Clock()
texto = None

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            posMouse = pygame.mouse.get_pos()
            formaClicada = gerador.verificaClique(posMouse)
            if formaClicada:
                texto = f"Clique em um {formaClicada.tipo}! Posição: {posMouse}, Área: {round(formaClicada.area(), 2)}"
            else:
                texto = f"Clique fora das formas na posição: {posMouse}"

    tela.fill(preto)
    gerador.moverFormas()
    gerador.desenharFormas()

    if texto:
        desenhaTexto(texto, (50, 50))

    pygame.display.flip()
    clock.tick(60)
