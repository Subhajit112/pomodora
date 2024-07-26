from tkinter import *
import math
#global variables
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
#code start

#functions

def countdown_reset():
    pass
    
def countdown_start():
    global reps
    reps +=1
    short_break_sec = 2
    work_sec = 5
    long_break_sec = 2
    if reps % 2 != 0:
        countdown(work_sec)
        mylable.config(text= "WORK", fg= GREEN)
    if reps % 2 == 0:
        countdown(short_break_sec)
        mylable.config(text= "BREAK", fg= PINK)
    if reps % 8 == 0:
        countdown(long_break_sec)
        mylable.config(text= "BREAK", fg= RED)



def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text = f"{"%02d" % count_min}:{"%02d" % count_sec}")
    if count > 0:
        window.after(1000, countdown, count-1)
    else:
        countdown_start()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        checkmark.config(text=mark)
    
 
    
window = Tk()
window.title("Pomodora")
window.config(padx = 50, pady = 50, bg = YELLOW)
mylable = Label(text = "TIMER", font = ("Arial", 24, "bold"), fg = GREEN, bg = YELLOW)
mylable.grid(row = 0, column = 2)
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato = PhotoImage(file = "tomato.png")
canvas.create_image(100, 108, image = tomato)
timer_text = canvas.create_text(103, 130, text = "00:00", font = (FONT_NAME, 25, "bold"))
canvas.grid(row = 2, column = 2)
start_button = Button(text = "START", highlightthickness = 0, command = countdown_start)
start_button.grid(row = 3, column = 0)
reset_button = Button(text = "RESET", highlightthickness = 0, command= countdown_reset)
reset_button.grid(row = 3, column = 3)
checkmark = Label( fg = "black")
checkmark.grid(row = 3, column = 2)


window.mainloop()
