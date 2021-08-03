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

def main():
    pygame.init()
    screen  = pygame.display.set_mode((WIDTH,HEIGHT))
    clock  = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    game_state = GameState();
    loadIMAGES()
    running =True
    #to track
    squareSelected=()
    playerClicks = []
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running =False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                location=pygame.mouse.get_pos()
                row = location[0]//Square_size
                column = location[1]//  Square_size
                
                if(squareSelected ==(column,row)):
                    squareSelected=()
                    playerClicks=[]
                else:
                    squareSelected = (row,column)
                    playerClicks.append(squareSelected)
                if(len(playerClicks)==2):
                    move = ChessEngine.Move(playerClicks[0],playerClicks[1],game_state.board);
                    print(move.preOutput())
                    game_state.makeMove(move)
                    squareSelected=()
                    playerClicks=[]
        drawGameState(screen,game_state)
        pygame.display.update()
        clock.tick(MAX_FPS)
        pygame.display.flip()
if __name__ == "__main__":
    main()