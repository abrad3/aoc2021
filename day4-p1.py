import pandas as pd
filename="./input-day4.csv"

bingoTables=pd.read_csv(filename, header=None, skiprows=1)
calledNumbers=(pd.read_csv(filename, header=None, nrows=1).values)[0]

class BingoBoard:
    def __init__(self, board):
        self.board = board
        self.marked = [ [0 for x in range(5)] for y in range(5) ]
        self.winner = "False"

    def updateBoard(self, number):
        for x in range(0, len(self.board)):
            try:
                pos=self.board[x].index(number)
                self.marked[x][pos]=1
            except:
                continue 
    def isWinner(self):
        counter = [0]*5
        for x in range(0, len(self.board)):
            if sum(self.marked[x]) == 5: 
                self.winner = True
                return True
            for y in range(0, len(self.board)):
                counter[y] += self.marked[x][y]
        if 5 in counter: 
            self.winner = True
            return True
        else: 
            return False

    def showBoard(self):
        print(self.board)

    def score(self):
        counter = 0
        for x in range(0, len(self.board)):
            for y in range(0, len(self.board)):
               if self.marked[x][y]==0: 
                   counter += self.board[x][y]
        return counter

def dataToBoards(tables):
    listofBoards = []
    for i in range(0, tables.size, 5):
        board = tables.loc[i:i+4].reset_index()
        boardList = []
        for j in range(0, 5):
            row = board[0].loc[j].split(' ')
            numRow = [ int(n) for n in row if n != '']
            boardList.append(numRow)
        listofBoards.append(BingoBoard(boardList))
    return listofBoards

boards = dataToBoards(bingoTables)

def winningNumber(boards, numbers):
   for i in numbers:
       for b in boards:
           b.updateBoard(i)
           if b.isWinner():
              return [i, b.score()]
           else: continue

result = winningNumber(boards, calledNumbers)
print("The answer is: "+str(result[0]*result[1]))
