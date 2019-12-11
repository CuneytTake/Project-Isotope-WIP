import time
import tkinter as tk
import tkinter.ttk as ttk
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
from widgets import Radiobuttons, DateTimeEntry, ProductInfo, ProductActualInfo


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
        # save_path placeholder to prevent losing data
        self.save_path = './DataLog/bin'
        self.isotope_name = 'None'

        def load_data():
            pass

        def save_data():
            save_path = self.save_path
            isotope_name = self.isotope_name
            try:
                # directory does not exist, creates dir
                os.makedirs(save_path)
                save(save_path, isotope_name)
            except FileExistsError:
                # directory already exists.
                save(save_path, isotope_name)

        def save(save_path, isotope_name):
            string_date = '/'.join(self.calibration_date_entry.get())
            print(string_date)

            unix_date = time.mktime(datetime.strptime(string_date, "%d/%m/%Y/%H/%M").timetuple())
            d = {'isotope-name': isotope_name,
                 'ID': self.product_info.id_entry.get(),
                 'production_company_name': self.product_info.company_name_entry.get(),
                 'half_life': self.product_info.iso_half_life_value_label.get(),
                 'initial_mBQ': self.product_info.iso_initial_mbq_entry.get(),
                 'calibration_unix': unix_date,
                 'calibration_timestamp': string_date,
                 'save_date': date.today(),
                 }
            file_name = os.path.join(save_path, d['ID'] + ' ' + str(date.today()))
            if os.path.exists(file_name):
                print('test')
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

        """ Registration frame """
        # ID, calibration date, arrival date frame.
        self.data_entry_frame = tk.Frame(parent, borderwidth=3, relief='ridge', width=300)
        self.data_entry_frame.grid(column=0, row=0, sticky=tk.NE, ipady=6)

        # Radio buttons frame
        self.radiobuttons = Radiobuttons(parent, data_display=self)
        self.radiobuttons.grid(column=1, row=0, sticky=tk.NE)

        # Product info frame
        self.product_info = ProductInfo(self.data_entry_frame)
        self.product_info.pack(side=tk.TOP)

        # Calibration date entry
        self.calibration_date_entry = DateTimeEntry(self.data_entry_frame, "Calibration date:")
        self.calibration_date_entry.pack(side=tk.TOP, anchor=tk.W, fill='x')

        # Arrival date entry
        self.arrival_date_entry = DateTimeEntry(self.data_entry_frame, "Arrival date:")
        self.arrival_date_entry.pack(side=tk.TOP, anchor=tk.W, fill='x')
        # save button
        self.save_button = tk.Button(self.data_entry_frame, text='Save', borderwidth=3,
                                     overrelief='sunken',
                                     command=lambda: save_data())
        self.save_button.pack(side=tk.BOTTOM, fill='both', expand=True)

        """ Actual info frame """
        self.data_actual_info = tk.Frame(parent, borderwidth=3, relief='ridge', width=300)
        self.data_actual_info.grid(column=2, row=0, sticky=tk.NE)
        # Product actual info
        self.actual_info = ProductActualInfo(self.data_actual_info)
        self.actual_info.pack(side=tk.TOP)
        # product calibration and arrival date info
        self.calibration_date = DateTimeEntry(self.data_actual_info, "Calibration date: ")
        self.calibration_date.pack(side=tk.TOP, anchor=tk.W, fill='x')
        #
        self.arrival_date = DateTimeEntry(self.data_actual_info, "Arrival date: ")
        self.arrival_date.pack(side=tk.TOP, anchor=tk.W, fill='x')

        for entry in self.calibration_date.entries:
            entry.configure(state='readonly')
        for entry in self.arrival_date.entries:
            entry.configure(state='readonly')

        # load button
        self.load_button = tk.Button(self.data_actual_info, text='Load', borderwidth=3,
                                     overrelief='sunken',
                                     command=None)
        self.load_button.pack(side=tk.BOTTOM, fill='x')

        print('Finished creating widgets.')


if __name__ == "__main__":
    root = tk.Tk()
    app = DataDisplay(root)
    root.title("DataDisplay")
    root.geometry('800x800')
    root.resizable(True, True)
    root.mainloop()
