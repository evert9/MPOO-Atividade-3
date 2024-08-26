import random
from Forma import Forma

class Gerador:
    def __init__(self, tela, larguraTela, alturaTela, cores):
        self.tela = tela
        self.larguraTela = larguraTela
        self.alturaTela = alturaTela
        self.cores = cores
        self.formas = []

    def gerarFormas(self, quantidade):
        for _ in range(quantidade): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
            tipo = random.choice(["quadrado", "circulo", "retangulo", "triangulo"])
            cor = random.choice(self.cores)
            velocidade = [random.choice([-2, -1, 1, 2]), random.choice([-2, -1, 1, 2])]  # Velocidade inicial aleatória

            if tipo == "circulo":
                raio = random.randint(20, 50)
                posicao = (
                    random.randint(raio, self.larguraTela - raio),
                    random.randint(raio, self.alturaTela - raio)
                )
                dimensao = (raio,)
            elif tipo == "quadrado":
                lado = random.randint(50, 100)
                posicao = (
                    random.randint(0, self.larguraTela - lado),
                    random.randint(0, self.alturaTela - lado)
                )
                dimensao = (lado, lado)
            elif tipo == "retangulo":
                largura = random.randint(50, 150)
                altura = random.randint(30, 100)
                posicao = (
                    random.randint(0, self.larguraTela - largura),
                    random.randint(0, self.alturaTela - altura)
                )
                dimensao = (largura, altura)
            elif tipo == "triangulo":
                base = random.randint(50, 100)
                altura = random.randint(50, 100)
                posicao = (
                    random.randint(0, self.larguraTela - base),
                    random.randint(altura, self.alturaTela)
                )
                dimensao = (base, altura)

            novaForma = Forma(tipo, cor, posicao, dimensao, velocidade)
            self.formas.append(novaForma)

    def desenharFormas(self):
        for forma in self.formas:
            forma.desenhar(self.tela)

    def moverFormas(self):
        for forma in self.formas:
            forma.mover(self.larguraTela, self.alturaTela)

    def verificaClique(self, posMouse):
        for forma in self.formas:
            if forma.verificaClique(posMouse):
                return forma
        return None
