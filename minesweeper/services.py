
from models import Cell,Board
import random
from pdb import set_trace as bp


status={'end':-1}
game=None

class Game_Service(object):

    def __init__(self,row_num,col_num):
        self._row_num=row_num
        self._col_num=col_num
        if game is None:
            global game
            game=Board(row_num,col_num)
        mine_percent=0.3
        self._mine_num=int(mine_percent*float(self._row_num*self._col_num))
        self.shifts=[-1,0,1]
        
        
    def generate_map(self):
    """ generate mine map
    """
        s=set([])
        while len(s)<=self._mine_num:
            i=random.randint(0, self._row_num*self._col_num-1)
            if i not in s:
                self._set_mine(i)
                s.add(i)     
        return {#'board':[game.get_board()[inx].get_neighbor() for inx in range(0,self._row_num*self._col_num)],
                #'mines':game.get_mines(),
                'row_num':self._row_num,
                'col_num':self._col_num}
    

    def _set_mine(self,index):
    """ set cell[index] as a mine
        and update its neighbor cell's mine number
    """
        game.get_cell(index).set_mine() #set current index as mine
        game.add_mine(index) #add index to mine_index

        # add its neighbor's neighbor_num     
        temp_r=index/self._col_num
        temp_c=index%self._col_num
        shift=[[temp_r+dr,temp_c+dc] for dr in self.shifts for dc in self.shifts
                if [temp_r+dr,temp_c+dc]!=[temp_r,temp_c]
                and temp_r+dr in range(0,self._row_num)
                and temp_c+dc in range(0,self._col_num)]
        for s in shift:
            game.get_cell(s[0]*self._col_num+s[1]).add_neighbor()
            

    def choose_mine(self,index):
    """ choose a cell
        return game status and cells need to change
    """
        cell=game.get_cell(index)
        update_stack={'type':'continue'}
        
        if cell.isMine():
            self._flipAll(update_stack) #clicked on a mine
        else:
            self._flip(update_stack,index) #clicked on a safe cell

        return update_stack
    

    def _flip(self,update_stack,index):
    """ flip the chosen cell and its adjcent cells
    """
        cell=game.get_cell(index)
        if cell.ifFlipped()==False:
            cell.flip()
            game.decrease_remain()
            if cell.isMine()==False and cell.get_neighbor()>0:
                update_stack[str(index)]=cell.get_neighbor()
                return
            elif cell.isMine()==False and cell.get_neighbor()==0:
                update_stack[str(index)]=cell.get_neighbor()
                temp_r=index/self._col_num
                temp_c=index%self._col_num
                shift=[[temp_r+dr,temp_c+dc] for dr in self.shifts for dc in self.shifts
                       if [temp_r+dr,temp_c+dc]!=[temp_r,temp_c]
                       and temp_r+dr in range(0,self._row_num)
                       and temp_c+dc in range(0,self._col_num)]
                for s in shift:
                    self._flip(update_stack,s[0]*self._col_num+s[1])
                    

    def _flipAll(self,update_stack):
    """ flip all mines
    """
        mines_index=game.get_mines()
        for i in mines_index:
            update_stack[str(i)]=status['end']

        update_stack['row_num']=self._row_num
        update_stack['col_num']=self._col_num
        update_stack['_mine_num']=len(mines_index) 
        if len(mines_index)==game.get_remain():     
            update_stack['type']='win'  
        else:
            update_stack['type']='lose'
            
    
            
            
        
