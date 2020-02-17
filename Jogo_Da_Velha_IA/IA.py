class IA_jogo:

    Mapa          = None
    '''
        Neste caso tanto a matriz 
        de derrotas como a de vitórias,
        Logo alimente essa variavel com 2 matrizes bi-dimensionais
    '''
    Numero_de_Neuronios = None
    Neuronios           = []

    def __init__(self, MP, NR, JG, JP, JE):        
        self.Numero_de_Neuronios = NR
        for i in range(NR):
            self.Neuronios.append(Neuronio(JG, JP, JE, MP))

    def jogadaIA(self, MP):
        self.Neuronios[0].Atualizar_Mapa(MP)
        self.Neuronios[0].Analise_Vetorial()



class Neuronio:

    Jogadas_Ganhas     = None
    Jogadas_Perdidas   = None
    Jogadas_Empatadas  = None
    Jogadas_Totais     = []
    Mapa               = []
    Mapa_Computacional = []

    #Construtor da classe
    def __init__(self, JG, JP, JE, MP):
        
        self.Jogadas_Ganhas    = JG
        self.Jogadas_Perdidas  = JP
        self.Jogadas_Empatadas = JE 
        self.Jogadas_Totais = [self.Jogadas_Ganhas, self.Jogadas_Perdidas, self.Jogadas_Empatadas]
        self.Mapa              = MP
        self.Mapa_Computacional = list( 0 for i in range( len(self.Mapa) ) )
    def Atualizar_Mapa( self, MP ):
        self.Mapa = MP

    def Conversor_Mapa( self ):

        for i in range( len(self.Mapa)  ):
            if self.Mapa[i] == 'x':
                self.Mapa_Computacional[i] = 0
            
            elif self.Mapa[i] == 'o':
                self.Mapa_Computacional[i] = 1

            else:
                self.Mapa_Computacional[i] = -1



    def Analise_Vetorial( self ):
        
        self.Conversor_Mapa()
        Previsao_Melhor_Jogada = [0 , 0] #indice de algum dos 3 vetores principais
        Analise_Numerica = [
            ["Jogadas Ganhas"   , list(0 for x in range(len(self.Jogadas_Ganhas   )) ) ],            
            ["Jogadas Empatadas", list(0 for x in range(len(self.Jogadas_Empatadas)) ) ],
        ]
        for i in range(2):
            for j  in range( len(self.Jogadas_Totais[i]) ):
                for k in range(9):
                    if self.Mapa_Computacional[k] == self.Jogadas_Totais[i][j][k]:
                        Analise_Numerica[i][1][j] += 1
                        if Previsao_Melhor_Jogada[1] < Analise_Numerica[i][1][j]:
                            Previsao_Melhor_Jogada = [i, j]
        #print(Previsao_Melhor_Jogada)
        for i in range(9):
            if self.Mapa[i] == '-':
                if self.Jogadas_Ganhas[Previsao_Melhor_Jogada[1]][i] == 1:
                    self.Mapa[i] = 'o'
                    break
                



        