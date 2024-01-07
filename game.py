from tkinter import *
import values
import utils
import time 
from cell import Cell
from chrono import Chrono

#Set up values.window
values.win.geometry(f'{values.WIDTH}x{values.HEIGHT}')
values.win.configure(bg="#82C3F8" )
values.win.title('Minesweeper Game')

start_time=None
go_msg=None

def timer(self):
    self.sv.set(self.format_time(time.time()-self.start_time))
    self.after_loop=self.win.after(50,self.timer)


top_frame=Frame(
    values.win,
    bg='#82C3F8',
    width=values.WIDTH,
    height=utils.height_ratio(30)
    )

top_frame.place(x=0,y=0)


left_frame= Frame(
    values.win,
    bg='#82C3F8', 
    width=utils.width_ratio(13),
    height=utils.height_ratio(80)
    
)

left_frame.place(x=0,y=utils.height_ratio(20))

center_frame=Frame(
    values.win,
    bg='#82C3F8',
    width=utils.width_ratio(50),
    height=utils.height_ratio(50),
    
) 

center_frame.place(x=utils.width_ratio(13),y=utils.height_ratio(30))

top_banner=Label(
    top_frame,
    bg='#98B1B4',
    width=utils.width_ratio(10.25),
    height=utils.height_ratio(1.5),
)

top_banner.place(x=utils.width_ratio(13),y=utils.height_ratio(5))

instr_banner=Label(top_banner,bg=values.get_bg(top_banner),font='ariel 10',text=values.INSTRUCTIONS)
instr_banner.place(x=20,y=110)
#center_frame.place(x=utils.calculate_grid_x_pos(),y=utils.calculate_grid_y_pos())


    
def exit_game():
        values.win.quit()
    
def restart():
        load_game()
        
def create_exit_btn(xval,yval,loc,w,h):
        
    exit_button= Button(
            loc,
            text='Exit',
            width=w,
            height=h,
            command=exit_game
            )

    exit_button.place(x=xval,y=yval)
    
def create_restart_btn(xval,yval,loc,w,h):
    
    restart_button= Button(
        loc,
        text='Restart',
        width=w,
        height=h,
        command=restart
        )

    restart_button.place(x=xval,y=yval)

create_exit_btn(20,20,top_banner,8,4)
create_restart_btn(90,20,top_banner,8,4)

def create_msg(color,msg):
    
        global go_msg
    
        go_msg=Label(top_banner, bg=color,fg='white', font=('Arial',9),width= utils.width_ratio(10.25), height=utils.height_ratio(1.5),text=msg)
        go_msg.place(x=0,y=0)
        
        create_exit_btn(160,100,go_msg,8,2)
        create_restart_btn(230,100,go_msg,8,2)
        

def load_game():
   
    global go_msg
    
    if go_msg:
        go_msg.destroy()

    if len(Cell.cells)!=0:
        Cell.cells.clear()
    
    for r in range(values.ROWS):
        for col in range(values.COLUMNS):
            c=Cell(col,r)
            c.create_button(center_frame)
            c.cell_button.grid(
                column=col, row=r) 


    Cell.assign_mines()
    
    

@staticmethod 
def format_time(time_passed):
    minutes=int(time_passed/60)
    seconds=int(time_passed-minutes*60)
        
    return '%02d:%02d' % (minutes,seconds)
    
