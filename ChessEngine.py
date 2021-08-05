class GameState():
    def __init__(self):
        self.board= [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["xx","xx","xx","xx","xx","xx","xx","xx"],
            ["xx","xx","xx","xx","xx","xx","xx","xx"],
            ["xx","xx","xx","xx","xx","xx","xx","xx"],
            ["xx","xx","xx","xx","xx","xx","xx","xx"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wK","wQ","wB","wN","wR"],
            ]
        self.whiteToMove =True
        self.moves =[]
    
    '''Checks for validity of the first click'''
    def getValidityOfFirstClick(self,p):
        if(self.board[p[0]][p[1]]=="xx"):
            return False
        if(self.whiteToMove):
            if(self.board[p[0]][p[1]][0]!="w"):
                return False
        else:
            if(self.board[p[0]][p[1]][0]!="b"):
                return False
        return True

    '''Executes a move that has been passed in'''
    def makeMove(self,move):
        if(self.board[move.startRow][move.startColumn]=="xx"):
            print("Invalid move")
            return
        if(self.board[move.endRow][move.endColumn][0]==self.board[move.startRow][move.startColumn][0]):
            print("Invalid move - same colour piece")
            return
        if self.whiteToMove and self.board[move.startRow][move.startColumn][0]!="w":
            print("Invalid move - white has to play")
            return
        if not self.whiteToMove:
            if(self.board[move.startRow][move.startColumn][0]!="b"):
                print("Invalid move - black has to play")
                return
        self.board[move.startRow][move.startColumn]="xx"
        self.board[move.endRow][move.endColumn]=move.pieceMoved
        self.moves.append(move)
        self.whiteToMove= not self.whiteToMove
    
    def UndoLastMove(self):
        if(len(self.moves)!=0):
            move = self.moves.pop()
            self.board[move.startRow][move.startColumn]=move.pieceMoved
            self.board[move.endRow][move.endColumn]=move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
    '''Defining all moves'''
    '''Pawn and Rook moves done'''
    '''Bishop moves now'''
    def getValidRookMoves(self,row,column,moves):
        dx = (0,0,-1,1)
        dy = (-1,1,0,0)
        for d in range(4):
            for i in range(1,8):
                nextRow = row + dx[d]*i
                nextColumn = column + dy[d]*i
                if 0<=nextRow<=7 and 0<=nextColumn<=7:
                    if self.board[nextRow][nextColumn]=="xx":
                        moves.append(Move((row,column),(nextRow,nextColumn),self.board))
                    elif self.board[nextRow][nextColumn][0]!=self.board[row][column][0]:
                        moves.append(Move((row,column),(nextRow,nextColumn),self.board))
                        break
                    else:
                        break
                else:
                    break
    def getValidKnightMoves(self):
        pass
    def getValidBishopMoves(self,row,column,moves):
        dx = (-1,-1,1,1)
        dy = (-1,1,1,-1)
        for d in range(4):
            for i in range(1,8):
                nextRow = row + dx[d]*i
                nextColumn = column + dy[d]*i
                if 0<=nextRow<=7 and 0<=nextColumn<=7:
                    if self.board[nextRow][nextColumn]=="xx":
                        moves.append(Move((row,column),(nextRow,nextColumn),self.board))
                    elif self.board[nextRow][nextColumn][0]!=self.board[row][column][0]:
                        moves.append(Move((row,column),(nextRow,nextColumn),self.board))
                        break
                    else:
                        break
                else:
                    break
    def getValidQueenMoves(self,row,column,moves):
        self.getValidBishopMoves(row,column,moves)
        self.getValidRookMoves(row,column,moves)

    def getValidKingMoves(self):
        pass
    '''Doesnt have special moves'''
    def getValidPawnMoves(self,row,column,moves):
        if self.whiteToMove:
            '''The square in front is free'''
            if row-1>=0 and self.board[row-1][column]=="xx":
                moves.append(Move((row,column),(row-1,column),self.board))  
                '''As there are two options for the first pawn move'''
                if(row==6 and self.board[row-2][column]=="xx"):
                    moves.append(Move((row,column),(row-2,column),self.board))
            '''Captures and white can only capture a black piece'''
            if row-1>=0 and column+1<=7 and self.board[row-1][column+1][0]=="b":
                moves.append(Move((row,column),(row-1,column+1),self.board))
            if row-1>=0 and column-1>=0 and  self.board[row-1][column-1][0]=="b":
                moves.append(Move((row,column),(row-1,column-1),self.board))

        else:
            '''The square in front is free'''
            if row+1<=7 and  self.board[row+1][column]=="xx":
                moves.append(Move((row,column),(row+1,column),self.board))
                '''As there are two options for the first pawn move'''
                if(row==1 and self.board[row+2][column]=="xx"):
                    moves.append(Move((row,column),(row+2,column),self.board))
            '''Captures and black can only capture a white peice'''
            if row+1<=7 and column+1 <=7 and self.board[row+1][column+1][0]=="w":
                moves.append(Move((row,column),(row+1,column+1),self.board))
            if row+1<=7 and column-1>=0 and self.board[row+1][column-1][0]=="w":
                moves.append(Move((row,column),(row+1,column-1),self.board))
    def getAllPossibleMoves(self):
        moves = []
        for row in range (0,8):
            for column in range(0,8):
                curPeice = self.board[row][column]
                if(curPeice[0]=="b" and not self.whiteToMove) or (curPeice[0]=="w" and self.whiteToMove):
                    if curPeice[1]=="R":
                        self.getValidRookMoves(row,column,moves)
                    elif curPeice[1]=="N":
                        self.getValidKnightMoves()
                    elif curPeice[1]=="B":
                        self.getValidBishopMoves(row,column,moves)
                    elif curPeice[1]=="Q":
                        self.getValidQueenMoves(row,column,moves)
                    elif curPeice[1]=="K":
                        self.getValidKingMoves()
                    elif curPeice[1]=="p":
                        self.getValidPawnMoves(row,column,moves) 
        return moves                    
    
    

class Move():
    rankToRow= {"1":7 ,"2":6 ,"3":5 ,"4":4 ,"5":3 ,"6":2,"7":1,"8":0}
    fileToColumn={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    rowToRank= {v: k for k,v in rankToRow.items()}
    columnToFile= {v:k for k,v in fileToColumn.items()}
    def __init__(self,startSquare,endSquare,board):
        self.startRow = startSquare[0]
        self.endRow = endSquare[0]
        self.startColumn = startSquare[1]
        self.endColumn  = endSquare[1]
        self.pieceMoved = board[self.startRow][self.startColumn] 
        self.pieceCaptured =board[self.endRow][self.endColumn]
        self.moveID = self.startRow*4000+self.startColumn*400+self.endRow*40+self.endColumn*4

    def __eq__(self,other):
        return isinstance(other,Move) and self.moveID==other.moveID  
    def preOutput(self):
        return self.getRankFile(self.startRow,self.startColumn)+self.getRankFile(self.endRow,self.endColumn)
    def getRankFile(self,row,column):
        return self.columnToFile[column]+self.rowToRank[row]