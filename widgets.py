""" Tkinter Widgets module """

import tkinter as tk

class ProductActualInfo(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # company name label and entry
        self.company_name_label = tk.Label(self, text='Production Company name:', anchor=tk.W)
        self.company_name_entry = tk.Entry(self, state='readonly')
        # transport company label and entry
        self.transport_company_label = tk.Label(self, text='Transport Company name:', anchor=tk.W)
        self.transport_company_entry = tk.Entry(self, state='readonly')
        # transport driver label and entry
        self.driver_name_label = tk.Label(self, text='Transport Driver name:', anchor=tk.W)
        self.driver_name_entry = tk.Entry(self, state='readonly')
        # ID Entry and label for the isotope
        self.id_entry_label = tk.Label(self, text='Isotope ID:')
        self.id_entry = tk.Entry(self, state='readonly')
        # isotope half life label and entry
        self.iso_half_life_label = tk.Label(self, text='Half-life:')
        self.iso_half_life_value_entry = tk.Entry(self, state='readonly')
        # isotope initial gbq label and entry
        self.iso_initial_gbq_label = tk.Label(self, text='Initial Becquerel in mBQ:')
        self.iso_initial_gbq_entry = tk.Entry(self, state='readonly')
        # isotope actual gbq value label and entry
        self.iso_actual_mbq_label = tk.Label(self, text='Actual mBQ: ')
        self.iso_actual_mbq_entry = tk.Entry(self, state='readonly')

        # space management for labels
        self.company_name_label.grid(column=0, row=0, sticky=tk.W)
        self.transport_company_label.grid(column=0, row=1, sticky=tk.W)
        self.driver_name_label.grid(column=0, row=2, sticky=tk.W)
        self.id_entry_label.grid(column=0, row=3, sticky=tk.W)
        self.iso_initial_gbq_label.grid(column=0, row=4, sticky=tk.W)
        self.iso_half_life_label.grid(column=0, row=5, sticky=tk.W)
        self.iso_actual_mbq_label.grid(column=0, row=6, sticky=tk.W)

        # space management for entries
        self.company_name_entry.grid(column=1, row=0)
        self.transport_company_entry.grid(column=1, row=1)
        self.driver_name_entry.grid(column=1, row=2)
        self.id_entry.grid(column=1, row=3)
        self.iso_initial_gbq_entry.grid(column=1, row=4)
        self.iso_half_life_value_entry.grid(column=1, row=5)
        self.iso_actual_mbq_entry.grid(column=1, row=6)

    def get(self):
        return self.id_entry.get()


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
        self.id_entry_label = tk.Label(self, text='Isotope ID:')
        self.id_entry = tk.Entry(self, text='Enter ID for the isotope to be saved:')
        # isotope initial mbq label and entry
        self.iso_initial_mbq_label = tk.Label(self, text='Initial Becquerel in mBQ:')
        self.iso_initial_mbq_entry = tk.Entry(self)
        # isotope half life label and entry
        self.iso_half_life_label = tk.Label(self, text='Half-life:')
        self.iso_half_life_value_label = tk.Entry(self, state='readonly')

        # space management for labels
        self.company_name_label.grid(column=0, row=0, sticky=tk.W)
        self.transport_company_label.grid(column=0, row=1, sticky=tk.W)
        self.driver_name_label.grid(column=0, row=2, sticky=tk.W)
        self.id_entry_label.grid(column=0, row=3, sticky=tk.W)
        self.iso_half_life_label.grid(column=0, row=5, sticky=tk.W)
        self.iso_initial_mbq_label.grid(column=0, row=4, sticky=tk.W)

        # space management for entries
        self.company_name_entry.grid(column=1, row=0)
        self.transport_company_entry.grid(column=1, row=1)
        self.driver_name_entry.grid(column=1, row=2)
        self.id_entry.grid(column=1, row=3)
        self.iso_half_life_value_label.grid(column=1, row=5)
        self.iso_initial_mbq_entry.grid(column=1, row=4)

    def get(self):
        return self.id_entry.get()


class DateTimeEntry(tk.Frame):
    def __init__(self, parent, label):
        super().__init__(parent)
        # Labels
        date_label = tk.Label(self, text=label)
        label_0 = tk.Label(self, text='DD/MM/YY:')
        label_1 = tk.Label(self, text='/', borderwidth=0)
        label_2 = tk.Label(self, text='/', borderwidth=0)
        label_3 = tk.Label(self, text='HH:MM', borderwidth=0)
        label_4 = tk.Label(self, text=':', borderwidth=0)
        # Entries
        self.entry_day = tk.Entry(self, width=3, borderwidth=1)
        self.entry_month = tk.Entry(self, width=3, borderwidth=1)
        self.entry_year = tk.Entry(self, width=5, borderwidth=1)
        self.entry_hour = tk.Entry(self, width=3, borderwidth=1)
        self.entry_minute = tk.Entry(self, width=3, borderwidth=1)

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


class Radiobuttons(tk.Frame):
    def __init__(self, parent, data_display):
        super().__init__(parent)
        # Inserts becquerel value to label
        def insert_becquerel():
            v = self.radio.get()
            initial_becquerel = 0
            if v == 1:
                initial_becquerel = 26.83
                data_display.save_path = './DataLog/Holmium-166'
                data_display.isotope_name = 'Holmium-166'
                print('half-life value of Holmium-166 is: ' + str(initial_becquerel))
            elif v == 2:
                initial_becquerel = 1771.68
                data_display.save_path = './DataLog/Iridium-192'
                data_display.isotope_name = 'Iridium-192'
                print('half-life value of Iridium-192 is: ' + str(initial_becquerel))
            elif v == 3:
                initial_becquerel = 1425.12
                data_display.save_path = './DataLog/Jodium-125'
                data_display.isotope_name = 'Jodium-125'
                print('half-life value of Jodium-125 is: ' + str(initial_becquerel))
            elif v == 4:
                initial_becquerel = 192.48
                data_display.save_path = './DataLog/Jodium-131'
                data_display.isotope_name = 'Jodium-131'
                print('half-life value of Jodium-131 is: ' + str(initial_becquerel))
            elif v == 5:
                initial_becquerel = 159.36
                data_display.save_path = './DataLog/Lutetium-177'
                data_display.isotope_name = 'Lutetium-177'
                print('half-life value of Lutetium-177 is: ' + str(initial_becquerel))
            elif v == 6:
                initial_becquerel = 65.94
                data_display.save_path = './DataLog/Molybdenum-99'
                data_display.isotope_name = 'Molybdenum-99'
                print('half-life value of Molybdenum-99 is: ' + str(initial_becquerel))
            elif v == 7:
                initial_becquerel = 1212.00
                data_display.save_path = './DataLog/Strontium-89'
                data_display.isotope_name = 'Strontium-89'
                print('half-life value of Strontium-89 is: ' + str(initial_becquerel))
            elif v == 8:
                initial_becquerel = 6.01
                data_display.save_path = './DataLog/Technetium-99M'
                data_display.isotope_name = 'Technetium-99M'
                print('half-life value of Technetium-99M is: ' + str(initial_becquerel))
            elif v == 9:
                initial_becquerel = 125.88
                data_display.save_path = './DataLog/Xenon-133'
                data_display.isotope_name = 'Xenon-133'
                print('half-life value of Xenon-133 is: ' + str(initial_becquerel))
            elif v == 10:
                initial_becquerel = 63.84
                data_display.save_path = './DataLog/Yttrium-90'
                data_display.isotope_name = 'Yttrium-90'
                print('half-life value of Yttrium-90 is: ' + str(initial_becquerel))

            # Temporarily sets the state on the label to 'normal', otherwise unable to insert() a string.
            # After insert, sets state back to 'readonly'
            data_display.product_info.iso_half_life_value_label.configure(state=tk.NORMAL)
            data_display.product_info.iso_half_life_value_label.delete(0, 20)
            data_display.product_info.iso_half_life_value_label.insert(0, initial_becquerel)
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
