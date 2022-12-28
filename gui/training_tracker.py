
import tkinter as tk
from tkinter import font as tkfont

from sqlalchemy.orm import sessionmaker

from gui.design import design_frame
from gui.history import History
from gui.homepage import HomePage
from gui.setup import Setup
from gui.start import Start
from programa import engine


class TrainingTracker(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.session = self.db_conn()


        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, Setup, Start, History):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            design_frame(frame)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")





    def db_conn(self):
        Session = sessionmaker(bind=engine)
        return Session()


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        if page_name == "Start":
            frame.load_row()
        frame.tkraise()
