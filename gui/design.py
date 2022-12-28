from tkinter import font as tkfont


def design_button_main(button):
    button.config(font=tkfont.Font(family='Helvetica', size=18),bg='White', bd=10)
    button.config(height=3, width=15)
def design_button_setup(button):
    pass


def design_frame(frame):
    frame.config(bg="Black")

def design_button_correct(button):
    button.config(bg='Green')



def design_button_wrong(button):
    button.config(bg='Red')