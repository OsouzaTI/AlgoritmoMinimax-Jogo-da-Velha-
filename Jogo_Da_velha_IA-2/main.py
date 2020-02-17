from os import system
from IA import Jogo_IA
from DefinindoGanhador import Ganhador_Jogo
from time import sleep
from random import randint
class Main:
    Game_over = False
    Numero_de_Jogos = 0
    Ordem = [0, 1]
    game_state = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1]
    ]
    _IA  = []
    GJ = Ganhador_Jogo()

    def __init__(self):

        self._IA.append( Jogo_IA(self.game_state) )
        self._IA.append( Jogo_IA(self.game_state) )

        print("Jogo iniciado")
    def setarGameState(self):
        self.game_state = [
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1]
        ]

        self.reestart()

    def reestart(self):
        self.play()

    def play(self):
        self.mostrar()
        # try:
        #     posicao = list(map(int,  input("Digite a posição: ").split()))
        #     self.game_state[posicao[0]-1][posicao[1]-1] = self.Ordem[1]     
        # except:
        #     pass

        
        #print(self.GJ.DefinindoGanhador(self.game_state))
        #sleep(2)

        if self.GJ.DefinindoGanhador(self.game_state) != -1:
            self.mostrar()                        
            if self.GJ.DefinindoGanhador(self.game_state) != 2:
                self._IA[self.GJ.DefinindoGanhador(self.game_state)].adicionarJogada(self.game_state)

            #sleep(2)            
            self.Numero_de_Jogos = self.Numero_de_Jogos + 1
            p = randint(0,1)
            if p == 0:
                self.Ordem = [0, 1]
            else:
                self.Ordem = [1, 0]

            self.setarGameState()
            #self.Game_over = not self.Game_over
        else:
            #sleep(2) 
            self._IA[0].Analise_Vetorial(self.game_state, self.Ordem[0])
            self._IA[1].Analise_Vetorial(self.game_state, self.Ordem[1])

        if not self.Game_over:
            self.reestart()

    def mostrar(self):
        system("cls")
        print(
            '''
=> IA numero 1                  => IA numero 2
    Vitórias:           %d          Vitórias:           %d
    Jogadas Aprendidas: %d          Jogadas Aprendidas: %d
                Número de Jogos: %d
            ''' %(self._IA[0].Pontos, self._IA[1].Pontos,
                  self._IA[0].Jogadas_Aprendidas, self._IA[1].Jogadas_Aprendidas, self.Numero_de_Jogos)
            )
        for i in range(3):
            for j in range(3):
                if self.game_state[i][j] == 0:
                    print('X' + "\t|\t", end='')
                elif self.game_state[i][j] == 1:
                    print('O' + "\t|\t", end='')
                else:
                    print(str(self.game_state[i][j]) + "\t|\t", end='')

            print("\n")

j = Main()
j.play()