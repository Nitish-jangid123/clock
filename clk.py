from time import strftime, sleep
from tkinter import Label, Tk

window = Tk()
window.title("Digital Clock")
window.geometry("200x80")
window.configure(bg="black")
window.resizable(False, False)

clock_label = Label(window, bg="black", fg="white", font=("Times", 30, 'bold'), relief='flat')
clock_label.place(x=20, y=20)

running = True  # Global variable to control the loop

def stop_program():
    global running
    running = False

def updating_label():
    global running
    if not running:
        window.destroy()
        return

    current_time = strftime('%H:%M:%S')
    clock_label.configure(text=current_time)
    window.after(1000, updating_label)  # Call updating_label() after 1000ms (1 second)

# Bind the stop_program function to the window close button
window.protocol("WM_DELETE_WINDOW", stop_program)

updating_label()
window.mainloop()

