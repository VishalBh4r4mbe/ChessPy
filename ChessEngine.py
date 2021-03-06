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
        '''Keeping Track of the king to check for Checks'''
        self.whiteKing = (7,4)
        self.blackKing = (0,4)
        self.currentlyInCheck = False
        self.pins= []
        self.checks = []    
    
    '''
    Checks for validity of the first click
    '''
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
        '''These were dealt with in Valid move generation and Other Validity Checker for the first click'''
        # if(self.board[move.endRow][move.endColumn][0]==self.board[move.startRow][move.startColumn][0]):
        #     print("Invalid move - same colour piece")
        #     return
        # if self.whiteToMove and self.board[move.startRow][move.startColumn][0]!="w":
        #     print("Invalid move - white has to play")
        #     return
        # if not self.whiteToMove:
        #     if(self.board[move.startRow][move.startColumn][0]!="b"):
        #         print("Invalid move - black has to play")
        #         return
        if(self.board[move.startRow][move.startColumn][1]=="wK"):
            self.whiteKing = (move.endRow,move.endColumn)
        if(self.board[move.startRow][move.startColumn][1]=="bK"):
            self.blackKing = (move.endRow,move.endColumn)

        self.board[move.startRow][move.startColumn]="xx"
        self.board[move.endRow][move.endColumn]=move.pieceMoved
        self.moves.append(move)
        self.whiteToMove= not self.whiteToMove
    
    def UndoLastMove(self):
        '''Removes the last move and changes the board accordingly'''
        if(len(self.moves)!=0):
            move = self.moves.pop()
            self.board[move.startRow][move.startColumn]=move.pieceMoved
            self.board[move.endRow][move.endColumn]=move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
    
    
    '''Checks for Checks and pins and returns them'''
    def PinCheckChecker(self):
        pins = []
        checks = []
        inCheck = False
        if self.whiteToMove:
            startRow ,startColumn = self.whiteKing
            curColor = "w"
            oppColor = "b"
        else :
            startRow ,startColumn = self.blackKing
            curColor = "b"
            oppColor = "w"
        dirs = ((-1,0),(0,-1),(1,0),(0,1),(-1,-1),(1,-1),(-1,1),(1,1))
            
        for i in range(8):
            possiblePin =()
            for j in range(1,8):
                endRow = startRow + j*dirs[i][0]
                endColumn = startColumn + j*dirs[i][1]
                if 0<=endRow<=7 and 0<=endColumn<=7:
                    endPiece = self.board[endRow][endColumn]
                    if endPiece[0]==curColor:
                        if len(possiblePin)==0:
                            possiblePin = (endRow,endColumn,dirs[i][0],dirs[i][1])
                        else :
                            break
                    elif endPiece[0]==oppColor:
                        peice= endPiece[1]
                        if (0<=i<=3 and peice=='R') or (4<=i<=7 and peice=='B') or (i==1 and peice=='p') and ((6<=i<=7 and oppColor=='w') or (4<=i<=5 and oppColor=='b')) or peice == 'Q' or (i==1 and peice=='K'):
                            if(len(possiblePin)==0):
                                inCheck= True
                                checks.append((endRow,endColumn,dirs[i][0],dirs[i][1]))
                            else :
                                pins.append(possiblePin)
                                break
                        else :
                            break
                else :
                    break
        knightDirs = ((-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1))
        for i in range(8):
            endRow = startRow + knightDirs[i][0]
            endColumn = startColumn + knightDirs[i][1]
            if 0<=endRow<=7 and 0<=endColumn<=7:
                endPiece = self.board[endRow][endColumn]
                if endPiece[0]==oppColor and endPiece[1]=='N':
                    inCheck = True
                    checks.append((endRow,endColumn,knightDirs[i][0],knightDirs[i][1]))
            
        return inCheck,pins,checks
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
    def getValidKnightMoves(self,row,column,moves):
        dx = (-2,-2,2,2,-1,1,-1,1)
        dy = (-1,1,-1,1,2,2,-2,-2)
        for d in range(8):
            nextRow = row + dx[d]
            nextColumn = column + dy[d]
            if 0<=nextRow<=7 and 0<=nextColumn<=7:
                if self.board[nextRow][nextColumn]=="xx":
                    moves.append(Move((row,column),(nextRow,nextColumn),self.board))
                elif self.board[nextRow][nextColumn][0]!=self.board[row][column][0]:
                    moves.append(Move((row,column),(nextRow,nextColumn),self.board))             
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

    def getValidKingMoves(self,row,column,moves):
        dx = (-1,-1,0,1,1,1,0,-1)
        dy = (-1,0,-1,0,-1,1,1,1)
        for d in range(8):
            nextRow = row + dx[d]
            nextColumn = column + dy[d]
            if 0<=nextRow<=7 and 0<=nextColumn<=7:
                if self.board[nextRow][nextColumn]=="xx":
                    moves.append(Move((row,column),(nextRow,nextColumn),self.board))
                elif self.board[nextRow][nextColumn][0]!=self.board[row][column][0]:
                    moves.append(Move((row,column),(nextRow,nextColumn),self.board))
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
                        self.getValidKnightMoves(row,column,moves)
                    elif curPeice[1]=="B":
                        self.getValidBishopMoves(row,column,moves)
                    elif curPeice[1]=="Q":
                        self.getValidQueenMoves(row,column,moves)
                    elif curPeice[1]=="K":
                        self.getValidKingMoves(row,column,moves)
                    elif curPeice[1]=="p":
                        self.getValidPawnMoves(row,column,moves) 
        return moves                    
    
    def ValidMoveFinder(self):
        moves = []
        self.inCheck ,self.pins,self.checks = self.PinCheckChecker()
        if self.whiteToMove:
            kingPos = self.whiteKing
        else :
            kingPos = self.blackKing
        if self.inCheck:
            if len(self.checks)==1:
                moves = self.getAllPossibleMoves()
                checkRow = self.checks[0][0]
                checkColumn = self.check[0][1]
                CheckingPeice = self.board[checkRow][checkColumn]
                validSquares = []
                if CheckingPeice == 'N':
                    validSquares = [(checkRow,checkColumn)]
                else :
                    for i in range(1,8):
                        validSquare = (kingPos[0] + i*self.checks[0][2],kingPos[1] + i*self.checks[0][3])
                        validSquares.append(validSquare)
                        if(validSquare[0]==checkRow and validSquare[1]==checkColumn):
                            break  
                
                for i in range(len(moves),-1,-1,-1):
                    if moves[i].pieceMoved[1]!='K':
                        if not (moves[i].endRow,moves[i].endColumn) in validSquares:
                            moves.remove(moves[i])
            else:
                self.getValidKingMoves(kingPos[0],kingPos[1],moves)
        else:
            moves = self.getAllPossibleMoves()
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