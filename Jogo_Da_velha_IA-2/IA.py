from BaseDeDados import Base
from random import randint
class Jogo_IA:

    Mapa = None
    Melhor_Jogada = [0, 0]
    BD = None
    Banco_de_Jogadas = None
    Pontos = 0
    Jogadas_Aprendidas = None

    def __init__(self, MP):
        
        self.Mapa = MP
        self.BD = Base()
        self.Banco_de_Jogadas = self.BD.getBanco_de_Jogadas()
        self.Jogadas_Aprendidas = len(self.Banco_de_Jogadas)

    def adicionarJogada(self, MP):
        self.BD.addJogada(MP)
        self.Banco_de_Jogadas = self.BD.getBanco_de_Jogadas()
        self.Jogadas_Aprendidas = len(self.Banco_de_Jogadas)
        self.Pontos = self.Pontos + 1
    

    def Analise_Vetorial(self, MP, player):
        self.Mapa = MP

        for k in range( len(self.BD.getBanco_de_Jogadas()) ):
            n = 0
            for i in range(3):
                for j in range(3):
                    if self.Banco_de_Jogadas[k][i][j] == self.Mapa[i][j] and self.Mapa[i][j] == player:
                        n = n + 1
                        if self.Melhor_Jogada[1] < n:
                            self.Melhor_Jogada = [k, n]
        Nao_encontrada = False
        for i in range(3):
            for j in range(3):
                if self.Banco_de_Jogadas[k][i][j] == player and self.Mapa[i][j] == -1:
                    self.Mapa[i][j] = player
                    Nao_encontrada = True
                    return self.Mapa
        
        if not Nao_encontrada:
            caso = False
            while(not caso):
                n = [randint(0, 2), randint(0, 2)]
                if self.Mapa[n[0]][n[1]] == -1:
                    self.Mapa[n[0]][n[1]] = player
                    caso = True

        return self.Mapa
