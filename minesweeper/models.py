

class Board(object):
    def __init__(self,row_num,col_num):
        self._row_num=row_num
        self._col_num=col_num
        self._mine_index=[]
        self._board=[Cell() for i in range(self._row_num*self._col_num+1)]
        self._remain=row_num*col_num

    def get_cell(self,index):
        return self._board[index]

    def get_mines(self):
        return self._mine_index

    def add_mine(self,index):
        self._mine_index.append(index)

    def get_board(self):
        return self._board

    def get_remain(self):
        return self._remain

    def decrease_remain(self):
        self._remain-=1


class Cell(object):
    def __init__(self):
        self._isMine=False
        self._neighbor=0
        self._ifFlipped=False

    def set_mine(self):
        self._isMine=True

    def add_neighbor(self):
        self._neighbor+=1

    def flip(self):
        self._ifFlipped=True

    def isMine(self):
        return self._isMine

    def ifFlipped(self):
        return self._ifFlipped

    def get_neighbor(self):
        return self._neighbor
        
    
