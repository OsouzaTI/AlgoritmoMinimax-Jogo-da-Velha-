class Base:
    #Banco_de_Jogadas[0][1 ou 2 ou 3(São os estados de cada linha da jogada salva)]
    Banco_de_Jogadas = [

        [#Posição 0 -> Matiz de posições
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1],
        ],
        # [#Posição 1 -> Matiz de posições
        #     [0,  0, 0],
        #     [1, 1, -1],
        #     [0, -1, 1],
        # ],
        # [#Posição 2 -> Matiz de posições
        #     [1,  0, 1],
        #     [0,  0, 1],
        #     [1,  0,-1],
        # ],
        # [#Posição 3 -> Matiz de posições
        #     [1,  0, 0],
        #     [0,  1, 1],
        #     [0,  1, 0],
        # ],
        # [#Posição 4 -> Matiz de posições
        #     [0,  1, 1],
        #     [1,  0, 0],
        #     [0,  0, 1],
        # ],
        # [#Posição 5 -> Matiz de posições
        #     [0,  0, 1],
        #     [1,  1, 0],
        #     [0,  1, 0],
        # ],
        # [#Posição 6 -> Matiz de posições
        #     [0,  1, 0],
        #     [1,  1, 0],
        #     [0,  1, 1],
        # ],


    ]

    def __init__(self):
        pass

    def getBanco_de_Jogadas(self):
        return self.Banco_de_Jogadas
    
    def addJogada(self, MP):
        self.Banco_de_Jogadas.append(MP)