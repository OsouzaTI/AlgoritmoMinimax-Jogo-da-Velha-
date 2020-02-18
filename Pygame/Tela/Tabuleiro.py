from DefinindoGanhador import Ganhador_Jogo
from os import system
from time import sleep
from threading import Thread
from threading import Event
import sys

class Tempo_De_Execucao(Thread):
    TempoDeExecucao = 0
    Reset = True
    def __init__ (self):
        Thread.__init__(self)  
        self._stop = Event() 
        print("THREAD INICIADA")      

    # function using _stop function 
    def stop(self): 
        self._stop.set() 
  
    def stopped(self): 
        return self._stop.isSet() 

    def run(self):   

        while True: 
            if self.stopped(): 
                return
            sleep(0.01)
            print("THREAD RODANDO -> ", self.TempoDeExecucao)                   
            self.TempoDeExecucao = self.TempoDeExecucao + 0.01

    def resetaTempoExecucao(self):
        self.TempoDeExecucao = 0          
        self.stop()

    def getTempoExecucao(self):
        return self.TempoDeExecucao
        

class Tabuleiro:
    Ganhador = Ganhador_Jogo()
    Game_State = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

    fc = 0
       

    BestSpot = None
    Jogos = 0

    IAplayer = 'X'
    IApontos = 0
    HUplayer = 'O'
    HUpontos = 0
    def __init__(self, Game_State, HU, IA):
        self.Game_State = Game_State
        self.IAplayer = IA
        self.HUplayer = HU               
        

    def mapa_vazios(self, _Game_State):

        indices_vazios = []

        for i in range(9):
            if _Game_State[i] != 'O' and _Game_State[i] != 'X' :
                indices_vazios.append(i)
        #print(indices_vazios)    
        return indices_vazios
    
    def MiniMax(self, _Game_State, player):

        self.fc = self.fc + 1        
        indices_vazios = self.mapa_vazios(_Game_State)

        if ( self.Ganhador.DefinindoGanhador(_Game_State, self.HUplayer) ):
            return [-10]
        elif( self.Ganhador.DefinindoGanhador(_Game_State, self.IAplayer) ):
            return [10]
        elif( len(indices_vazios) == 0 ):
            return [0]

        moves = []

        for i in range( len(indices_vazios) ):

            move = []
            move.append(indices_vazios[i])

            _Game_State[indices_vazios[i]] = player

            if player == self.IAplayer:
                result = self.MiniMax(_Game_State, self.HUplayer)                
                move.append(result[1] if len(result) > 1 else result[0])
            else:
                result = self.MiniMax(_Game_State, self.IAplayer)
                move.append(result[1] if len(result) > 1 else result[0])
            
            _Game_State[indices_vazios[i]] = -1

            moves.append(move)

        #print(moves)
        BestMove = None
        if player == self.IAplayer:
            BestScore = -10000
            for i in range( len(moves) ):
                if moves[i][1] > BestScore:
                    BestScore = moves[i][1]
                    BestMove = i
        else:
            BestScore = 10000
            for i in range( len(moves) ):
                if moves[i][1] < BestScore:
                    BestScore = moves[i][1]
                    BestMove = i
                     
        return moves[BestMove]
            
    def setGame_State(self, Game_State):
        self.Game_State = Game_State

    def playerHU(self):
        print("\n")
        n = int(input("Digite a posição: "))
        self.Game_State[n] = self.HUplayer

    def playerIA(self):             
        th = Tempo_De_Execucao()  
        th.start()  
        self.BestSpot = self.MiniMax(self.Game_State, self.IAplayer)        
        Informacoes = [
            self.BestSpot[0], self.fc, th.getTempoExecucao()
        ]
        self.fc = 0      
        th.resetaTempoExecucao()        
        # try:
        #     self.Game_State[self.BestSpot] = self.IAplayer
        #     print("\nMelhor Jogada(Posição): %d" %(self.BestSpot))        
        #     print("Chamadas Recursivas: %d" %(self.fc))
        #     self.fc = 0
        # except IndexError:
        #     self.resetarTabuleiro()

        # sleep(5)

        return Informacoes


    def mostrar(self):
        system("cls")
        print(
            '''
                Jogos Realizados: %d
                IA pontos:        %d
                HUpontos :        %d
            '''
        %(self.Jogos, self.IApontos, self.HUpontos))
        for i in range(9):
            if i % 3 == 0:
                print("\n")
            
            if self.Game_State[i] == 'X':
                print("X|\t", end='')
            elif self.Game_State[i] == 'O':
                print("O|\t", end='')
            else:
                print(" |\t", end='')

        #print(self.Game_State)

    def playGame(self, b):
        
        self.mostrar()    
        
        if not b:
            self.playerIA()
        else:
            self.playerHU()

        self.mostrar()

        if ( self.Ganhador.DefinindoGanhador(self.Game_State, self.HUplayer) ):
            self.HUpontos = self.HUpontos + 1
            print("Maquina Burra KapaKapakapa!")
            sleep(2)
            self.resetarTabuleiro()
        elif( self.Ganhador.DefinindoGanhador(self.Game_State, self.IAplayer) ):
            self.IApontos = self.IApontos + 1
            print("HOLY SHIT IA ganhou!")
            sleep(2)
            self.resetarTabuleiro()
        elif( len(self.mapa_vazios(self.Game_State)) == 0 ):
            self.resetarTabuleiro()
    
        return self.playGame(not b)        
        

    def resetarTabuleiro(self):

        self.Game_State = [
                    'O', -1, 'X',
                    'X', -1, 'X',
                    -1,  'O', 'O'                  
                ]
        
        self.fc = 0

        self.playGame(False)
        

# t = Tabuleiro([-1, -1, -1, -1, -1, -1, -1, -1, -1], 'O', 'X')
# t.playGame(True)
#t.mostrar()