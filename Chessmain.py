import pygame

from ChessEngine import GameState
import ChessEngine

WIDTH = HEIGHT= 512
DIM = 8
Square_size  = WIDTH//DIM 
MAX_FPS = 30
IMAGES = {}

def loadIMAGES():
    pieces = ["bR","bN","bB","bQ","bK","wR","wN","wB","wK","bp","wp","wQ"]
    
    for piece in pieces:
        IMAGES[piece]= pygame.transform.scale(pygame.image.load("./images/"+piece+".png"),(Square_size,Square_size))
        
def drawGameState(screen,gamestate):
    drawBoard(screen)
    drawPieces(screen,gamestate.board)
        
def drawBoard(screen):
    colors = [pygame.Color("white"),pygame.Color("gray")]
    for i in range(DIM):
        for j in range(DIM):
            color = colors[((i+j)%2)]
            pygame.draw.rect(screen,color,pygame.Rect(j*Square_size,i*Square_size,Square_size,Square_size))
def drawPieces(screen,board):
    for i in range(DIM):
        for j in range(DIM):
             piece  = board[j][i]
             if piece !="xx":
                 screen.blit(IMAGES[piece],pygame.Rect(i*Square_size,j*Square_size,i,j))
def colorCell(screen,y,x,color):
    pygame.draw.rect(screen,color,pygame.Rect(x*Square_size,y*Square_size,Square_size,Square_size))


def main():
    pygame.init()
    screen  = pygame.display.set_mode((WIDTH,HEIGHT))
    clock  = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    gameState = GameState()
    moveMade =False
    validMoves = gameState.getAllPossibleMoves()
    loadIMAGES()
    running =True
    #to track
    squareSelected=()
    playerClicks = []
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                print("exiting")
                running =False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_z:
                    gameState.UndoLastMove() 
                    moveMade=True
    
            elif e.type == pygame.MOUSEBUTTONDOWN:
                location=pygame.mouse.get_pos()
                ## get row and column
                column = location[0]//Square_size
                row = location[1]//  Square_size
                ##if the same square is clicked twice
                if(squareSelected ==(row,column)):
                    squareSelected=()
                    playerClicks=[]
                #push the sqaure to the list
                else:
                    squareSelected = (row,column)
                    playerClicks.append(squareSelected)


                '''if a blank square is selected  or other colored piece is selected'''
                
                if (len(playerClicks)==1):
                    if(not gameState.getValidityOfFirstClick(playerClicks[0])):
                        squareSelected=()
                        playerClicks=[]
                        print("Select a peice or a peice of your color")                        
                        
                #Checked if the move is a valid move or not 
                if(len(playerClicks)==2):
                    move = ChessEngine.Move(playerClicks[0],playerClicks[1],gameState.board)
                    if move in validMoves:
                        print(move.preOutput())
                        gameState.makeMove(move)
                        moveMade = True
                    else :
                        print("Not a valid move")
                    squareSelected=()
                    playerClicks=[]
        if moveMade:
            validMoves = gameState.getAllPossibleMoves()
            moveMade = False
        
        drawGameState(screen,gameState)
        pygame.display.update()
        clock.tick(MAX_FPS)
        pygame.display.flip()
if __name__ == "__main__":
    main()