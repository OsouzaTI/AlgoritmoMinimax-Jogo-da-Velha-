Horizontal = 0
Vertical   = 0

def verificarG(MP, n):
    if MP[n] == 'x':
        return 0
    elif MP[n] == 'o':
        return 1

def G_horizontal( MP ):
    if MP[0] == MP[1] == MP[2] and MP[0] != '-' and MP[1] != '-' and MP[2] != '-':
        return verificarG(MP, 0)

    if MP[3] == MP[4] == MP[5] and MP[0] != '-' and MP[1] != '-' and MP[2] != '-':
        return verificarG(MP, 3)
    
    if MP[6] == MP[7] == MP[8] and MP[0] != '-' and MP[1] != '-' and MP[2] != '-':
        return verificarG(MP, 6)
    
    return -1

def G_vertical( MP ):
    if MP[0] == MP[3] == MP[6] and MP[0] != '-' and MP[3] != '-' and MP[6] != '-':
        return verificarG(MP, 0)

    if MP[1] == MP[4] == MP[7] and MP[1] != '-' and MP[4] != '-' and MP[7] != '-':
        return verificarG(MP, 1)
    
    if MP[2] == MP[5] == MP[8] and MP[2] != '-' and MP[5] != '-' and MP[8] != '-':
        return verificarG(MP, 2)

    return -1

def G_diagonal( MP ):
    if MP[0] == MP[4] == MP[8] and MP[0] != '-' and MP[4] != '-' and MP[8] != '-':
        return verificarG(MP, 0)

    if MP[2] == MP[4] == MP[6] and MP[2] != '-' and MP[4] != '-' and MP[6] != '-':
        return verificarG(MP, 2)

    return -1

def GanhouMaster( MP ):
    if G_horizontal(MP) != -1:
        return G_horizontal(MP)
    elif G_vertical(MP) != -1:
        return G_vertical(MP)
    elif G_diagonal(MP) != -1:
        return G_diagonal(MP)
    
    return -1
