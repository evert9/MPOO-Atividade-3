import pygame

class Forma:
    def __init__(self, tipo, cor, posicao, dimensao, velocidade):
        self.tipo = tipo
        self.cor = cor
        self.posicao = list(posicao)
        self.dimensao = dimensao
        self.velocidade = velocidade

    def desenhar(self, tela):
        if self.tipo == "quadrado" or self.tipo == "retangulo":
            pygame.draw.rect(tela, self.cor, (*self.posicao, *self.dimensao))
        elif self.tipo == "circulo":
            pygame.draw.circle(tela, self.cor, self.posicao, self.dimensao[0])
        elif self.tipo == "triangulo":
            pygame.draw.polygon(tela, self.cor,
                [self.posicao, (self.posicao[0] + self.dimensao[0], self.posicao[1]),
                (self.posicao[0] + self.dimensao[0] // 2, self.posicao[1] - self.dimensao[1])
            ])

    def area(self):
        if self.tipo == "quadrado" or self.tipo == "retangulo":
            return self.dimensao[0] * self.dimensao[1]
        elif self.tipo == "circulo":
            return 3.14 * (self.dimensao[0] ** 2)
        elif self.tipo == "triangulo":
            return (self.dimensao[0] * self.dimensao[1]) / 2

    def verificaClique(self, pos_mouse):
        if self.tipo == "quadrado" or self.tipo == "retangulo":
            return (self.posicao[0] <= pos_mouse[0] <= self.posicao[0] + self.dimensao[0] and
                    self.posicao[1] <= pos_mouse[1] <= self.posicao[1] + self.dimensao[1])
        elif self.tipo == "circulo":
            distancia = ((pos_mouse[0] - self.posicao[0]) ** 2 + (pos_mouse[1] - self.posicao[1]) ** 2) ** 0.5
            return distancia <= self.dimensao[0]
        elif self.tipo == "triangulo":
            x, y = pos_mouse
            bx, by = self.posicao
            return bx <= x <= bx + self.dimensao[0] and by >= y >= by - self.dimensao[1]

    def mover(self, larguraTela, alturaTela):
        self.posicao[0] += self.velocidade[0]
        self.posicao[1] += self.velocidade[1]

        if self.tipo == "circulo":
            if self.posicao[0] - self.dimensao[0] <= 0 or self.posicao[0] + self.dimensao[0] >= larguraTela:
                self.velocidade[0] *= -1
            if self.posicao[1] - self.dimensao[0] <= 0 or self.posicao[1] + self.dimensao[0] >= alturaTela:
                self.velocidade[1] *= -1
        else:
            if self.posicao[0] <= 0 or self.posicao[0] + self.dimensao[0] >= larguraTela:
                self.velocidade[0] *= -1
            if self.posicao[1] <= 0 or self.posicao[1] + self.dimensao[1] >= alturaTela:
                self.velocidade[1] *= -1
