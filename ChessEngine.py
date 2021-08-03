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
        self.pieceCapture =board[self.endRow][self.endColumn]
    
    
    def preOutput(self):
        return self.getRankFile(self.startRow,self.startColumn)+self.getRankFile(self.endRow,self.endColumn)
    def getRankFile(self,row,column):
        return self.columnToFile[column]+self.rowToRank[row]
    