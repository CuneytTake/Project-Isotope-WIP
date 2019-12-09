import time
import tkinter as tk
import os
import datetime
from datetime import date
import csv
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from matplotlib.figure import Figure
from datetime import datetime, timedelta
import numpy as np


# Molybdenum99:
# #half life duration in hours
# half_life = 66
#
# # Initial GBq on production (10~370 GBq)
# initial_GBq = 100
#
# # production time in hours
# initial_time = time.time() / 3600
#
# # def every(delay, task):
# #
# #     next_time = time.time() + delay
# #     while True:
# #         time.sleep(max(0, next_time - time.time()))
# #         try:
# #             task()
# #         except Exception:
# #             traceback.print_exc()
# #         # skip tasks if we are behind schedule:
# #         next_time += (time.time() - next_time) // delay * delay + delay
#
# def calc_gbq():
#     time_now = time.time() / 3600
#     time_passed = time_now - initial_time
#     current_GBq = initial_GBq * 0.5 ** (time_passed / half_life)
#     print(current_GBq)
#
# # Runs function on a seperate thread, every second.
# calc_gbq()
# # threading.Thread(target=lambda: every(1, calc_gbq)).start()


class DataDisplay(tk.Frame):
    """ Provides the GUI, powered by the Tkinter module. """

    def __init__(self, parent):
        super().__init__()
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.grid()
        self.create_widgets(parent)

    def create_widgets(self, parent):
        print("Creating widgets... ")

        def save_data():
            # If radio button choice '1', Molybdenum-99:
            if self.radiobuttons.get() == 1:
                # Creates path if it doesn't exist and saves station data per station, in CSV format.
                save_path = './DataLog/Molybdenum99'
                try:
                    os.makedirs(save_path)
                    save(save_path)
                except FileExistsError:
                    # directory already exists
                    save(save_path)

            if self.radiobuttons.get() == 2:
                # Creates path if it doesn't exist and saves station data per station, in CSV format.
                save_path = './DataLog/Technetium99M'
                try:
                    os.makedirs(save_path)
                    save(save_path)
                except FileExistsError:
                    # directory already exists
                    save(save_path)

        def save(save_path):
            string_date = '/'.join(self.calibration_date_entry.get())
            print(string_date)

            unix_date = time.mktime(datetime.strptime(string_date, "%d/%m/%Y/%H/%M").timetuple())
            d = {'ID': self.product_info.id_entry.get(),
                 'production_company_name': self.product_info.company_name_entry.get(),
                 'half_life': self.product_info.iso_half_life_value_label.get(),
                 'initial_GBq': self.product_info.iso_initial_gbq_entry.get(),
                 'calibration_unix': unix_date,
                 'calibration_timestamp': string_date,
                 'save_date': date.today(),
                 }
            file_name = os.path.join(save_path, d['ID'] + ' ' + str(date.today()))
            with open(file_name + '.csv', 'a') as f:
                w = csv.DictWriter(f, d.keys())
                if f.tell() == 0:
                    w.writeheader()
                    w.writerow(d)
                    print('first line in file, writing headers..')
                    print('writing rows..')
                else:
                    w.writerow(d)
                    print('file has headers, writing rows..')

        # Radio buttons frame
        self.radiobuttons = Radiobuttons(parent, data_display=self)
        self.radiobuttons.grid(column=1, row=0, sticky=tk.NE)

        # ID, calibration date, arrival date frame.
        self.data_entry_frame = tk.Frame(parent, borderwidth=3, relief='ridge', width=300)
        self.data_entry_frame.grid(column=0, row=0, sticky=tk.NE, ipady=6)

        # Producer info frame

        self.product_info = ProductInfo(self.data_entry_frame)
        self.product_info.pack(side=tk.TOP)

        # Calibration date entry
        self.calibration_date_entry = DateTimeEntry(self.data_entry_frame, "Calibration date:", 1, 1, 2019, 0, 0)
        self.calibration_date_entry.pack(side=tk.TOP, anchor=tk.W, fill='x')
        # Arrival date entry
        self.arrival_date_entry = DateTimeEntry(self.data_entry_frame, "Arrival date:", 1, 1, 2019, 0, 0)
        self.arrival_date_entry.pack(side=tk.TOP, anchor=tk.W, fill='x')
        # Calibration date 'OK'
        self.calibration_ok_button = tk.Button(self.data_entry_frame, text='Save to CSV', borderwidth=3, overrelief='sunken',
                                          command=lambda: save_data())
        self.calibration_ok_button.pack(side=tk.TOP, anchor=tk.W, fill='both', expand=True)

        print('Finished creating widgets.')


class Radiobuttons(tk.Frame):
    def __init__(self, parent, data_display):
        super().__init__(parent)

        # Inserts becquerel value to label
        def insert_becquerel():
            v = self.radio.get()
            becquerel = 0
            if v == 1:
                becquerel = 26.83
                print('half-life value of Holmium-166 is: ' + str(becquerel))
            elif v == 2:
                becquerel = 1771.68
                print('half-life value of Iridium-192 is: ' + str(becquerel))
            elif v == 3:
                becquerel = 1425.12
                print('half-life value of Jodium-125 is: ' + str(becquerel))
            elif v == 4:
                becquerel = 192.48
                print('half-life value of Jodium-131 is: ' + str(becquerel))
            elif v == 5:
                becquerel = 159.36
                print('half-life value of Lutetium-177 is: ' + str(becquerel))
            elif v == 6:
                becquerel = 65.94
                print('half-life value of Molybdenum-99 is: ' + str(becquerel))
            elif v == 7:
                becquerel = 1212.00
                print('half-life value of Strontium-89 is: ' + str(becquerel))
            elif v == 8:
                becquerel = 6.01
                print('half-life value of Technetium-99M is: ' + str(becquerel))
            elif v == 9:
                becquerel = 125.88
                print('half-life value of Xenon-133 is: ' + str(becquerel))
            elif v == 10:
                becquerel = 63.84
                print('half-life value of Yttrium-90 is: ' + str(becquerel))
            # Temporarily sets the state on the label to 'normal', otherwise unable to insert() a string.
            # After insert, sets state back to 'readonly'
            data_display.product_info.iso_half_life_value_label.configure(state=tk.NORMAL)
            data_display.product_info.iso_half_life_value_label.delete(0, 20)
            data_display.product_info.iso_half_life_value_label.insert(0, becquerel)
            data_display.product_info.iso_half_life_value_label.configure(state='readonly')

        # Setting border-width and border-type
        self.configure(borderwidth=3, relief='ridge')
        # Setting self.radio to be an integer for function use.
        self.radio = tk.IntVar()
        # Defining radio-buttons
        rb = tk.Radiobutton(self, text='Holmium-166', variable=self.radio, value=1, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: [print('Radiobutton selected Holmium-166'), insert_becquerel()])
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Iridium-192', variable=self.radio, value=2, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: [print('Radiobutton selected Iridium-192'), insert_becquerel()])
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Jodium-125', variable=self.radio, value=3, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: [print('Radiobutton selected Jodium-125'), insert_becquerel()])
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Jodium-131', variable=self.radio, value=4, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: [print('Radiobutton selected Jodium-131'), insert_becquerel()])
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Lutetium-177', variable=self.radio, value=5, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: [print('Radiobutton selected Lutetium-177'), insert_becquerel()])
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Molybdenum-99', variable=self.radio, value=6, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: [print('Radiobutton selected Molybdenum-99'), insert_becquerel()])
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Strontium-89', variable=self.radio, value=7, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: [print('Radiobutton selected Strontium-89'), insert_becquerel()])
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Technetium-99M', variable=self.radio, value=8, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: [print('Radiobutton selected Technetium-99M'), insert_becquerel()])
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Xenon-133', variable=self.radio, value=9, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: [print('Radiobutton selected Xenon-133'), insert_becquerel()])
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Yttrium-90', variable=self.radio, value=10, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: [print('Radiobutton selected Yttrium-90'), insert_becquerel()])
        rb.pack(side=tk.LEFT, anchor=tk.W)

    def get(self):
        return self.radio.get()


class DateTimeEntry(tk.Frame):
    def __init__(self, parent, label, day=1, month=1, year=2000, hour=0, minute=0):
        super().__init__(parent)
        # Labels
        date_label = tk.Label(self, text=label)
        label_0 = tk.Label(self, text='DD/MM/YY:')
        label_1 = tk.Label(self, text='/', borderwidth=0)
        label_2 = tk.Label(self, text='/', borderwidth=0)
        label_3 = tk.Label(self, text='HH:MM', borderwidth=0)
        label_4 = tk.Label(self, text=':', borderwidth=0)
        # Entries
        self.entry_day = tk.Entry(self, width=2, borderwidth=1)
        self.entry_month = tk.Entry(self, width=2, borderwidth=1)
        self.entry_year = tk.Entry(self, width=4, borderwidth=1)
        self.entry_hour = tk.Entry(self, width=2, borderwidth=1)
        self.entry_minute = tk.Entry(self, width=2, borderwidth=1)

        # Listing entries for function use
        self.entries = [self.entry_day, self.entry_month, self.entry_year, self.entry_hour, self.entry_minute]
        # binds key release to a function
        self.entry_day.bind('<KeyRelease>', lambda e: self._check(0, 2))
        self.entry_month.bind('<KeyRelease>', lambda e: self._check(1, 2))
        self.entry_year.bind('<KeyRelease>', lambda e: self._check(2, 4))
        self.entry_hour.bind('<KeyRelease>', lambda e: self._check(3, 2))
        self.entry_minute.bind('<KeyRelease>', lambda e: self._check(4, 2))

        # Space management
        date_label.pack(side=tk.TOP, fill="x")
        label_0.pack(side=tk.LEFT)
        self.entry_day.pack(side=tk.LEFT)
        label_1.pack(side=tk.LEFT)
        self.entry_month.pack(side=tk.LEFT)
        label_2.pack(side=tk.LEFT)
        self.entry_year.pack(side=tk.LEFT)
        label_3.pack(side=tk.LEFT)
        self.entry_hour.pack(side=tk.LEFT)
        label_4.pack(side=tk.LEFT)
        self.entry_minute.pack(side=tk.LEFT)

    def get(self):
        return [e.get() for e in self.entries]

    def reset(self):
        self.entry_day.delete(0, "end")
        self.entry_month.delete(0, "end")
        self.entry_year.delete(0, "end")
        self.entry_hour.delete(0, "end")
        self.entry_minute.delete(0, "end")

    def _backspace(self, entry):
        cont = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, cont[:-1])

    def _check(self, index, size):
        entry = self.entries[index]
        next_index = index + 1
        next_entry = self.entries[next_index] if next_index < len(self.entries) else None
        data = entry.get()
        if len(data) > size or not data.isdigit():
            self._backspace(entry)
        if len(data) >= size and next_entry:
            next_entry.focus()


class ProductInfo(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # company name label and entry
        self.company_name_label = tk.Label(self, text='Production Company name:', anchor=tk.W)
        self.company_name_entry = tk.Entry(self)
        # transport company label and entry
        self.transport_company_label = tk.Label(self, text='Transport Company name:', anchor=tk.W)
        self.transport_company_entry = tk.Entry(self)
        # transport driver label and entry
        self.driver_name_label = tk.Label(self, text='Transport Driver name:', anchor=tk.W)
        self.driver_name_entry = tk.Entry(self)
        # ID Entry and label for the isotope
        self.id_entry_label = tk.Label(self, text='Isotope ID name:')
        self.id_entry = tk.Entry(self, text='Enter ID for the isotope to be saved:')
        self.iso_half_life_label = tk.Label(self, text='Half-life:')
        self.iso_half_life_value_label = tk.Entry(self, state='readonly')
        self.iso_initial_gbq_label = tk.Label(self, text='Initial Becquerel in GBq:')
        self.iso_initial_gbq_entry = tk.Entry(self)

        # space management for labels
        self.company_name_label.grid(column=0, row=0, sticky=tk.W)
        self.transport_company_label.grid(column=0, row=1, sticky=tk.W)
        self.driver_name_label.grid(column=0, row=2, sticky=tk.W)
        self.id_entry_label.grid(column=0, row=3, sticky=tk.W)
        self.iso_half_life_label.grid(column=0, row=5, sticky=tk.W)
        self.iso_initial_gbq_label.grid(column=0, row=4, sticky=tk.W)

        # space management for entries
        self.company_name_entry.grid(column=1, row=0)
        self.transport_company_entry.grid(column=1, row=1)
        self.driver_name_entry.grid(column=1, row=2)
        self.id_entry.grid(column=1, row=3)
        self.iso_half_life_value_label.grid(column=1, row=5)
        self.iso_initial_gbq_entry.grid(column=1, row=4)

    def get(self):
        return self.id_entry.get()


if __name__ == "__main__":
    root = tk.Tk()
    app = DataDisplay(root)
    root.title("DataDisplay")
    root.geometry('800x800')
    root.resizable(True, True)
    root.mainloop()
