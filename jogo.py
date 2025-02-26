#Projeto jogo da velha

tabuleiro = [['a', 'b', 'c'], 
             ['d', 'e', 'f'], 
             ['g', 'h', 'i']]

jogador = 'X'
jogadas = 0

def MostrarTabuleiro():
    print(tabuleiro[0])
    print(tabuleiro[1])
    print(tabuleiro[2])
    
def verificarVencedor():
    for linha in range(3):
        if tabuleiro[linha][0] == \
            tabuleiro[linha][1] == \
            tabuleiro[linha][2]:
            return True
            
    for coluna in range(3):
        if tabuleiro[0][coluna] == \
            tabuleiro[1][coluna] == \
            tabuleiro[2][coluna]:
            return True
            
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        return True
        
    return False            
            
    
while jogadas < 9:
    MostrarTabuleiro()
    posicao = input(f"{jogador} Insira a posição que deseja jogar: ")

    jogada_realizada = False
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == posicao:
                tabuleiro[linha][coluna] = jogador
                jogada_realizada = True
                                
    if jogada_realizada == False:
        jogador = 'O' if jogador == 'X' else 'X'
        jogadas += 1
                
    if verificarVencedor():            
        print(f"O jogador vencedor foi {jogador}!")
        break
    
    
