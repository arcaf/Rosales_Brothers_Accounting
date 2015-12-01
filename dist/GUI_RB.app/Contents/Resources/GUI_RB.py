import Tkinter
import datetime
import ttk
import os.path
from collections import namedtuple
class InitRB:
        def __init__(self):
                self._root_window = Tkinter.Tk()
                self.center_window(200, 300)
                self._root_window.title('numBR')
                self._label_0 = Tkinter.Label(self._root_window, text='Welcome to numBR 1.0 \n by: Francisco Arca')
                self._label_0.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label = Tkinter.Label(self._root_window, text='What would you like to do?')
                self._label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._var = Tkinter.StringVar(self._root_window)
                self._var.set("Seleccione una opcion...")
                self._entry = Tkinter.OptionMenu(self._root_window, self._var, 'Seleccione una opcion...', 'Anadir gasto', 'Anadir ingreso', 'Anadir payroll', 'Anadir empleado','Borrar empleado', 'Mostrar totales de la compania')
                self._entry.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._okay = Tkinter.Button(self._root_window, text = 'Okay', width= 8, command=self.get_text)
                self._okay.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = Tkinter.S)
                self._exit = Tkinter.Button(self._root_window, text = 'Quit', width= 8, command=self.quit)
                self._exit.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = Tkinter.S)
                self._clear = Tkinter.Button(self._root_window, text = 'Clear(only admin)', width= 15, command=self.stop)
                self._clear.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = Tkinter.S)
                self._root_window.rowconfigure(0, weight = 1)
                self._root_window.rowconfigure(1, weight = 1)
                self._root_window.rowconfigure(2, weight = 1)
                self._root_window.rowconfigure(3, weight = 1)
                self._root_window.rowconfigure(4, weight = 1)
                self._root_window.rowconfigure(5, weight = 1)
                self._root_window.columnconfigure(0, weight = 1)


        def center_window(self, w, h):

                ws = self._root_window.winfo_screenwidth()
                hs = self._root_window.winfo_screenheight()
                x = (ws/2) - (w/2)    
                y = (hs/2) - (h/2)
                self._root_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        def start(self):
                self._root_window.mainloop()
        def stop(self):
                self._new_window = Tkinter.Toplevel()
                self._label = Tkinter.Label(self._new_window, text='''Please enter a valid password\nfor this function\n\n''')
                self._label.grid(row=0, column=0, padx=0, pady=0)
                self._text1 = Tkinter.Entry(self._new_window, bg = "gray", width = 20, show="*")
                self._text1.grid(row=2, column=0, padx=30, pady=5)
                self._button_ok= Tkinter.Button(self._new_window, text = 'Okay', command=self.clear)
                self._button_ok.grid(row=4, column=0, padx=3, pady=3, sticky = Tkinter.W)
                self._button_can= Tkinter.Button(self._new_window, text = 'Cancel', command=self.ok)
                self._button_can.grid(row=4, column=0, padx=3, pady=3, sticky = Tkinter.E)
                self._new_window.rowconfigure(0, weight=1)
                self._new_window.rowconfigure(1, weight=1)
                self._new_window.columnconfigure(0, weight=1)
                self._new_window.grab_set()
                self._new_window.wait_window()
        def clear(self):
                if self._text1.get() == "rosalesadmin":
                        f = open("incomes.txt", "r+")
                        f.truncate()
                        f.close()
                        g = open("expenses.txt", "r+")
                        g.truncate()
                        g.close()
                        t = open("employees.txt", "r+")
                        t.truncate()
                        t.close()
                        self._clear_window = Tkinter.Toplevel()
                        self._label = Tkinter.Label(self._clear_window, text='''Clearing successful!\n\n''')
                        self._label.grid(row=0, column=0, padx=0, pady=0)
                        self._button_ok= Tkinter.Button(self._clear_window, text = 'Okay', command=self.clear_ok)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0)
                        self._clear_window.rowconfigure(0, weight=1)
                        self._clear_window.rowconfigure(1, weight=1)
                        self._clear_window.columnconfigure(0, weight=1)
                        self._clear_window.grab_set()
                        self._clear_window.wait_window()
                else:
                        self.ok()
                        self._new_window = Tkinter.Toplevel()
                        self._label = Tkinter.Label(self._new_window, text='''Not a valid password!\n\n''')
                        self._label.grid(row=0, column=0, padx=0, pady=0)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'Okay', command=self.change)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0)
                        self._new_window.rowconfigure(0, weight=1)
                        self._new_window.rowconfigure(1, weight=1)
                        self._new_window.columnconfigure(0, weight=1)
                        self._new_window.grab_set()
                        self._new_window.wait_window()
        def change(self):
                self.ok()
                self.stop()
                
        def exp_cancel(self):
                self._exp_window.destroy()
        def ok(self):
                self._new_window.destroy()
        def clear_ok(self):
                self._clear_window.destroy()
                self._new_window.destroy()
        def ok_now(self):
                self._new_window.destroy()
                self._exp_window.destroy()
        def quit(self):
                self._root_window.destroy()
        def add_expense_fromhere(self):
                self._exp_window.destroy()
                self._new_window.destroy()
                self.add_expense()
        def add_payroll_fromhere(self):
                self._exp_window.destroy()
                self._new_window.destroy()
                self.driver()
        def add_income_fromhere(self):
                self._exp_window.destroy()
                self._new_window.destroy()
                self.add_income()
        def add_employee_fromhere(self):
                self._exp_window.destroy()
                self._new_window.destroy()
                self.employees()
        def get_text(self):
                if self._var.get() == "Seleccione una opcion...":
                        self._new_window = Tkinter.Toplevel()
                        self._label = Tkinter.Label(self._new_window, text='''Por favor asegurese de seleccionar una opcion\n\n''')
                        self._label.grid(row=0, column=0, padx=0, pady=0)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'Okay', command=self.ok)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0)
                        self._new_window.rowconfigure(0, weight=1)
                        self._new_window.rowconfigure(1, weight=1)
                        self._new_window.columnconfigure(0, weight=1)
                        self._new_window.grab_set()
                        self._new_window.wait_window()
                elif self._var.get() == "Anadir gasto":
                        self.add_expense()
                elif self._var.get() == "Anadir ingreso":
                        self.add_income()
                elif self._var.get() == "Mostrar totales de la compania":
                        self.show_totals()
                elif self._var.get() == "Anadir empleado":
                        self.employees()
                elif self._var.get() == "Anadir payroll":
                        self.driver()
                elif self._var.get() == "Borrar empleado":
                        self.delete_emp()
        def delete_emp(self):
                with open('employees.txt', 'r') as infile:
                        lines = infile.readlines()
                self.l_emp = ["Select a choice..."]
                self.filenames = ["Select a choice..."]
                for line in lines:
                        d = line.find("Name")
                        if d != -1:
                                self.l_emp.append(line[d+6:].strip('\n').strip("\""))
                self._exp_window = Tkinter.Tk()
                self._exp_window.title('Borrar dempleados del sistema')
                self._label_exp_0 = Tkinter.Label(self._exp_window, text='Forma para borrar a un empleado permanentemente')
                self._label_exp_0.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._drivers = Tkinter.StringVar(self._exp_window)
                self._drivers.set("Select a choice...")
                self._drivers_entry = Tkinter.OptionMenu(self._exp_window, self._drivers, *self.l_emp)
                self._drivers_entry.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_2 = Tkinter.Label(self._exp_window, text='Fecha de nacimiento (MM/DD/YYYY):')
                self._label_exp_2.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._text_exp_2 = Tkinter.Entry(self._exp_window, relief="raised", width = 10, bg = "gray")
                self._text_exp_2.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._add = Tkinter.Button(self._exp_window, text = 'Borrar empleado', width= 15, command=self.borrar_emp)
                self._add.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = Tkinter.W)
                self._back = Tkinter.Button(self._exp_window, text = 'Cancelar', width= 15, command=self.exp_cancel)
                self._back.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = Tkinter.E)
                self._root_window.rowconfigure(0, weight = 1)
                self._root_window.rowconfigure(1, weight = 1)
                self._root_window.rowconfigure(2, weight = 1)
                self._root_window.rowconfigure(3, weight = 1)
                self._root_window.rowconfigure(4, weight = 1)
                self._root_window.rowconfigure(5, weight = 1)
                self._root_window.columnconfigure(0, weight = 1)
        def borrar_emp(self):
                try:
                        count = 0
                        l = self._drivers.get().strip().split()
                        date = self._text_exp_2.get().split(self._text_exp_2.get()[2])
                        os.remove(date[0]+date[1]+date[2]+l[-1]+l[0]+'.txt')
                        with open('employees.txt', 'r') as infile:
                                lines = infile.readlines()
                        f = open('employees.txt', 'w')
                        for line in range(len(lines)):
                                if lines[line] == 'new\n' and self._drivers.get() in lines[line+1] :
                                        count = 5
        
                                if count >= 0:
                                        count -= 1
                                else:
                                        f.write(lines[line])

                        f.close()
                        self._new_window = Tkinter.Toplevel()
                        self._label = Tkinter.Label(self._new_window, text='''Empleado borrado!''')
                        self._label.grid(row=0, column=0, padx=10, pady=10)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'Okay', command=self.ok_now)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0)
                        self._new_window.rowconfigure(0, weight=1)
                        self._new_window.rowconfigure(1, weight=1)
                        self._new_window.columnconfigure(0, weight=1)
                        self._new_window.grab_set()
                        self._new_window.wait_window()
                except:
                        self._new_window = Tkinter.Toplevel()
                        self._label = Tkinter.Label(self._new_window, text='''Esta entrada no es valida,\n chequea lo que acabas de poner\n\n''')
                        self._label.grid(row=0, column=0, padx=0, pady=0)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'Okay', command=self.ok)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0)
                        self._new_window.rowconfigure(0, weight=1)
                        self._new_window.rowconfigure(1, weight=1)
                        self._new_window.columnconfigure(0, weight=1)
                        self._new_window.grab_set()
                        self._new_window.wait_window()
        def employees(self):
                self._exp_window = Tkinter.Tk()
                self._exp_window.title('Anadir empleado al sistema')
                self._label_exp_0 = Tkinter.Label(self._exp_window, text='Forma para anadir un empleado')
                self._label_exp_0.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_1 = Tkinter.Label(self._exp_window, text='Nombre y apellido del empleado: ')
                self._label_exp_1.grid(row = 1, column = 0, padx = 0, pady = 10, sticky = Tkinter.N)
                self._text_exp_1 = Tkinter.Entry(self._exp_window, relief="raised", width = 25, bg = "gray")
                self._text_exp_1.grid(row = 2, column = 0, padx = 0, pady = 10, sticky = Tkinter.N)
                self._label_exp_2 = Tkinter.Label(self._exp_window, text='Fecha de nacimiento (MM/DD/YYYY):')
                self._label_exp_2.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._text_exp_2 = Tkinter.Entry(self._exp_window, relief="raised", width = 10, bg = "gray")
                self._text_exp_2.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_3 = Tkinter.Label(self._exp_window, text='Direccion del empleado:')
                self._label_exp_3.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._text_exp_3 = Tkinter.Text(self._exp_window, relief="raised", height = 4, width = 50, bg = "gray")
                self._text_exp_3.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_4 = Tkinter.Label(self._exp_window, text='Otros_comentarios:')
                self._label_exp_4.grid(row = 7, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._text_exp_4 = Tkinter.Text(self._exp_window, relief="raised", height = 4, width = 50, bg = "gray")
                self._text_exp_4.grid(row = 8, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._add = Tkinter.Button(self._exp_window, text = 'Anadir empleado', width= 15, command=self.add_emp)
                self._add.grid(row = 9, column = 0, padx = 10, pady = 10, sticky = Tkinter.W)
                self._back = Tkinter.Button(self._exp_window, text = 'cancelar', width= 15, command=self.exp_cancel)
                self._back.grid(row = 9, column = 0, padx = 10, pady = 10, sticky = Tkinter.E)
                self._root_window.rowconfigure(0, weight = 1)
                self._root_window.rowconfigure(1, weight = 1)
                self._root_window.rowconfigure(2, weight = 1)
                self._root_window.rowconfigure(3, weight = 1)
                self._root_window.rowconfigure(4, weight = 1)
                self._root_window.rowconfigure(5, weight = 1)
                self._root_window.rowconfigure(6, weight = 1)
                self._root_window.rowconfigure(7, weight = 1)
                self._root_window.rowconfigure(8, weight = 1)
                self._root_window.rowconfigure(9, weight = 1)
                self._root_window.columnconfigure(0, weight = 1)

        def add_emp(self):
                try:
                        if self._text_exp_1.get() == "" or self._text_exp_2.get() == "":
                                outfile = open('employees.txt', 'a')
                                raise Exception()
                        full = self._text_exp_1.get().strip().split()
                        date = self._text_exp_2.get().split(self._text_exp_2.get()[2])
                        
                        with open('employees.txt', 'r') as infile:
                                lines = infile.readlines()
                        outfile = open('employees.txt', 'a')
                        dated = datetime.date(int(date[2]), int(date[0]), int(date[1]))
                        l = self._text_exp_1.get().strip().split()
                        if os.path.isfile(str(date[0])+str(date[1])+str(date[2])+str(l[-1])+str(l[0])+'.txt'):
                                raise Exception()
                        else:
                                
                                open(str(date[0])+str(date[1])+str(date[2])+str(l[-1])+str(l[0])+'.txt', 'w')

                        if len(lines) == 0 :
                                outfile.write("--------------Company Employee(s) entered on"+ str(datetime.datetime.now().date())+" ----------------------\n")
                                outfile.write("DOB:"+ str(dated)+"Full Name:\""+str(self._text_exp_1.get().strip())+"\"")
                                outfile.write("\nAddress: "+str(self._text_exp_3.get("1.0", 'end-1c'))+"\n"+ "Other_Comments:\""+ str(self._text_exp_4.get("1.0", 'end-1c'))+"\"\n")
                                outfile.write("Filename: "+ "\"" + str(date[0])+str(date[1])+str(date[2])+str(l[-1])+str(l[0])+'.txt'+"\"\n")
                                
                        else:
                                outfile.write('new\n')
                                outfile.write("DOB:"+ str(dated)+"Full Name:\""+str(self._text_exp_1.get().strip())+"\"")
                                outfile.write("\nAddress: "+str(self._text_exp_3.get("1.0", 'end-1c'))+"\n"+ "Other_Comments:\""+ str(self._text_exp_4.get("1.0", 'end-1c'))+"\"\n")
                                outfile.write("Filename: "+ "\"" + str(date[0])+str(date[1])+str(date[2])+str(l[-1])+str(l[0])+'.txt'+"\"\n")

                                
                        outfile.close()
                        
                        self._new_window = Tkinter.Toplevel()
                        self._label = Tkinter.Label(self._new_window, text='''Entrada satisfactoria! \nLe gustaria hace otra??\n\n''')
                        self._label.grid(row=0, column=0, padx=10, pady=10)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'No', command=self.ok_now)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0, sticky = Tkinter.E,)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'Yes', command=self.add_employee_fromhere)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0, sticky = Tkinter.W)
                        self._new_window.rowconfigure(0, weight=1)
                        self._new_window.rowconfigure(1, weight=1)
                        self._new_window.columnconfigure(0, weight=1)
                        self._new_window.grab_set()
                        self._new_window.wait_window()
                        
                except:
                        outfile.close()
                        self._new_window = Tkinter.Toplevel()
                        self._label = Tkinter.Label(self._new_window, text='''Esta entrada no es valida,\n chequea lo que acabas de poner\n\n''')
                        self._label.grid(row=0, column=0, padx=0, pady=0)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'Okay', command=self.ok)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0)
                        self._new_window.rowconfigure(0, weight=1)
                        self._new_window.rowconfigure(1, weight=1)
                        self._new_window.columnconfigure(0, weight=1)
                        self._new_window.grab_set()
                        self._new_window.wait_window()
        def driver(self):
                with open('employees.txt', 'r') as infile:
                        lines = infile.readlines()
                self.l_emp = ["Select a choice..."]
                self.filenames = ["Select a choice..."]
                for line in lines:
                        d = line.find("Name")
                        f = line.find("Filename")
                        if d != -1:
                                self.l_emp.append(line[d+6:].strip('\n').strip("\""))
                        if f != -1:
                                self.filenames.append(line[d+11:].strip('\n').strip("\""))

                self._exp_window = Tkinter.Tk()
                self._exp_window.title('Anadir el pago de nomina de un chofer (payroll)')
                self._label_exp_0 = Tkinter.Label(self._exp_window, text='Anadir payroll')
                self._label_exp_0.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._drivers = Tkinter.StringVar(self._exp_window)
                self._drivers.set("Select a choice...")
                self._drivers_entry = Tkinter.OptionMenu(self._exp_window, self._drivers, *self.l_emp)
                self._drivers_entry.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_2 = Tkinter.Label(self._exp_window, text='Cantidad pagada (in $):')
                self._label_exp_2.grid(row = 3, column = 0, padx = 0, pady = 10, sticky = Tkinter.N)
                self._label_exp_2_1 = Tkinter.Label(self._exp_window, text='$')
                self._label_exp_2_1.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = Tkinter.W)
                self._text_exp_2 = Tkinter.Entry(self._exp_window, relief="raised", width = 15, bg = "gray")
                self._text_exp_2.grid(row = 4, column = 0, padx = 0, pady = 10, sticky = Tkinter.N)
                self._label_exp_3 = Tkinter.Label(self._exp_window, text='Fecha del pago(MM/DD/YYYY):')
                self._label_exp_3.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._text_exp_3 = Tkinter.Entry(self._exp_window, relief="raised", width = 10, bg = "gray")
                self._text_exp_3.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_4 = Tkinter.Label(self._exp_window, text='Otros_commentarios:')
                self._label_exp_4.grid(row = 7, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._text_exp_4 = Tkinter.Text(self._exp_window, relief="raised", height = 4, width = 50, bg = "gray")
                self._text_exp_4.grid(row = 8, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._add = Tkinter.Button(self._exp_window, text = 'Anadir payroll', width= 15, command=self.add_to_file_payroll)
                self._add.grid(row = 9, column = 0, padx = 10, pady = 10, sticky = Tkinter.W)
                self._back = Tkinter.Button(self._exp_window, text = 'cancelar', width= 15, command=self.exp_cancel)
                self._back.grid(row = 9, column = 0, padx = 10, pady = 10, sticky = Tkinter.E)
                self._root_window.rowconfigure(0, weight = 1)
                self._root_window.rowconfigure(1, weight = 1)
                self._root_window.rowconfigure(2, weight = 1)
                self._root_window.rowconfigure(3, weight = 1)
                self._root_window.rowconfigure(4, weight = 1)
                self._root_window.rowconfigure(5, weight = 1)
                self._root_window.rowconfigure(6, weight = 1)
                self._root_window.rowconfigure(7, weight = 1)
                self._root_window.rowconfigure(8, weight = 1)
                self._root_window.rowconfigure(9, weight = 1)
                self._root_window.columnconfigure(0, weight = 1)

        def add_to_file_payroll(self):
                try:
                        if self._text_exp_2.get() == "" or self._drivers.get() == 'Select a choice...' or "," in self._text_exp_2.get():
                                outfile = open('employees.txt', 'a')
                                raise Exception()
                        
                        num = self.l_emp.index(self._drivers.get())
                        with open(self.filenames[num], 'r') as infile:
                                lines = infile.readlines()
                        outfile = open(self.filenames[num], 'a')
                        
 

                        d = self._text_exp_3.get().split(self._text_exp_3.get()[2])
                        dated = datetime.date(int(d[2]), int(d[0]), int(d[1]))
                        
                        if len(lines) == 0:
                                outfile.write("--------------Payroll(s)_entered_for "+ str(self._drivers.get())+" ----------------------\n")
                                outfile.write("Paid_on:\""+str(dated)+"\" "+ " Amount:\"$"+ str(self._text_exp_2.get())+"\"")
                                outfile.write("\nOther_Comments:\""+ str(self._text_exp_4.get("1.0", 'end-1c'))+"\"\n")
                                
                        else:
                                outfile.write("Paid_on:\""+str(dated)+"\" "+ " Amount:\"$"+ str(self._text_exp_2.get())+"\"")
                                outfile.write("\nOther_Comments:\""+ str(self._text_exp_4.get("1.0", 'end-1c'))+"\"\n")
                        outfile.close()
                        self._new_window = Tkinter.Toplevel()
                        self._label = Tkinter.Label(self._new_window, text='''Entrada satisfactoria! \nLe gustaria hace otra?\n\n''')
                        self._label.grid(row=0, column=0, padx=10, pady=10)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'No', command=self.ok_now)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0, sticky = Tkinter.E,)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'Yes', command=self.add_payroll_fromhere)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0, sticky = Tkinter.W)
                        self._new_window.rowconfigure(0, weight=1)
                        self._new_window.rowconfigure(1, weight=1)
                        self._new_window.columnconfigure(0, weight=1)
                        self._new_window.grab_set()
                        self._new_window.wait_window()
                except:
                        outfile.close()
                        self._new_window = Tkinter.Toplevel()
                        self._label = Tkinter.Label(self._new_window, text='''Esta entrada no es valida,\n chequea lo que acabas de poner\n\n''')
                        self._label.grid(row=0, column=0, padx=0, pady=0)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'Okay', command=self.ok)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0)
                        self._new_window.rowconfigure(0, weight=1)
                        self._new_window.rowconfigure(1, weight=1)
                        self._new_window.columnconfigure(0, weight=1)
                        self._new_window.grab_set()
                        self._new_window.wait_window()
                
        def add_to_file_expense(self):
                try:
                        if self._text_exp_2.get() == "" or "," in self._text_exp_2.get():
                                outfile = open('payroll_Yoimar.txt', 'a')
                                raise Exception()
                        with open('expenses.txt', 'r') as infile:
                                lines = infile.readlines()
                        outfile = open('expenses.txt', 'a')
                        d = self._text_exp_3.get().split(self._text_exp_3.get()[2])
                        dated = datetime.date(int(d[2]), int(d[0]), int(d[1]))
                        
                        if len(lines) == 0:
                                outfile.write("--------------Expense(s)_entered_on "+ str(datetime.datetime.now().date())+" ----------------------\n")
                                outfile.write("date spent:\""+str(dated)+"\" "+ " Amount:\"$"+ str(self._text_exp_2.get())+"\"")
                                outfile.write("\nNickname:\""+str(self._text_exp_1.get())+"\" "+ " Other_Comments:\""+ str(self._text_exp_4.get("1.0", 'end-1c'))+"\"\n")
                                
                        else:
                                for line in range(0, len(lines)-1, 3):
                                        if lines[line][0] == "-":
                                                ft = lines[line].split()
                                                dat = ft[1].split("-")
                                                fixed = datetime.date(int(dat[0]), int(dat[1]), int(dat[2]))
                                                if (fixed == datetime.datetime.now().date()):
                                                        outfile.write("\ndate spent:\""+str(dated)+"\" "+ " Amount:\"$"+ str(self._text_exp_2.get())+"\"")
                                                        outfile.write("\nNickname:\""+str(self._text_exp_1.get())+"\" "+ " Other_Comments:\""+ str(self._text_exp_4.get("1.0", 'end-1c'))+"\"\n")
                                                else:
                                                        outfile.write("\n--------------Expense(s)_entered_on "+ str(datetime.datetime.now().date())+" ----------------------")
                                                        outfile.write("\ndate spent:\""+str(dated)+"\" "+ " Amount:\"$"+ str(self._text_exp_2.get())+"\"")
                                                        outfile.write("\nNickname:\""+str(self._text_exp_1.get())+"\" "+ " Other_Comments:\""+ str(self._text_exp_4.get("1.0", 'end-1c'))+"\"\n")
                        outfile.close()
                        self._new_window = Tkinter.Toplevel()
                        self._label = Tkinter.Label(self._new_window, text='''Entrada satisfactoria! \nLe gustaria hace otra?\n\n''')
                        self._label.grid(row=0, column=0, padx=10, pady=10)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'No', command=self.ok_now)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0, sticky = Tkinter.E,)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'Yes', command=self.add_expense_fromhere)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0, sticky = Tkinter.W)
                        self._new_window.rowconfigure(0, weight=1)
                        self._new_window.rowconfigure(1, weight=1)
                        self._new_window.columnconfigure(0, weight=1)
                        self._new_window.grab_set()
                        self._new_window.wait_window()
                                               
                except:
                        outfile.close()
                        self._new_window = Tkinter.Toplevel()
                        self._label = Tkinter.Label(self._new_window, text='''Esta entrada no es valida,\n chequea lo que acabas de poner\n\n''')
                        self._label.grid(row=0, column=0, padx=0, pady=0)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'Okay', command=self.ok)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0)
                        self._new_window.rowconfigure(0, weight=1)
                        self._new_window.rowconfigure(1, weight=1)
                        self._new_window.columnconfigure(0, weight=1)
                        self._new_window.grab_set()
                        self._new_window.wait_window()
        def add_to_file_income(self):
                try:
                        if self._text_exp_2.get() == "" or "," in self._text_exp_2.get():
                                outfile = open('employees.txt', 'a')
                                raise Exception()
                        with open('incomes.txt', 'r') as infile:
                                lines = infile.readlines()
                        outfile = open('incomes.txt', 'a')
                        d = self._text_exp_3.get().split(self._text_exp_3.get()[2])
                        dated = datetime.date(int(d[2]), int(d[0]), int(d[1]))
                        

                        if len(lines) == 0 :
                                outfile.write("--------------Income(s)_entered_on "+ str(datetime.datetime.now().date())+" ----------------------\n")
                                outfile.write("Pay_date:\""+str(dated)+"\" "+ " Amount:$"+ str(self._text_exp_2.get()))
                                outfile.write("\nNickname:\""+str(self._text_exp_1.get())+"\" "+ " Other_Comments:\""+ str(self._text_exp_4.get("1.0", 'end-1c'))+"\"\n")
                                
                        else:
                                for line in range(0, len(lines)-1, 3):
                                        if lines[line][0] == "-":
                                                ft = lines[line].split()
                                                dat = ft[1].split("-")
                                                
                                                fixed = datetime.date(int(dat[0]), int(dat[1]), int(dat[2]))
                                                if (fixed == datetime.datetime.now().date()):
                                                        outfile.write("\nPay_date:\""+str(dated)+"\" "+ " Amount:$"+ str(self._text_exp_2.get()))
                                                        outfile.write("\nNickname:\""+str(self._text_exp_1.get())+"\" "+ " Other_Comments:\""+ str(self._text_exp_4.get("1.0", 'end-1c'))+"\"\n")
                                                else:
                                                        outfile.write("\n--------------Income(s)_entered_on "+ str(datetime.datetime.now().date())+" ----------------------")
                                                        outfile.write("\nPay_date:\""+str(dated)+"\" "+ " Amount:$"+ str(self._text_exp_2.get()))
                                                        outfile.write("\nNickname:\""+str(self._text_exp_1.get())+"\" "+ " Other_Comments:\""+ str(self._text_exp_4.get("1.0", 'end-1c'))+"\"\n")
                        outfile.close()
                        self._new_window = Tkinter.Toplevel()
                        self._label = Tkinter.Label(self._new_window, text='''Entrada satisfactoria! \nLe gustaria hace otra??\n\n''')
                        self._label.grid(row=0, column=0, padx=10, pady=10)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'No', command=self.ok_now)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0, sticky = Tkinter.E,)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'Yes', command=self.add_income_fromhere)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0, sticky = Tkinter.W)
                        self._new_window.rowconfigure(0, weight=1)
                        self._new_window.rowconfigure(1, weight=1)
                        self._new_window.columnconfigure(0, weight=1)
                        self._new_window.grab_set()
                        self._new_window.wait_window()
                                               
                except:
                        outfile.close()
                        self._new_window = Tkinter.Toplevel()
                        self._label = Tkinter.Label(self._new_window, text='''Esta entrada no es valida,\n chequea lo que acabas de poner\n\n''')
                        self._label.grid(row=0, column=0, padx=0, pady=0)
                        self._button_ok= Tkinter.Button(self._new_window, text = 'Okay', command=self.ok)
                        self._button_ok.grid(row=1, column=0, padx=0, pady=0)
                        self._new_window.rowconfigure(0, weight=1)
                        self._new_window.rowconfigure(1, weight=1)
                        self._new_window.columnconfigure(0, weight=1)
                        self._new_window.grab_set()
                        self._new_window.wait_window()
        def get_income_totals(self, file):
                with open(file, 'r') as infile:
                        lines = infile.readlines()
                count = 0
                for line in lines:
                        d = line.find("Amount")
                        if d != -1:
                                amount = float(line[d+8:].strip('\n').strip('$').strip("\""))
                                count += amount                               
                return count
        def get_payroll_totals(self):
                NL = []
                new = ""
                count = 0
                with open('employees.txt', 'r') as infile:
                        lines = infile.readlines()
                employee = namedtuple('employee', 'name filename payroll')
                for line in lines:
                        if line == "new\n":
                                count = 0
                        d = line.find("Name")
                        f = line.find("Filename")
                        if d != -1:
                                new = line[d+6:].strip('\n').strip("\"")
                        if f != -1:
                                with open(line[f+11:].strip('\n').strip("\""), 'r') as outfile:
                                        moneylines = outfile.readlines()
                                for m in moneylines:
                                        money = m.find("Amount")
                                        if money != -1:
                                                amount = float(m[money+8:].strip('\n').strip('$').strip("\""))
                                                count += amount
                                NL.append(employee(new, line[f+11:].strip('\n').strip("\""), count))
                                outfile.close()
                return NL
                        
        
        def show_totals(self):
                self._exp_window = Tkinter.Tk()
                self._exp_window.title('Rosales Brothers Totals')
                self._label_exp_0 = Tkinter.Label(self._exp_window, text='Rosales Company Totals')
                self._label_exp_0.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._exp_frame = Tkinter.Frame(self._exp_window, relief = "sunken", bg="gray")
                self._exp_frame.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                count_inc = self.get_income_totals("incomes.txt")
                count_exp = self.get_income_totals("expenses.txt")
                self.count_payroll = self.get_payroll_totals()
                total_pay = 0
                for emp in self.count_payroll:
                        total_pay += emp.payroll
                self._label_exp_1 = Tkinter.Label(self._exp_frame, text='Total de ingresos:              $'+ format(count_inc, ',.2f'))
                self._label_exp_1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_2 = Tkinter.Label(self._exp_frame, text='Total de gastos:           (loss)$'+ format(count_exp, ',.2f'))
                self._label_exp_2.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_3 = Tkinter.Label(self._exp_frame, text='Total payroll:           (loss)$'+ format(total_pay, ',.2f'))
                self._label_exp_3.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._show = Tkinter.Button(self._exp_window, text = 'Detalles de payroll', width= 20, command=self.show_details_payroll)
                self._show.grid(row = 4, column = 0, padx = 5, pady = 10, sticky = Tkinter.E)
                self._label_exp_5 = Tkinter.Label(self._exp_frame, font = "Helvetica 16 bold", text='Perdida total:           (loss)$'+ format(total_pay+count_exp, ',.2f'))
                self._label_exp_5.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                if count_inc-(total_pay+count_exp) < 0:
                        self._label_exp_6 = Tkinter.Label(self._exp_frame, font = "Helvetica 16 bold", text='Gross company profit: (loss)$'+ format(abs(count_inc-(total_pay+count_exp)), ',.2f'))
                        self._label_exp_6.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                else:
                        self._label_exp_7 = Tkinter.Label(self._exp_frame, font = "Helvetica 16 bold", text='Gross company profit:       $'+ format(abs(count_inc-(total_pay+count_exp)), ',.2f'))
                        self._label_exp_7.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
       
                self._back = Tkinter.Button(self._exp_window, text = 'Ir atras', width= 10, command=self.exp_cancel)
                self._back.grid(row = 7, column = 0, padx = 5, pady = 10, sticky = Tkinter.E)
                self._root_window.rowconfigure(0, weight = 1)
                self._root_window.rowconfigure(1, weight = 1)
                self._root_window.rowconfigure(2, weight = 1)
                self._root_window.rowconfigure(3, weight = 1)
                self._root_window.rowconfigure(4, weight = 1)
                self._root_window.rowconfigure(5, weight = 1)
                self._root_window.rowconfigure(6, weight = 1)
                self._root_window.rowconfigure(7, weight = 1)
                self._root_window.rowconfigure(7, weight = 1)
                self._root_window.columnconfigure(0, weight = 1)
        def show_details_payroll(self):
                new_list = []
                for emp in self.count_payroll:
                        new_list.append(emp.name + " - $"+format(emp.payroll, ',.2f'))
                self._new_window = Tkinter.Toplevel()
                self._label = Tkinter.Label(self._new_window, text='''Empleados\n''')
                self._label.grid(row=0, column=0, padx=10, pady=10)
                self._label_0 = Tkinter.Label(self._new_window, text='''Nombre             Cantidad\n''')
                self._label_0.grid(row=1, column=0, padx=10, pady=10)
                self._label_1 = Tkinter.Label(self._new_window, text="\n".join(map(str, new_list)))
                self._label_1.grid(row=2, column=0, padx=10, pady=10)
                self._button_ok= Tkinter.Button(self._new_window, text = 'Okay', command=self.ok)
                self._button_ok.grid(row=3, column=0, padx=0, pady=0, sticky = Tkinter.E,)
                self._new_window.rowconfigure(0, weight=1)
                self._new_window.rowconfigure(1, weight=1)
                self._new_window.rowconfigure(2, weight=1)
                self._new_window.rowconfigure(3, weight=1)
                self._new_window.columnconfigure(0, weight=1)
                self._new_window.grab_set()
                self._new_window.wait_window()
                        
        def add_expense(self):
                self._exp_window = Tkinter.Tk()
                self._exp_window.title('Anadir un gasto')
                self._label_exp_0 = Tkinter.Label(self._exp_window, text='Forma para anadir un gasto')
                self._label_exp_0.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_1 = Tkinter.Label(self._exp_window, text='Nickname del gasto:')
                self._label_exp_1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._text_exp_1 = Tkinter.Entry(self._exp_window, relief="raised", width = 50, bg = "gray")
                self._text_exp_1.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_2 = Tkinter.Label(self._exp_window, text='Cantidad gastada (in $):')
                self._label_exp_2.grid(row = 3, column = 0, padx = 0, pady = 10, sticky = Tkinter.N)
                self._label_exp_2_1 = Tkinter.Label(self._exp_window, text='$')
                self._label_exp_2_1.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = Tkinter.W)
                self._text_exp_2 = Tkinter.Entry(self._exp_window, relief="raised", width = 15, bg = "gray")
                self._text_exp_2.grid(row = 4, column = 0, padx = 0, pady = 10, sticky = Tkinter.N)
                self._label_exp_3 = Tkinter.Label(self._exp_window, text='Fecha del gasto (MM/DD/YYYY):')
                self._label_exp_3.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._text_exp_3 = Tkinter.Entry(self._exp_window, relief="raised", width = 10, bg = "gray")
                self._text_exp_3.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_4 = Tkinter.Label(self._exp_window, text='Otros_comentarios:')
                self._label_exp_4.grid(row = 7, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._text_exp_4 = Tkinter.Text(self._exp_window, relief="raised", height = 4, width = 50, bg = "gray")
                self._text_exp_4.grid(row = 8, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._add = Tkinter.Button(self._exp_window, text = 'Anadir el gasto', width= 15, command=self.add_to_file_expense)
                self._add.grid(row = 9, column = 0, padx = 10, pady = 10, sticky = Tkinter.W)
                self._back = Tkinter.Button(self._exp_window, text = 'cancelar', width= 15, command=self.exp_cancel)
                self._back.grid(row = 9, column = 0, padx = 10, pady = 10, sticky = Tkinter.E)
                self._root_window.rowconfigure(0, weight = 1)
                self._root_window.rowconfigure(1, weight = 1)
                self._root_window.rowconfigure(2, weight = 1)
                self._root_window.rowconfigure(3, weight = 1)
                self._root_window.rowconfigure(4, weight = 1)
                self._root_window.rowconfigure(5, weight = 1)
                self._root_window.rowconfigure(6, weight = 1)
                self._root_window.rowconfigure(7, weight = 1)
                self._root_window.rowconfigure(8, weight = 1)
                self._root_window.rowconfigure(9, weight = 1)
                self._root_window.columnconfigure(0, weight = 1)

        def add_income(self):
                self._exp_window = Tkinter.Tk()
                self._exp_window.title('Anadir una entrada')
                self._label_exp_0 = Tkinter.Label(self._exp_window, text='Forma para anadir una entrada')
                self._label_exp_0.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_1 = Tkinter.Label(self._exp_window, text='Income Nickname:')
                self._label_exp_1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._text_exp_1 = Tkinter.Entry(self._exp_window, relief="raised", width = 50, bg = "gray")
                self._text_exp_1.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_2 = Tkinter.Label(self._exp_window, text='Cantidad del ingreso(in $):')
                self._label_exp_2.grid(row = 3, column = 0, padx = 0, pady = 10, sticky = Tkinter.N)
                self._label_exp_2_1 = Tkinter.Label(self._exp_window, text='$')
                self._label_exp_2_1.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = Tkinter.W)
                self._text_exp_2 = Tkinter.Entry(self._exp_window, relief="raised", width = 15, bg = "gray")
                self._text_exp_2.grid(row = 4, column = 0, padx = 0, pady = 10, sticky = Tkinter.N)
                self._label_exp_3 = Tkinter.Label(self._exp_window, text='Fecha del ingreso(MM/DD/YYYY):')
                self._label_exp_3.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._text_exp_3 = Tkinter.Entry(self._exp_window, relief="raised", width = 10, bg = "gray")
                self._text_exp_3.grid(row = 6, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._label_exp_4 = Tkinter.Label(self._exp_window, text='Otros_comentarios:')
                self._label_exp_4.grid(row = 7, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._text_exp_4 = Tkinter.Text(self._exp_window, relief="raised", height = 4, width = 50, bg = "gray")
                self._text_exp_4.grid(row = 8, column = 0, padx = 10, pady = 10, sticky = Tkinter.N)
                self._add = Tkinter.Button(self._exp_window, text = 'Anadir el ingreso', width= 15, command=self.add_to_file_income)
                self._add.grid(row = 9, column = 0, padx = 10, pady = 10, sticky = Tkinter.W)
                self._back = Tkinter.Button(self._exp_window, text = 'cancelar', width= 15, command=self.exp_cancel)
                self._back.grid(row = 9, column = 0, padx = 10, pady = 10, sticky = Tkinter.E)
                self._root_window.rowconfigure(0, weight = 1)
                self._root_window.rowconfigure(1, weight = 1)
                self._root_window.rowconfigure(2, weight = 1)
                self._root_window.rowconfigure(3, weight = 1)
                self._root_window.rowconfigure(4, weight = 1)
                self._root_window.rowconfigure(5, weight = 1)
                self._root_window.rowconfigure(6, weight = 1)
                self._root_window.rowconfigure(7, weight = 1)
                self._root_window.rowconfigure(8, weight = 1)
                self._root_window.rowconfigure(9, weight = 1)
                self._root_window.columnconfigure(0, weight = 1)  
                
              
InitRB().start()
