import tkinter as tk

from gui.design import design_button_main


class HomePage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Training Tracker", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button_setup = tk.Button(self, text="Training Setup",
                            command=lambda: controller.show_frame("Setup"))
        design_button_main(button_setup)


        button_starter = tk.Button(self, text="Start Training",
                            command=lambda: controller.show_frame("Start"))
        design_button_main(button_starter)
        button_history = tk.Button(self, text="History",
                            command=lambda: controller.show_frame("History"))
        design_button_main(button_history)
        button_setup.pack()
        button_starter.pack()
        button_history.pack()