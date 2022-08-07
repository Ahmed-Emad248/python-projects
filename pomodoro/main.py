import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 2
reps = 0
timer =None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_canvas, text=f"00:00")
    timer_label.config(text="TIMER", font=(FONT_NAME, 30, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
    checkmark.config(text="",font=(FONT_NAME, 14, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps +=1
    work_sec= int(WORK_MIN * 60)
    short_break= int(SHORT_BREAK_MIN * 60)
    long_beak= int(LONG_BREAK_MIN * 60)

    if reps % 2 == 0  :
        count_down(short_break)
        timer_label.config(text="break",font=(FONT_NAME,30,"bold"),fg=PINK,highlightthickness=0,bg=YELLOW)
    elif reps % 8 == 0 :
        count_down(long_beak)
        timer_label.config(text="long break", font=(FONT_NAME, 30, "bold"), fg=RED, highlightthickness=0, bg=YELLOW)
    else:
        count_down(work_sec)
        timer_label.config(text="work", font=(FONT_NAME, 30, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if int(count_sec) < 10 :
        count_sec =f"0{count_sec}"
    if count_min < 10:
        count_min=f"0{count_min}"
    canvas.itemconfig(timer_canvas,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=  window.after(1000,count_down,count - 1)
    else:

        start_count()
        marks = ""
        for _ in range(math.floor(reps/2)) :
                marks += "✔"
        checkmark.config(text=marks,font=(FONT_NAME,14,"bold"),fg=GREEN,highlightthickness=0,bg=YELLOW)

# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
###########################################################################
##########################create label#####################################
timer_label=Label(text="TIMER",font=(FONT_NAME,30,"bold"),fg=GREEN,highlightthickness=0,bg=YELLOW)
timer_label.grid(column=2,row=1)
###########################################################################
#########################background########################################
canvas= Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
background=PhotoImage(file="tomato.png")
canvas.create_image(100,110,image=background)
timer_canvas=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,24,"bold"))
canvas.grid(column=2,row=3)
#############################################################################
#####################start button############################################
start=Button(text="start",command=start_count,highlightthickness=0)
start.grid(column=1,row=4)
############################################################################
#####################reset button###########################################
reset=Button(text="reset",command=reset_timer,highlightthickness=0)
reset.grid(column=3,row=4)
###########################################################################
###########################checkmark label#################################
checkmark=Label(font=(FONT_NAME,14,"bold"),fg=GREEN,highlightthickness=0,bg=YELLOW)
checkmark.grid(column=2,row=4)
window.mainloop()
