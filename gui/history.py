import datetime
import tkinter as tk

from programa import Istorija


class History(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.row_count = 1
        self.controller = controller
        label = tk.Label(self, text="History", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Ok",
                           command=lambda: controller.show_frame("HomePage"))

        label_data = tk.Label(self, text="Data")
        options = self.load_dates()
        selected_date = tk.StringVar()
        selected_date.set("Select Date")
        dropdown_dates = tk.OptionMenu(self, selected_date, *options, command=lambda event: self.load_row(selected_date.get()))

        self.lentele = tk.Frame(self)





        label_data.pack()
        dropdown_dates.pack()
        self.lentele.pack()
        button.pack()

    def load_dates(self):
        dates = []
        for value in self.controller.session.query(Istorija.data).distinct():
            date = value[0].strftime('%Y-%m-%d')
            if date not in dates:
                dates.append(date)

        return dates

    def load_row(self, data):
        d = datetime.datetime.strptime(data, '%Y-%m-%d')

        for widget in self.lentele.winfo_children():
            widget.destroy()
        pratimas = tk.Label(self.lentele, text="Pratimas")
        serijos = tk.Label(self.lentele, text="Serijos")
        pakartojimai = tk.Label(self.lentele, text="Pakartojimai")
        atlikta = tk.Label(self.lentele, text="Atlikta")

        pratimas.grid(row=0, column=1)
        serijos.grid(row=0, column=2)
        pakartojimai.grid(row=0, column=3)
        atlikta.grid(row=0, column=4)

        records = self.controller.session.query(Istorija).filter(Istorija.data > d,
                                                                 Istorija.data < d + datetime.timedelta(days=1))

        if records.first() is None:
            label_empty = tk.Label(self.lentele, text="Treniruociu istorijos nera")
            label_empty.grid(row=self.row_count, column=1)
            return

        for record in records:
            self.add_row(record)


    def add_row(self, record):
        label_pratimas = tk.Label(self.lentele, text=record.pratimas)
        label_serijos = tk.Label(self.lentele, text=record.serijos)
        label_pakartojimai = tk.Label(self.lentele, text=record.pakartojimai)
        label_atlikta = tk.Label(self.lentele, text=record.atlikta)


        label_pratimas.grid(row=self.row_count, column=1)
        label_serijos.grid(row=self.row_count, column=2)
        label_pakartojimai.grid(row=self.row_count, column=3)
        label_atlikta.grid(row=self.row_count, column=4)


        self.row_count += 1




