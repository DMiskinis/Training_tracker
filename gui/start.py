import datetime
import tkinter as tk

from gui.design import design_button_correct, design_button_wrong
from programa import Programa, Istorija


class Start(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.row_count = 1
        label = tk.Label(self, text="Started Training", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Ok",
                           command=lambda: controller.show_frame("HomePage"))

        self.lentele = tk.Frame(self)




        self.load_row()
        self.lentele.pack()
        button.pack()


    # Uzkrauname treniruociu programos irasus
    def load_row(self):

        # Isvalome esancius irasus
        for widget in self.lentele.winfo_children():
            widget.destroy()

        # Sukuriame lenteles stulpeliu pavadinimus
        pratimas = tk.Label(self.lentele, text="Pratimas")
        serijos = tk.Label(self.lentele, text="Serijos")
        pakartojimai = tk.Label(self.lentele, text="Pakartojimai")

        # Lenteles stulpeliu pavadinimus isdeliojame grid'o pagalba
        pratimas.grid(row=0, column=1)
        serijos.grid(row=0, column=2)
        pakartojimai.grid(row=0, column=3)

        # Pasiimame visus issaugotus pratimus is duomenu bazes
        records = self.controller.session.query(Programa).all()

        # Patikrinam ar yra issaugotas bent vienas pratimas
        if len(records) == 0:
            label_empty = tk.Label(self.lentele, text="Treniruociu programa nesukurta")
            label_empty.grid(row=self.row_count, column=1)
            return

        # Atvaizduojam kiekviena irasa metodo add_row pagalba
        for record in records:
            self.add_row(record)

    # Atvaizduojam kiekviena irasa
    def add_row(self, record):

        # Iraso elementams sukuriame label'ius
        label_pratimas = tk.Label(self.lentele, text=record.pratimas)
        label_serijos = tk.Label(self.lentele, text=record.serijos)
        label_pakartojimai = tk.Label(self.lentele, text=record.pakartojimai)

        # Sukuriame mygtukus pratimo valdymui (ivygdyti arba praleisti)
        button_done = tk.Button(self.lentele, text="Done")
        button_skip = tk.Button(self.lentele, text="Skip")

        # Sukonfiguruojame valdymo mygtuku komandas
        button_done.config(command=lambda: self.remove_row(record, "Done", label_pratimas, label_serijos, label_pakartojimai, button_done, button_skip))
        button_skip.config(
            command=lambda: self.remove_row(record, "Skip", label_pratimas, label_serijos, label_pakartojimai,
                                            button_done, button_skip))
        # Pritaikome mygtuku dizaina
        design_button_correct(button_done)
        design_button_wrong(button_skip)

        # Isdeliojam elementus grid'o pagalba
        label_pratimas.grid(row=self.row_count, column=1)
        label_serijos.grid(row=self.row_count, column=2)
        label_pakartojimai.grid(row=self.row_count, column=3)

        button_done.grid(row=self.row_count, column=4)
        button_skip.grid(row=self.row_count, column=5)

        # Padidame lenteles eiluciu count'erio reiksme
        self.row_count += 1

    # Istrinam eilutes elementus
    def remove_row(self, record, atlikta, pratimas, serijos, pakartojimai, done, skip):

        self.insert_record(record, atlikta)

        pratimas.grid_remove()
        serijos.grid_remove()
        pakartojimai.grid_remove()
        done.grid_remove()
        skip.grid_remove()

    # Issaugome pratimo atlikimo statusa duomenu bazeje
    def insert_record(self, record, atlikta):

        self.controller.session.add(Istorija(record.pratimas, record.serijos, record.pakartojimai, datetime.datetime.now(), atlikta))
        self.controller.session.commit()











