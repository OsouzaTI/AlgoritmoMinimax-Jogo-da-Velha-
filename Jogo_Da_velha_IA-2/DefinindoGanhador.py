from time import sleep

class Ganhador_Jogo:

    Mapa = None

    def __init__(self):
        pass

    def DefinindoGanhador(self, MP):

        self.Mapa = MP

        if self.horizontal() != -1 or self.vertical() != -1 or self.diagonal() != -1 or self.empate() == 1:
            if self.horizontal() != -1:
                return self.horizontal()
            elif self.vertical() != -1:
                return self.vertical()
            elif self.diagonal() != -1:
                return self.diagonal()
            else:
                return 2
        else:
            return -1
        

    def horizontal(self):
        h = 0
        for i in range(3):
            for j in range(2):
                if self.Mapa[i][j] == self.Mapa[i][j+1] and self.Mapa[i][j] != -1:
                    h = h + 1
                    #print("Achei :" + str(self.Mapa[i][j]))
            if h == 2:
                return self.Mapa[i][j]
            else:
                h = 0
        
        return -1
        

    def vertical(self):
        v = 0
        for i in range(3):
            for j in range(2):
                if self.Mapa[j][i] == self.Mapa[j+1][i] and self.Mapa[j][i] != -1:
                    v = v + 1
            if v == 2:
                return self.Mapa[j][i]
            else:
                v = 0
        
        return -1
    
    def diagonal(self):
        d = 0
        for i in range(2):
            if self.Mapa[i][i] == self.Mapa[i+1][i+1] and self.Mapa[i][i] != -1:
                d = d + 1

        if d == 2:           
            return self.Mapa[i][i]
        
        d = 0

        for i in range(2):
            if self.Mapa[i][3-(i+1)] == self.Mapa[i+1][3-(i+2)] and self.Mapa[i][3-(i+1)] != -1:
                d = d + 1
        if d == 2:
            return self.Mapa[i][3-(i+1)]
        else:
            return -1

    def empate(self):                
        for i in range(3):
            for j in range(3):
                if self.Mapa[i][j] == -1:
                    return -1
        
        return 1
                
                    
        