import time
import tkinter as tk
import os
import datetime
from datetime import date
import csv


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

    @staticmethod
    def create_widgets(parent):
        print("Creating widgets... ")

        def save_data():
            # If radio button choice '1', Molybdenum-99:
            if radiobuttons.get() == 1:
                # Creates path if it doesn't exist and saves station data per station, in CSV format.
                save_path = './DataLog/Molybdenum99'
                try:
                    os.makedirs(save_path)
                    save(save_path)
                except FileExistsError:
                    # directory already exists
                    save(save_path)

            if radiobuttons.get() == 2:
                # Creates path if it doesn't exist and saves station data per station, in CSV format.
                save_path = './DataLog/Technetium99M'
                try:
                    os.makedirs(save_path)
                    save(save_path)
                except FileExistsError:
                    # directory already exists
                    save(save_path)

        def save(save_path):
            string_date = '/'.join(calibration_date_entry.get())
            print(string_date)

            unix_date = time.mktime(datetime.datetime.strptime(string_date, "%d/%m/%Y/%H/%M").timetuple())
            d = {'ID': product_info.id_entry.get(),
                 'production_company_name': product_info.company_name_entry.get(),
                 'half_life': product_info.iso_half_life_value_label.get(),
                 'initial_GBq': product_info.iso_initial_gbq_entry.get(),
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
        radiobuttons = Radiobuttons(parent)
        radiobuttons.grid(column=1, row=0, sticky=tk.NE)

        # ID, calibration date, arrival date frame.
        data_entry_frame = tk.Frame(parent, borderwidth=3, relief='ridge')
        data_entry_frame.grid(column=0, row=0, sticky=tk.NE)

        # Producer info frame
        product_info = ProductInfo(data_entry_frame)
        product_info.pack(side=tk.TOP)

        # Calibration date entry
        calibration_date_entry = DateTimeEntry(data_entry_frame, "Calibration date:", 1, 1, 2019, 0, 0)
        calibration_date_entry.pack(side=tk.TOP, anchor=tk.W, fill='x')
        # Arrival date entry
        arrival_date_entry = DateTimeEntry(data_entry_frame, "Arrival date:", 1, 1, 2019, 0, 0)
        arrival_date_entry.pack(side=tk.TOP, anchor=tk.W, fill='x')
        # Calibration date 'OK'
        calibration_ok_button = tk.Button(data_entry_frame, text='Save to CSV', borderwidth=3, overrelief='sunken',
                                          command=lambda: save_data())
        calibration_ok_button.pack(side=tk.TOP, anchor=tk.W, fill='x')


class Radiobuttons(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Setting border-width and border-type
        self.configure(borderwidth=3, relief='ridge')
        # Setting self.radio to be an integer for function use.
        self.radio = tk.IntVar()
        # Defining radio-buttons
        rb = tk.Radiobutton(self, text='Molybdenum-99', variable=self.radio, value=1, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: print('Radiobutton selected Molybdenum99M'))
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Technetium-99M', variable=self.radio, value=2, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: print('Radiobutton selected Technetium99M'))
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Xenon-133', variable=self.radio, value=3, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: print('Radiobutton selected Xenon-133'),
                            state=tk.DISABLED)
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Holmium-166', variable=self.radio, value=4, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: print('Radiobutton selected Holmium-166'),
                            state=tk.DISABLED)
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Lutetium-177', variable=self.radio, value=5, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: print('Radiobutton selected Lutetium-177'),
                            state=tk.DISABLED)
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Jodium-125', variable=self.radio, value=6, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: print('Radiobutton selected Jodium-125'),
                            state=tk.DISABLED)
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Iridium-192', variable=self.radio, value=7, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: print('Radiobutton selected Iridium-192'),
                            state=tk.DISABLED)
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Strontium-89', variable=self.radio, value=8, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: print('Radiobutton selected Jodium-131'),
                            state=tk.DISABLED)
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Jodium-131', variable=self.radio, value=9, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: print('Radiobutton selected Strontium-89'),
                            state=tk.DISABLED)
        rb.pack(anchor=tk.W)
        rb = tk.Radiobutton(self, text='Yttrium-90', variable=self.radio, value=10, indicatoron=0,
                            width=15, overrelief='sunken',
                            command=lambda: print('Radiobutton selected Yttrium-90'),
                            state=tk.DISABLED)
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
        self.iso_half_life_value_label = tk.Entry(self)
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


print('Finished creating widgets.')

if __name__ == "__main__":
    root = tk.Tk()
    app = DataDisplay(root)
    root.title("DataDisplay")
    root.geometry('800x800')
    root.resizable(True, True)
    root.mainloop()
