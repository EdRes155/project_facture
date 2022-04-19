import tkinter as tk
from tkinter import ttk

class Invoice(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.frame_init = tk.Frame(self, width=1024, height=640, background='white')
        self.frame_init.pack()

class Add_Client(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=480, background='white')

        self.client_number = tk.StringVar()
        self.client_name = tk.StringVar()
        self.client_rfc = tk.StringVar()
        self.client_street = tk.StringVar()
        self.client_town = tk.StringVar()
        self.client_state = tk.StringVar()
        self.client_zip_code = tk.StringVar()
        self.client_telephone = tk.StringVar()
        self.client_email = tk.StringVar()

        font_global = ('Helvetica', 14)

        #Creacion de label
        ttk.Label(self.window, text='Cliente:', font=font_global, anchor='e').place(x=10, y=10, width=160)
        ttk.Label(self.window, text='Nombre Cliente:', font=font_global, anchor='e').place(x=10, y=50, width=160)
        ttk.Label(self.window, text='RFC:', font=font_global, anchor='e').place(x=10, y=90, width=160)
        ttk.Label(self.window, text='Calle/Numero:', font=font_global, anchor='e').place(x=10, y=130, width=160)
        ttk.Label(self.window, text='Colonia/Municipio:', font=font_global, anchor='e').place(x=10, y=170, width=160)
        ttk.Label(self.window, text='Estado/Pais:', font=font_global, anchor='e').place(x=10, y=210, width=160)
        ttk.Label(self.window, text='Codigo Postal:', font=font_global, anchor='e').place(x=10, y=250, width=160)
        ttk.Label(self.window, text='Telefono:', font=font_global, anchor='e').place(x=10, y=290, width=160)
        ttk.Label(self.window, text='Email:', font=font_global, anchor='e').place(x=10, y=330, width=160)
        
        #Creacion de entry
        ttk.Entry(self.window, textvariable=self.client_number, font=font_global).place(x=180, y=10, width=100)
        ttk.Entry(self.window, textvariable=self.client_name, font=font_global).place(x=180, y=50, width=300)
        ttk.Entry(self.window, textvariable=self.client_rfc, font=font_global).place(x=180, y=90, width=150)
        ttk.Entry(self.window, textvariable=self.client_street, font=font_global).place(x=180, y=130, width=180)
        ttk.Entry(self.window, textvariable=self.client_town, font=font_global).place(x=180, y=170, width=180)
        ttk.Entry(self.window, textvariable=self.client_state, font=font_global).place(x=180, y=210, width=180)
        ttk.Entry(self.window, textvariable=self.client_zip_code, font=font_global).place(x=180, y=250, width=100)
        ttk.Entry(self.window, textvariable=self.client_telephone, font=font_global).place(x=180, y=290, width=130)
        ttk.Entry(self.window, textvariable=self.client_email, font=font_global).place(x=180, y=330, width=200)

class Modified_Client(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=480, background='white')

class Delete_Client(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=480, background='white')
class Add_Product(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=480, background='white')

class Modified_Product(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=480, background='white')

class Delete_Product(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=480, background='white')

class Configuration(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=480, background='white')

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('--PROGRAMA DE FACTURACION--')
        self.geometry('1024x640')
        self.resizable(False, False)

        #Creacion e incializacion del menubar
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        #Creacion menubar Facturacion
        self.invoice = tk.Menu(self.menubar, tearoff=0)
        self.invoice.add_command(label='Facturar', command=lambda:self.__invoice())

        #Creacion menubar Clientes
        self.client = tk.Menu(self.menubar, tearoff=0)
        self.client.add_command(label='Agregar Cliente', command=lambda:self.__add_client())
        self.client.add_command(label='Modificar Cliente', command=lambda:self.__modified_client())
        self.client.add_command(label='Eliminar Cliente', command=lambda:self.__delete_client())

        #Creacion menubar Inventario
        self.inventary = tk.Menu(self.menubar, tearoff=0)
        self.inventary.add_command(label='Agregar Producto', command=lambda:self.__add_product())
        self.inventary.add_command(label='Modificar Producto', command=lambda:self.__modified_product())
        self.inventary.add_command(label='Eliminar Producto', command=lambda:self.__delete_product())

        #Creacion menubar Configuracion
        self.configuration = tk.Menu(self.menubar, tearoff=0)
        self.configuration.add_command(label='Configuracion', command=lambda:self.__configuration())
        self.configuration.add_command(label='Salir')

        #Se añadem todos los menubar
        self.menubar.add_cascade(label='Facturacion', menu=self.invoice)
        self.menubar.add_cascade(label='Clientes', menu=self.client)
        self.menubar.add_cascade(label='Inventario', menu=self.inventary)
        self.menubar.add_cascade(label='Configuracion', menu=self.configuration)

    def __invoice(self):
        frame_invoice = Invoice(self)
        frame_invoice.pack()

    def __add_client(self):
        frame_add_client = Add_Client(self)
        frame_add_client.pack()

    def __modified_client(self):
        frame_modified_client = Modified_Client(self)
        frame_modified_client.pack()

    def __delete_client(self):
        frame_delete_client = Delete_Client(self)
        frame_delete_client.pack()

    def __add_product(self):
        frame_add_product = Add_Product(self)
        frame_add_product.pack()

    def __modified_product(self):
        frame_modified_product = Modified_Product(self)
        frame_modified_product.pack()

    def __delete_product(self):
        frame_delete_product = Delete_Product(self)
        frame_delete_product.pack()

    def __configuration(self):
        frame_configuration = Configuration(self)
        frame_configuration.pack()

if __name__ == '__main__':
    app = App()
    frame = Invoice(app)
    app.mainloop()