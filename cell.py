from tkinter import *
import utils
import values
import game
import random
import time
import game

class Cell:
    
    #class variable to store ALL cells
    cells=[]
    
    #class variable to store ALL mines
    mines=[]
    
    #class variable keeping track of the unopened cells
    remaining_cells=values.TOTAL_CELLS
    
    go_msg=None
    
    #method to create a cell.
    def __init__(self, x_pos,y_pos, is_mine=False):
        self.is_mine = is_mine
        self.cell_button = None
        self.x=x_pos
        self.y=y_pos
        self.entourage=[]
        self.mines_near=0
        self.is_clicked=False
        self.is_marked=False
        
        Cell.cells.append(self)
        
    
    #method to represent the cell using a button
    def create_button(self,location):
        btn=Button(
            location,
            bg='white',
            width=int(utils.width_ratio(values.BUTTON_X)),
            height=int(utils.height_ratio(values.BUTTON_Y))
        )
        
        btn.bind('<Button-1>',self.on_left_click)
        btn.bind('<Button-3>',self.on_right_click)
        
        self.cell_button=btn

        
        
            
    #boolean method checking if the cell is a corner  
    def is_a_corner(self):
        if(self.x==0):
            if (self.y ==0 or self.y==values.ROWS-1 ):
                return True
            
        elif(self.y==0 and self.x==values.COLUMNS-1 ):
            return True
        
        elif(self.y==values.ROWS-1 and self.x==values.COLUMNS-1):
            return True
        
        return False
    
    #method to terminate the game.called when a mine is clicked          
    def terminate_game(self):
        self.cell_button.configure(bg='red')
        
        for mine in Cell.mines:
            mine.cell_button.configure(bg='red')
            
        game.create_msg('black',"Game Over: \n You Clicked on a Mine!")
        
            
    def congratulate(self):
        game.create_msg('magenta',"Congrats! \n You Avoided All the Mines!")
        
        
     
    #displays the neighboring mines  
    def display_mines(self):
        
        if self.is_clicked:
            self.cell_button.config(relief='sunken')
        
        if not self.is_clicked:
            
            if Cell.remaining_cells!=0:
                self.is_clicked=True
                Cell.remaining_cells-=1
                self.cell_button.config(relief='sunken')
                self.cell_button.config(text=f"{self.mines_near}")
            
                if self.mines_near==0:
                    for n in self.entourage:
                        n.display_mines() 
                
                if Cell.remaining_cells==0:
                    self.congratulate()
        
            
                
                        
        
    
    def on_left_click(self, event):
        
        if self.is_mine: 
            self.terminate_game()
        else:
            self.display_mines()
                    
        
    def on_right_click(self, event):
        
        if self.is_marked:
            self.cell_button.config(bg='white',fg='black')
            self.is_marked=False
        else:
            self.cell_button.config(bg='black',fg='white')
            self.is_marked=True
            
    
    def calculate_mines(self):
        neighbours=[]
        index=values.COLUMNS*self.y+self.x
        mine_count=0
        val=1
        val2=1
        
        if self.is_a_corner():
            if self.y!=0:
                val2=-1
                
            neighbours.append(index+val2*values.COLUMNS)
                
            if(self.x!=0):
                 val=-1
            neighbours.append(index+val)
            neighbours.append(index+val+val2*values.COLUMNS)
        
        elif self.x==0 or self.x==values.COLUMNS-1 or self.y==0 or self.y==values.ROWS-1:
            
            val3=values.COLUMNS
            
            if(self.x!=0 and self.x!=values.COLUMNS-1):
                val3=val
                val=values.COLUMNS
                
            neighbours.append(index+val3)
            neighbours.append(index-val3)
            
            if self.x==values.COLUMNS-1 or self.y==values.ROWS-1:
                val*=-1
                
            neighbours.append(index+val)
            neighbours.append(index+val+val3)
            neighbours.append(index+val-val3)
        
        else:
            for i in range(2):
                if i>0:
                    val=-1
                neighbours.append(index+val)
                neighbours.append(index+val*values.COLUMNS)
                neighbours.append(index+val+values.COLUMNS)
                neighbours.append(index+val-values.COLUMNS)
                    
    
        for n in neighbours:
            if self.cells[n].is_mine:
                mine_count+=1 
            self.entourage.append(self.cells[n])
            #print(f"Added {self.cells[n].x},{self.cells[n].y} to {self.x},{self.y}")
            #print(f"lenght: {len(self.entourage)}")
            
    
        return mine_count; 
    
        
    def __repr__(self):
        return f"{self.is_mine}"
    
    @staticmethod
    def create_time_count_widget(location):
        label=Label(
            location,
            text=f"Remaining Cells: {Cell.remaining_cells}",
            bg=f"{values.get_bg(values.win)}",
            font=(values.FONT,int(values.FONTSIZE))
             
            ) 
        
        Cell.remaining_cells_widget = label
    
    @staticmethod
    def assign_mines():
        Cell.mines=random.sample(Cell.cells,values.MINE_COUNT)
        
        for mine in Cell.mines:
            mine.is_mine=True
            mine.cell_button.config(bg='blue')
        
        for cell in Cell.cells:
            cell.mines_near=cell.calculate_mines()
            
    @staticmethod
    def repr_all():
        for cell in Cell.cells:
            #cell.cell_button.config(text=f"{cell.is_mine}")
            #cell.cell_button.config(text=f"{values.COLUMNS*cell.y+cell.x}")
            print(f"cell {cell.x},{cell.y} has {cell.calculate_mines()} mines" )
            
    
    