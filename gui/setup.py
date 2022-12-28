import tkinter as tk

from sqlalchemy.orm.exc import UnmappedInstanceError

from programa import Programa


class Setup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.row_count = 1
        label = tk.Label(self, text="Training Setup", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Ok",
                           command=lambda: controller.show_frame("HomePage"))


        self.lentele = tk.Frame(self)

        pratimas = tk.Label(self.lentele, text="Pratimas")
        serijos = tk.Label(self.lentele, text="Serijos")
        pakartojimai = tk.Label(self.lentele, text="Pakartojimai")

        self.add = tk.Button(self.lentele, text="Add New", command=self.add_row)
        self.add.grid(row=2, column=1)

        records = self.controller.session.query(Programa).all()
        if len(records) > 0:
            for record in records:
                self.add_row(record)


        pratimas.grid(row=0, column=1)
        serijos.grid(row=0, column=2)
        pakartojimai.grid(row=0, column=3)




        self.lentele.pack()
        button.pack()



    def add_row(self, record=Programa("", 0, 0)):
        entry_pratimas = tk.Entry(self.lentele)
        entry_serijos = tk.Entry(self.lentele)
        entry_pakartojimai = tk.Entry(self.lentele)

        entry_serijos.insert(0, record.serijos)
        entry_pratimas.insert(0, record.pratimas)
        entry_pakartojimai.insert(0, record.pakartojimai)

        remove = tk.Button(self.lentele, text="Remove", command=lambda: self.remove_row(record.id, entry_pratimas, entry_serijos,
                                                                                        entry_pakartojimai, remove))

        entry_pratimas.grid(row=self.row_count, column=1)
        entry_serijos.grid(row=self.row_count, column=2)
        entry_pakartojimai.grid(row=self.row_count, column=3)
        remove.grid(row=self.row_count, column=4)

        self.row_count += 1
        self.add.grid(row=self.row_count)
        self.add.config(command=lambda: self.insert_record(record, entry_pratimas, entry_serijos, entry_pakartojimai))


    def remove_row(self, id, pratimas, serijos, pakartojimai, remove):
        try:
            remove_row = self.controller.session.query(Programa).get(id)
            self.controller.session.delete(remove_row)
            self.controller.session.commit()
        except UnmappedInstanceError:
            pass


        pratimas.grid_remove()
        serijos.grid_remove()
        pakartojimai.grid_remove()
        remove.grid_remove()

    def insert_record(self, record, entry_pratimas, entry_serijos, entry_pakartojimai):
        record.pratimas = entry_pratimas.get()
        record.serijos = int(entry_serijos.get())
        record.pakartojimai = int(entry_pakartojimai.get())
        self.controller.session.add(record)
        self.controller.session.commit()
        self.add_row(Programa("", 0, 0))



