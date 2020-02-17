from IA import *
from os import system
from random import randint
from time import sleep
from DefinindoGanhador import GanhouMaster

class JogoDaVelha:
    #Variaveis Vetorias
    Jogadas_Ganhas    = [
        [0,1,0,-1,1,0,1,-1,0],
        [0,0,0,1,1,-1,0,-1,1],
        [1,0,1,0,0,1,1,0,-1],
    ]
    Jogadas_Empatadas = [
        [1,0,0,0,1,1,0,1,0],
        [0,1,1,1,0,0,0,0,1],
        [0,0,1,1,1,0,0,1,0]
    ]
    #Variaveis de inicialização
    Acabou = False
    #Mapa do jogo
    Mapa = None
    
    #IA do jogo
    _IA = None

    def __init__(self):
        self.Mapa = list( '-' for x in range(9) )
        self._IA = IA_jogo(self.Mapa, 1, self.Jogadas_Ganhas, [], self.Jogadas_Empatadas)
        for h in range(100):
            self.Jogadas_Ganhas.append(list( randint(-1, 1) for x in range(9) ))
            
    #Apresentação do Mapa
    def mostrar(self):
        n = 0
        for i in range( len(self.Mapa) ):
            if n % 3 == 0: print("\n")
            n = n + 1        
            print(self.Mapa[i] + '\t|\t', end='')

    def resetarMapa(self):
        self.Mapa = list( '-' for x in range(9) )
    def resetarIA(self):
        self._IA = IA_jogo(self.Mapa, 1, self.Jogadas_Ganhas, [], self.Jogadas_Empatadas)

    def Conversor_Mapa( self ):
        Mapa_Computacional = list( '-' for x in range(9) )
        for i in range( len(self.Mapa) ):
            if self.Mapa[i] == 'x':
                Mapa_Computacional[i] = 0
            
            elif self.Mapa[i] == 'o':
                Mapa_Computacional[i] = 1

            else:
                Mapa_Computacional[i] = -1
        
        return Mapa_Computacional

    def play(self):
        while(not self.Acabou):
            system("cls")
            print(self.Jogadas_Ganhas)
            self.mostrar()    
            print("\nDigite uma posição de 1 a 9 : ", end='')
            n = int(input())
            self.Mapa[n-1] = 'x'

            self._IA.jogadaIA(self.Mapa)

            print(GanhouMaster(self.Mapa))
            if GanhouMaster(self.Mapa) == -1:
                print("Ninguem Ganhou")        
            elif GanhouMaster(self.Mapa) == 0:
                print("x Ganhou")                
                self.Jogadas_Ganhas.append(self.Conversor_Mapa())                
                sleep(10)
                self.resetarMapa()
                self.resetarIA()
            elif GanhouMaster(self.Mapa) == 1:
                print("o Ganhou")
                sleep(10)
                self.resetarMapa()
                self.resetarIA()

            sleep(1)
    
jogo = JogoDaVelha()
jogo.play()