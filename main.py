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


# #half life duration in hours
# half_life = 10
#
# # Initial GBq on production (10~370 GBq)
# initial_MBq = 15000
#
# print(time.time())
# # production time in hours
# initial_time = 689946120 / 3600
# print(initial_time)
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
#     print('hours passed:', time_passed)
#     current_MBq = initial_MBq * 0.5 ** (time_passed / half_life)
#     print(current_MBq)
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

        def load_csv():
            try:
                import_file_path = tk.filedialog.askopenfilename(initialdir='./DataLog')
                df = pd.read_csv(import_file_path)
                print(df)

                for e in self.actual_info.entries:
                    e.configure(state=tk.NORMAL)
                    e.delete(0, tk.END)
                self.actual_info.company_name_entry.insert(0, string=df['production_company_name'][0])
                self.actual_info.transport_company_entry.insert(0, string=df['transport_company_name'][0])
                self.actual_info.driver_name_entry.insert(0, string=df['transport_driver_name'][0])
                self.actual_info.id_entry.insert(0, string=df['ID'][0])
                self.actual_info.iso_initial_mbq_entry.insert(0, string=df['initial_mBQ'][0])
                self.actual_info.iso_half_life_value_entry.insert(0, string=df['half_life'][0])
                self.actual_info.iso_name_entry.insert(0, string=df['isotope_name'][0])
                self.actual_info.calibration_date_entry.insert(0, string=pd.to_datetime(df['calibration_unix'][0], unit='s').strftime('%d-%m-%Y %H:%M'))
                self.actual_info.arrival_date_entry.insert(0, string=pd.to_datetime(df['arrival_unix'][0], unit='s').strftime('%d-%m-%Y %H:%M'))
                self.actual_info.time_on_load_entry.insert(0, string=datetime.now().strftime('%d-%m-%Y %H:%M'))
                self.actual_info.iso_actual_mbq_entry.insert(0, string='10000')
                for e in self.actual_info.entries:
                    e.configure(state='readonly')
            except FileNotFoundError:
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
            # pulling data from widget entries and joining them together with a '/' as delimiter.
            calibrated_string_date = '/'.join(self.calibration_date_entry.get())
            print(calibrated_string_date)
            arrival_string_date = '/'.join(self.arrival_date_entry.get())
            print(arrival_string_date)
            # transforming joined string dates to unix dates.
            calibrated_unix_date = time.mktime(datetime.strptime(calibrated_string_date, "%d/%m/%Y/%H/%M").timetuple())
            arrival_unix_date = time.mktime(datetime.strptime(arrival_string_date, '%d/%m/%Y/%H/%M').timetuple())
            # setting dict to be saved to csv file.
            d = {'isotope_name': isotope_name,
                 'ID': self.product_info.id_entry.get(),
                 'production_company_name': self.product_info.company_name_entry.get(),
                 'transport_company_name': self.product_info.transport_company_entry.get(),
                 'transport_driver_name': self.product_info.driver_name_entry.get(),
                 'half_life': self.product_info.iso_half_life_value_entry.get(),
                 'initial_mBQ': self.product_info.iso_initial_mbq_entry.get(),
                 'calibration_unix': calibrated_unix_date,
                 'calibration_timestamp': calibrated_string_date,
                 'arrival_unix': arrival_unix_date,
                 'arrival_timestamp': arrival_string_date,
                 'save_date': date.today(),
                 }
            # joins save_path, 'ID' and today's date to be used as file name.
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
        self.data_entry_frame = tk.Frame(parent, borderwidth=3, relief='ridge')
        self.data_entry_frame.grid(column=0, row=0, sticky=tk.NE, ipady=6)

        # Radio buttons frame
        self.radiobuttons = Radiobuttons(parent, data_display=self)
        self.radiobuttons.grid(column=1, row=0, sticky=tk.NE)

        # Product info frame
        self.product_info = ProductInfo(self.data_entry_frame)
        self.product_info.pack(side=tk.TOP)

        # Calibration date entry
        self.calibration_date_entry = DateTimeEntry(self.data_entry_frame, "Calibration date(UTC):")
        self.calibration_date_entry.pack(side=tk.TOP, anchor=tk.W, fill='x')

        # Arrival date entry
        self.arrival_date_entry = DateTimeEntry(self.data_entry_frame, "Arrival date(UTC):")
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

        # load button
        self.load_button = tk.Button(self.data_actual_info, text='Load', borderwidth=3,
                                     overrelief='sunken',
                                     command=load_csv)
        self.load_button.pack(side=tk.BOTTOM, fill='x')

        print('Finished creating widgets.')


if __name__ == "__main__":
    root = tk.Tk()
    app = DataDisplay(root)
    root.title("DataDisplay")
    root.geometry('800x800')
    root.resizable(True, True)
    root.mainloop()
