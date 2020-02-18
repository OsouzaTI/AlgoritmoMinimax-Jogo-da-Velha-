import pygame
from time import sleep
from random import randint
from Tabuleiro import Tabuleiro
from DefinindoGanhador import Ganhador_Jogo
import sys


class GUI_tabela:

    telaMaster = None
    icon = None    
    ColorBG = None
    tamanhoQuadrado = 150
    Pos = None
    #0 = 'X', 1 = 'O'
    HUplayer = 1
    IAplayer = 0
    _HU = None
    _IA = None
    Assets = None
    Conjunto = None

    #Pontuação
    HUpontos        = 0
    IApontos        = 0
    Empates         = 0
    PartidasJogadas = 0
    #Tabuleiro
    Game_State = [-1, -1, -1,
                  -1, -1, -1,
                  -1, -1, -1]
    Alternada = True
    #IA
    IA = None
    TempoDeExecucao    = 0
    ChamadasRecursivas = 0
    #IA_FirstMove = 0
    #Font
    MinhaFonte = []
    Info = []
    InfoEspecial = []
    Textos = [
        ("IA pontos       : %d"%(IApontos)),
        ("HU pontos       : %d"%(HUpontos)),
        ("Empates         : %d"%(Empates)),
        ("Partidas Jogadas: %d"%(PartidasJogadas))
    ]
    TextoEspecial = [
        ("Tempo de Processamento : %.4fms"%(TempoDeExecucao)),
        ("Chamadas Recursivas    : %d"%(ChamadasRecursivas)),
    ]
    #Ganhador
    GD = None

    def __init__(self):
        #inicializando o pygame
        pygame.init()
        pygame.font.init()
        self.MinhaFonte = [
            pygame.font.SysFont('Arial', 38),
            pygame.font.SysFont('Arial', 26),
        ]
        #Iniciar Inteligência artificial
        self._HU = 'X' if self.HUplayer == 0 else 'O'
        self._IA = 'X' if self.IAplayer == 0 else 'O'
        self.IA = Tabuleiro(self.Game_State, self._HU, self._IA)

        #Iniciando Ganhador
        self.GD = Ganhador_Jogo()

        self.telaMaster = pygame.display.set_mode((900, 600))
        pygame.display.set_caption("Jogo da Velha")
        self.icon = pygame.image.load("business-and-finance.png")
        pygame.display.set_icon(self.icon)

        self.ColorBG = (255, 255, 255)
        self.telaMaster.fill( self.ColorBG )


        self.Assets = [
                ["cross1.png","circle1.png"]
            ]
        
        self.Conjunto = [pygame.image.load(self.Assets[0][0]),
                    pygame.image.load(self.Assets[0][1])]
        
    def RandomColor(self, r):

        red   = randint(0, 255)
        green = randint(0, 255)
        blue  = randint(0, 255)

        if not r:
            return (red, green, blue)
        else:
            return (80, 104, 118)

    def desenharTabela(self, tamanhoQuadrado, padd):
        x = 0 + padd
        y = 0 + padd
        Pares = []
        index = 0
        for i in range(9):
            if i % 3 == 0 and i != 0:
                x = 0 + padd
                y = y + tamanhoQuadrado
            else:
                if i != 0:
                    x = x + tamanhoQuadrado
                
            pygame.draw.rect(self.telaMaster
                            ,self.RandomColor(True),
                             (x, y, tamanhoQuadrado, tamanhoQuadrado))
            Pares.append(
                [
                    (x + tamanhoQuadrado, y),
                    (x + tamanhoQuadrado, y + tamanhoQuadrado),
                    (x , y + tamanhoQuadrado),
                    (x + tamanhoQuadrado, y + tamanhoQuadrado), 
                ])
        self.Pos = Pares
        for p in Pares:
            index = index + 1
            #print(index)
            if index != 3:
                pygame.draw.line(self.telaMaster, (255, 0, 0), p[0], p[1])
                pygame.display.flip()
            else:
                index = 0
            
            pygame.draw.line(self.telaMaster, (255, 0, 0), p[2], p[3])
            pygame.display.flip()
            
        pygame.display.update()

        
        
    def clique(self):
        Clicou = False
        while not Clicou:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    Run = False
                    print("Game Finalizado!")
                    sys.exit(0)
     
                elif e.type == pygame.MOUSEBUTTONUP:
                    print(pygame.mouse.get_pos())
                    m = list(pygame.mouse.get_pos())
                    index = 0                
                    for p in self.Pos:
                        #print(p)
                        if m[0] < p[0][0] and \
                        m[1] < p[2][1] and \
                        m[0] > p[0][0] - self.tamanhoQuadrado and \
                        m[1] > p[2][1] - self.tamanhoQuadrado:
                                                        
                            #print(index)
                            break
                        
                        index = index + 1
                    
                    try:
                        self.Game_State[index] = 'X' if self.HUplayer == 0 else 'O'
                        Clicou = True
                    except IndexError:
                        return self.clique()

                    
                           

    def Mostrar(self):
        
        for t in self.Textos:
            self.Info.append(self.MinhaFonte[0].render(t, False, (0, 0, 0)))

        for te in self.TextoEspecial:
            self.InfoEspecial.append(self.MinhaFonte[1].render(te, False, (0, 0, 0)))

        k = 0
        for i in range(len(self.Info)):
            self.telaMaster.blit(self.Info[i], (550, 100 + k) )
            k = k + 50
        
        k = 0    
        for j in range(len(self.InfoEspecial)):
            self.telaMaster.blit(self.InfoEspecial[j], (100 + (k * 100), 10) )
            k = k + 4

        self.Info.clear()
        self.InfoEspecial.clear()
        for i in range(9):

            if self.Game_State[i] == 'O':

                Xmin = self.Pos[i][0][0] - (self.tamanhoQuadrado - self.tamanhoQuadrado / 6)
                Ymin = self.Pos[i][2][1] - (self.tamanhoQuadrado - self.tamanhoQuadrado / 6)                                
                self.telaMaster.blit(self.Conjunto[1],(Xmin,Ymin))
                
            elif self.Game_State[i] == 'X':

                
                Xmin = self.Pos[i][0][0] - (self.tamanhoQuadrado - self.tamanhoQuadrado / 6)
                Ymin = self.Pos[i][2][1] - (self.tamanhoQuadrado - self.tamanhoQuadrado / 6)                                
                self.telaMaster.blit(self.Conjunto[0],(Xmin,Ymin))
        
        pygame.display.update()

    def resetarTabuleiro(self):
        self.Mostrar()
        sleep(4)
        self.PartidasJogadas = self.PartidasJogadas + 1
        self.Game_State = [
                    -1, -1, -1,
                    -1, -1, -1,
                    -1, -1, -1                  
                ]
        
        self.Textos = [
            ("IA pontos       : %d"%(self.IApontos)),
            ("HU pontos       : %d"%(self.HUpontos)),
            ("Empates         : %d"%(self.Empates)),
            ("Partidas Jogadas: %d"%(self.PartidasJogadas))
        ]

    def playerIA(self):
        self.IA.setGame_State(self.Game_State)
        #print(self.Game_State) 
        MelhorJogada = self.IA.playerIA()
        print("MJ: "+ str(MelhorJogada))
        self.Game_State[MelhorJogada[0]] = 'X' if self.IAplayer == 0 else 'O'  
        
        self.ChamadasRecursivas = MelhorJogada[1]
        self.TempoDeExecucao = MelhorJogada[2]
        
        self.TextoEspecial = [
            ("Tempo de Processamento : %.4fms"%(self.TempoDeExecucao)),
            ("Chamadas Recursivas    : %d"%(self.ChamadasRecursivas)),
        ]
        
                        
    def iniciarJogo(self, Alternada):
        self.telaMaster.fill( self.ColorBG )
        self.desenharTabela(self.tamanhoQuadrado, 50)

        self.Mostrar()
        
        if Alternada:
            self.clique()
        else:
            self.playerIA()
        
        if self.GD.DefinindoGanhador(self.Game_State, self._IA):
            self.IApontos = self.IApontos + 1
            self.resetarTabuleiro()
            return self.iniciarJogo(True)
        elif self.GD.DefinindoGanhador(self.Game_State, self._HU):
            self.HUpontos = self.HUpontos + 1
            self.resetarTabuleiro()
            return self.iniciarJogo(True)
        elif len( self.IA.mapa_vazios(self.Game_State) ) == 0:
            self.Empates = self.Empates + 1
            self.resetarTabuleiro()
            return self.iniciarJogo(True)
                
        return self.iniciarJogo(not Alternada)

j = GUI_tabela()
j.iniciarJogo(True)


























        
