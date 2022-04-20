import tkinter as tk
from tkinter import ttk

class Invoice(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.frame = tk.Frame(self, width=1024, height=640, background='white')
        self.frame.pack()

        self.invoice_label = tk.LabelFrame(self.frame, text='Facturar', font=('Helvetica', 20), background='white')
        self.invoice_label.place(x=5, y=5, width=1014, height=630)

        self.client_number = tk.StringVar()
        self.client_name = tk.StringVar()
        self.client_rfc = tk.StringVar()
        self.client_street = tk.StringVar()
        self.client_town = tk.StringVar()
        self.client_state = tk.StringVar()
        self.client_zip_code = tk.StringVar()
        self.client_telephone = tk.StringVar()
        self.client_email = tk.StringVar()
        self.product_code = tk.StringVar()

        font_global = ('Roboto', 14)
        font_global1 = ('Roboto', 12)

        #Datos del cliente tras busqueda
        ttk.Label(self.invoice_label, text='Cliente:', font=font_global, anchor='e', background='white').place(x=10, y=10, width=155)       
        ttk.Label(self.invoice_label, text='Nombre Cliente:', font=font_global, anchor='e', background='white').place(x=10, y=50, width=155)       
        ttk.Label(self.invoice_label, text='RFC:', font=font_global, anchor='e', background='white').place(x=480, y=50, width=155)       
        ttk.Label(self.invoice_label, text='Calle/Numero:', font=font_global, anchor='e', background='white').place(x=10, y=90, width=155)       
        ttk.Label(self.invoice_label, text='Colonia/Municipio:', font=font_global, anchor='e', background='white').place(x=10, y=130, width=155)       
        ttk.Label(self.invoice_label, text='Estado/Pais:', font=font_global, anchor='e', background='white').place(x=10, y=170, width=155)       
        ttk.Label(self.invoice_label, text='Codigo Postal:', font=font_global, anchor='e', background='white').place(x=10, y=210, width=155)       
        ttk.Label(self.invoice_label, text='Telefono:', font=font_global, anchor='e', background='white').place(x=480, y=90, width=155)       
        ttk.Label(self.invoice_label, text='Email:', font=font_global, anchor='e', background='white').place(x=480, y=130, width=155) 

        ttk.Entry(self.invoice_label, textvariable=self.client_number, font=font_global1).place(x=170, y=10, width=100)      
        ttk.Entry(self.invoice_label, textvariable=self.client_name, font=font_global1, state='disabled').place(x=170, y=50, width=300)      
        ttk.Entry(self.invoice_label, textvariable=self.client_rfc, font=font_global1, state='disabled').place(x=640, y=50, width=150)      
        ttk.Entry(self.invoice_label, textvariable=self.client_street, font=font_global1, state='disabled').place(x=170, y=90, width=180)      
        ttk.Entry(self.invoice_label, textvariable=self.client_town, font=font_global1, state='disabled').place(x=170, y=130, width=230)      
        ttk.Entry(self.invoice_label, textvariable=self.client_state, font=font_global1, state='disabled').place(x=170, y=170, width=200)      
        ttk.Entry(self.invoice_label, textvariable=self.client_zip_code, font=font_global1, state='disabled').place(x=170, y=210, width=100)      
        ttk.Entry(self.invoice_label, textvariable=self.client_telephone, font=font_global1, state='disabled').place(x=640, y=90, width=130)      
        ttk.Entry(self.invoice_label, textvariable=self.client_email, font=font_global1, state='disabled').place(x=640, y=130, width=280)      

        ttk.Button(self.invoice_label, text='Buscar').place(x=280, y=6, width=100)

        #Agregar producto a factura
        ttk.Label(self.invoice_label, text='Codigo:', font=font_global, anchor='e', background='white').place(x=10, y=260, width=150)
        ttk.Entry(self.invoice_label, textvariable=self.product_code, font=font_global).place(x=170, y=260, width=400)
        ttk.Button(self.invoice_label, text='Insertar').place(x=580, y=258, width=100)
        ttk.Button(self.invoice_label, text='Buscar').place(x=690, y=258, width=100)

        #Tabla para los productos
        columns = ('#0', '#1', "#2", '#3', '#4')
        self.product_table = ttk.Treeview(self.invoice_label, columns=columns, height=13)
        self.product_table.heading('#0', text='Codigo')
        self.product_table.heading('#1', text='Descripcion')
        self.product_table.heading('#2', text='Precio')
        self.product_table.heading('#3', text='Cantidad')
        self.product_table.heading('#4', text='Importe')
        self.product_table.heading(0, text='Importe')
        self.product_table.column('#0', width=138)
        self.product_table.column('#1', width=428)
        self.product_table.column('#2', width=140)
        self.product_table.column('#3', width=140)
        self.product_table.column('#4', width=150)
        self.product_table.place(x=10, y=300, width=984)


#Clase añadir un cliente
class Add_Client(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=480, background='white')
        self.window.title('-- AGREGAR CLIENTE --')
        self.window.resizable(False, False)

        #Labelframe cliente
        self.client_label = tk.LabelFrame(self.window, text='Cliente', font=('Roboto', 20), background='white')
        self.client_label.place(x=5, y=5, width=710, height=470)

        self.client_number = tk.StringVar()
        self.client_name = tk.StringVar()
        self.client_rfc = tk.StringVar()
        self.client_street = tk.StringVar()
        self.client_town = tk.StringVar()
        self.client_state = tk.StringVar()
        self.client_zip_code = tk.StringVar()
        self.client_telephone = tk.StringVar()
        self.client_email = tk.StringVar()

        font_global = ('Roboto', 14)

        #Creacion de label
        ttk.Label(self.client_label, text='Cliente:', font=font_global, anchor='e', background='white').place(x=10, y=10, width=160)
        ttk.Label(self.client_label, text='Nombre Cliente:', font=font_global, anchor='e', background='white').place(x=10, y=50, width=160)
        ttk.Label(self.client_label, text='RFC:', font=font_global, anchor='e', background='white').place(x=10, y=90, width=160)
        ttk.Label(self.client_label, text='Calle/Numero:', font=font_global, anchor='e', background='white').place(x=10, y=130, width=160)
        ttk.Label(self.client_label, text='Colonia/Municipio:', font=font_global, anchor='e', background='white').place(x=10, y=170, width=160)
        ttk.Label(self.client_label, text='Estado/Pais:', font=font_global, anchor='e', background='white').place(x=10, y=210, width=160)
        ttk.Label(self.client_label, text='Codigo Postal:', font=font_global, anchor='e', background='white').place(x=10, y=250, width=160)
        ttk.Label(self.client_label, text='Telefono:', font=font_global, anchor='e', background='white').place(x=10, y=290, width=160)
        ttk.Label(self.client_label, text='Email:', font=font_global, anchor='e', background='white').place(x=10, y=330, width=160)
        
        #Creacion de entry
        ttk.Entry(self.client_label, textvariable=self.client_number, font=font_global).place(x=180, y=10, width=100)
        ttk.Entry(self.client_label, textvariable=self.client_name, font=font_global).place(x=180, y=50, width=300)
        ttk.Entry(self.client_label, textvariable=self.client_rfc, font=font_global).place(x=180, y=90, width=150)
        ttk.Entry(self.client_label, textvariable=self.client_street, font=font_global).place(x=180, y=130, width=180)
        ttk.Entry(self.client_label, textvariable=self.client_town, font=font_global).place(x=180, y=170, width=180)
        ttk.Entry(self.client_label, textvariable=self.client_state, font=font_global).place(x=180, y=210, width=180)
        ttk.Entry(self.client_label, textvariable=self.client_zip_code, font=font_global).place(x=180, y=250, width=100)
        ttk.Entry(self.client_label, textvariable=self.client_telephone, font=font_global).place(x=180, y=290, width=130)
        ttk.Entry(self.client_label, textvariable=self.client_email, font=font_global).place(x=180, y=330, width=200)

        ttk.Button(self.client_label, text='Aceptar').place(x=20, y=380, width=120)
        ttk.Button(self.client_label, text='Cancelar', command=lambda:self.window.destroy()).place(x=570, y=380, width=120)

    def __save(self):
        pass

#Clase modificar cliente
class Modified_Client(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=480, background='white')
        self.window.title('-- MODIFICAR CLIENTE --')
        self.window.resizable(False, False)

        self.check_label = tk.LabelFrame(self.window, text='Modificar Cliente', font=('Roboto', 20), background='white')
        self.check_label.place(x=200, y=130, width=290, height=150)

        self.font_global = ('Roboto', 14)

        self.client_number = tk.StringVar()

        ttk.Label(self.check_label, text='Cliente:', font=self.font_global, background='white', anchor='e').place(x=10, y=20, width=80)
        ttk.Entry(self.check_label, textvariable=self.client_number, font=self.font_global).place(x=95, y=20, width=170)

        ttk.Button(self.check_label, text='Entrar',command=lambda:self.__interface()).place(x=95, y=60, width=100)

    def __interface(self):
        self.check_label.pack_forget()
        self.client_label = tk.LabelFrame(self.window, text='Cliente', font=('Roboto', 20), background='white')
        self.client_label.place(x=5, y=5, width=710, height=470)

        self.client_number = tk.StringVar()
        self.client_name = tk.StringVar()
        self.client_rfc = tk.StringVar()
        self.client_street = tk.StringVar()
        self.client_town = tk.StringVar()
        self.client_state = tk.StringVar()
        self.client_zip_code = tk.StringVar()
        self.client_telephone = tk.StringVar()
        self.client_email = tk.StringVar()

        font_global = ('Roboto', 14)

        #Creacion de label
        ttk.Label(self.client_label, text='Cliente:', font=font_global, anchor='e', background='white').place(x=10, y=10, width=160)
        ttk.Label(self.client_label, text='Nombre Cliente:', font=font_global, anchor='e', background='white').place(x=10, y=50, width=160)
        ttk.Label(self.client_label, text='RFC:', font=font_global, anchor='e', background='white').place(x=10, y=90, width=160)
        ttk.Label(self.client_label, text='Calle/Numero:', font=font_global, anchor='e', background='white').place(x=10, y=130, width=160)
        ttk.Label(self.client_label, text='Colonia/Municipio:', font=font_global, anchor='e', background='white').place(x=10, y=170, width=160)
        ttk.Label(self.client_label, text='Estado/Pais:', font=font_global, anchor='e', background='white').place(x=10, y=210, width=160)
        ttk.Label(self.client_label, text='Codigo Postal:', font=font_global, anchor='e', background='white').place(x=10, y=250, width=160)
        ttk.Label(self.client_label, text='Telefono:', font=font_global, anchor='e', background='white').place(x=10, y=290, width=160)
        ttk.Label(self.client_label, text='Email:', font=font_global, anchor='e', background='white').place(x=10, y=330, width=160)
        
        #Creacion de entry
        ttk.Entry(self.client_label, textvariable=self.client_number, font=font_global).place(x=180, y=10, width=100)
        ttk.Entry(self.client_label, textvariable=self.client_name, font=font_global).place(x=180, y=50, width=300)
        ttk.Entry(self.client_label, textvariable=self.client_rfc, font=font_global).place(x=180, y=90, width=150)
        ttk.Entry(self.client_label, textvariable=self.client_street, font=font_global).place(x=180, y=130, width=180)
        ttk.Entry(self.client_label, textvariable=self.client_town, font=font_global).place(x=180, y=170, width=180)
        ttk.Entry(self.client_label, textvariable=self.client_state, font=font_global).place(x=180, y=210, width=180)
        ttk.Entry(self.client_label, textvariable=self.client_zip_code, font=font_global).place(x=180, y=250, width=100)
        ttk.Entry(self.client_label, textvariable=self.client_telephone, font=font_global).place(x=180, y=290, width=130)
        ttk.Entry(self.client_label, textvariable=self.client_email, font=font_global).place(x=180, y=330, width=200)

        ttk.Button(self.client_label, text='Aceptar').place(x=20, y=380, width=120)
        ttk.Button(self.client_label, text='Cancelar', command=lambda:self.__cancel()).place(x=570, y=380, width=120)

    def __save(self):
        pass

    def __cancel(self):
        self.client_label.place_forget()
        self.check_label.place(x=200, y=130, width=290, height=150)

class Delete_Client(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=480, background='white')
        self.window.title('-- ELIMINAR CLIENTE --')
        self.window.resizable(False, False)

        self.check_label = tk.LabelFrame(self.window, text='Eliminar Cliente', font=('Roboto', 20), background='white')
        self.check_label.place(x=200, y=130, width=290, height=150)

        self.font_global = ('Roboto', 14)

        self.client_number = tk.StringVar()

        ttk.Label(self.check_label, text='Cliente:', font=self.font_global, background='white', anchor='e').place(x=10, y=20, width=80)
        ttk.Entry(self.check_label, textvariable=self.client_number, font=self.font_global).place(x=95, y=20, width=170)

        ttk.Button(self.check_label, text='Entrar',command=lambda:self.__interface()).place(x=95, y=60, width=100)

    def __interface(self):
        self.check_label.pack_forget()
        self.client_label = tk.LabelFrame(self.window, text='Cliente', font=('Roboto', 20), background='white')
        self.client_label.place(x=5, y=5, width=710, height=470)

        self.client_number = tk.StringVar()
        self.client_name = tk.StringVar()
        self.client_rfc = tk.StringVar()
        self.client_street = tk.StringVar()
        self.client_town = tk.StringVar()
        self.client_state = tk.StringVar()
        self.client_zip_code = tk.StringVar()
        self.client_telephone = tk.StringVar()
        self.client_email = tk.StringVar()

        font_global = ('Roboto', 14)

        #Creacion de label
        ttk.Label(self.client_label, text='Cliente:', font=font_global, anchor='e', background='white').place(x=10, y=10, width=160)
        ttk.Label(self.client_label, text='Nombre Cliente:', font=font_global, anchor='e', background='white').place(x=10, y=50, width=160)
        ttk.Label(self.client_label, text='RFC:', font=font_global, anchor='e', background='white').place(x=10, y=90, width=160)
        ttk.Label(self.client_label, text='Calle/Numero:', font=font_global, anchor='e', background='white').place(x=10, y=130, width=160)
        ttk.Label(self.client_label, text='Colonia/Municipio:', font=font_global, anchor='e', background='white').place(x=10, y=170, width=160)
        ttk.Label(self.client_label, text='Estado/Pais:', font=font_global, anchor='e', background='white').place(x=10, y=210, width=160)
        ttk.Label(self.client_label, text='Codigo Postal:', font=font_global, anchor='e', background='white').place(x=10, y=250, width=160)
        ttk.Label(self.client_label, text='Telefono:', font=font_global, anchor='e', background='white').place(x=10, y=290, width=160)
        ttk.Label(self.client_label, text='Email:', font=font_global, anchor='e', background='white').place(x=10, y=330, width=160)
        
        #Creacion de entry
        ttk.Entry(self.client_label, textvariable=self.client_number, font=font_global).place(x=180, y=10, width=100)
        ttk.Entry(self.client_label, textvariable=self.client_name, font=font_global).place(x=180, y=50, width=300)
        ttk.Entry(self.client_label, textvariable=self.client_rfc, font=font_global).place(x=180, y=90, width=150)
        ttk.Entry(self.client_label, textvariable=self.client_street, font=font_global).place(x=180, y=130, width=180)
        ttk.Entry(self.client_label, textvariable=self.client_town, font=font_global).place(x=180, y=170, width=180)
        ttk.Entry(self.client_label, textvariable=self.client_state, font=font_global).place(x=180, y=210, width=180)
        ttk.Entry(self.client_label, textvariable=self.client_zip_code, font=font_global).place(x=180, y=250, width=100)
        ttk.Entry(self.client_label, textvariable=self.client_telephone, font=font_global).place(x=180, y=290, width=130)
        ttk.Entry(self.client_label, textvariable=self.client_email, font=font_global).place(x=180, y=330, width=200)

        ttk.Button(self.client_label, text='Aceptar').place(x=20, y=380, width=120)
        ttk.Button(self.client_label, text='Cancelar', command=lambda:self.__cancel()).place(x=570, y=380, width=120)

    def __save(self):
        pass

    def __cancel(self):
        self.client_label.place_forget()
        self.check_label.place(x=200, y=130, width=290, height=150)

class Add_Product(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=360, background='white')
        self.window.title('-- AGREGAR PRODUCTO --')
        self.window.resizable(False, False)

        self.product_label = tk.LabelFrame(self.window, text='Producto', font=('Roboto', 20), background='white')
        self.product_label.place(x=5, y=5, width=710, height=350)

        self.product_code = tk.StringVar()
        self.product_description = tk.StringVar()
        self.product_price = tk.StringVar()
        self.product_price_shop = tk.StringVar()
        self.product_price_shop_iva = tk.StringVar()
        self.product_inventary = tk.StringVar()

        font_global = ('Roboto', 14)

        ttk.Label(self.product_label, text='Codigo:', font=font_global, anchor='e', background='white').place(x=10, y=10, width=200)
        ttk.Label(self.product_label, text='Descripcion:', font=font_global, anchor='e', background='white').place(x=10, y=50, width=200)
        ttk.Label(self.product_label, text='Precio Costo:', font=font_global, anchor='e', background='white').place(x=10, y=90, width=200)
        ttk.Label(self.product_label, text='Precio Venta(sin IVA):', font=font_global, anchor='e', background='white').place(x=10, y=130, width=200)
        ttk.Label(self.product_label, text='Precio Venta(con IVA):', font=font_global, anchor='e', background='white').place(x=10, y=170, width=200)
        ttk.Label(self.product_label, text='Cantidad:', font=font_global, anchor='e', background='white').place(x=10, y=210, width=200)

        ttk.Entry(self.product_label, textvariable=self.product_code, font=font_global).place(x=220, y=10, width=120)
        ttk.Entry(self.product_label, textvariable=self.product_description, font=font_global).place(x=220, y=50, width=350)
        ttk.Entry(self.product_label, textvariable=self.product_price, font=font_global).place(x=220, y=90, width=100)
        ttk.Entry(self.product_label, textvariable=self.product_price_shop, font=font_global).place(x=220, y=130, width=100)
        ttk.Entry(self.product_label, textvariable=self.product_price_shop_iva, font=font_global).place(x=220, y=170, width=100)
        ttk.Entry(self.product_label, textvariable=self.product_inventary, font=font_global).place(x=220, y=210, width=80)

        ttk.Button(self.product_label, text='Aceptar').place(x=20, y=260, width=120)
        ttk.Button(self.product_label, text='Cancelar').place(x=570, y=260, width=120)

    def __save(self):
        pass

    def __cancel(self):
        pass

class Modified_Product(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=360, background='white')
        self.window.title('-- MODIFICAR PRODUCTO --')
        self.window.resizable(False, False)

        self.check_label = tk.LabelFrame(self.window, text='Modificar Producto', font=('Roboto', 20), background='white')
        self.check_label.place(x=200, y=70, width=290, height=150)

        self.font_global = ('Roboto', 14)

        self.product_code = tk.StringVar()

        ttk.Label(self.check_label, text='Producto:', font=self.font_global, background='white', anchor='e').place(x=10, y=20, width=85)
        ttk.Entry(self.check_label, textvariable=self.product_code, font=self.font_global).place(x=100, y=20, width=165)

        ttk.Button(self.check_label, text='Entrar',command=lambda:self.__interface()).place(x=95, y=60, width=100)

    def __interface(self):
        self.check_label.place_forget()
        self.product_label = tk.LabelFrame(self.window, text='Producto', font=('Roboto', 20), background='white')
        self.product_label.place(x=5, y=5, width=710, height=350)

        self.product_code = tk.StringVar()
        self.product_description = tk.StringVar()
        self.product_price = tk.StringVar()
        self.product_price_shop = tk.StringVar()
        self.product_price_shop_iva = tk.StringVar()
        self.product_inventary = tk.StringVar()

        font_global = ('Roboto', 14)

        ttk.Label(self.product_label, text='Codigo:', font=font_global, anchor='e', background='white').place(x=10, y=10, width=200)
        ttk.Label(self.product_label, text='Descripcion:', font=font_global, anchor='e', background='white').place(x=10, y=50, width=200)
        ttk.Label(self.product_label, text='Precio Costo:', font=font_global, anchor='e', background='white').place(x=10, y=90, width=200)
        ttk.Label(self.product_label, text='Precio Venta(sin IVA):', font=font_global, anchor='e', background='white').place(x=10, y=130, width=200)
        ttk.Label(self.product_label, text='Precio Venta(con IVA):', font=font_global, anchor='e', background='white').place(x=10, y=170, width=200)
        ttk.Label(self.product_label, text='Cantidad:', font=font_global, anchor='e', background='white').place(x=10, y=210, width=200)

        ttk.Entry(self.product_label, textvariable=self.product_code, font=font_global).place(x=220, y=10, width=120)
        ttk.Entry(self.product_label, textvariable=self.product_description, font=font_global).place(x=220, y=50, width=350)
        ttk.Entry(self.product_label, textvariable=self.product_price, font=font_global).place(x=220, y=90, width=100)
        ttk.Entry(self.product_label, textvariable=self.product_price_shop, font=font_global).place(x=220, y=130, width=100)
        ttk.Entry(self.product_label, textvariable=self.product_price_shop_iva, font=font_global).place(x=220, y=170, width=100)
        ttk.Entry(self.product_label, textvariable=self.product_inventary, font=font_global).place(x=220, y=210, width=80)

        ttk.Button(self.product_label, text='Aceptar').place(x=20, y=260, width=120)
        ttk.Button(self.product_label, text='Cancelar', command=lambda:self.__cancel()).place(x=570, y=260, width=120)

    def __save(self):
        pass

    def __cancel(self):
        self.product_label.place_forget()
        self.check_label.place(x=200, y=70, width=290, height=150)


class Delete_Product(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=360, background='white')
        self.window.title('-- ELIMINAR PRODUCTO --')
        self.window.resizable(False, False)

        self.check_label = tk.LabelFrame(self.window, text='Eliminar Producto', font=('Roboto', 20), background='white')
        self.check_label.place(x=200, y=70, width=290, height=150)

        self.font_global = ('Roboto', 14)

        self.product_code = tk.StringVar()

        ttk.Label(self.check_label, text='Producto:', font=self.font_global, background='white', anchor='e').place(x=10, y=20, width=85)
        ttk.Entry(self.check_label, textvariable=self.product_code, font=self.font_global).place(x=100, y=20, width=165)

        ttk.Button(self.check_label, text='Entrar',command=lambda:self.__interface()).place(x=95, y=60, width=100)

    def __interface(self):
        self.check_label.place_forget()
        self.product_label = tk.LabelFrame(self.window, text='Producto', font=('Roboto', 20), background='white')
        self.product_label.place(x=5, y=5, width=710, height=350)

        self.product_code = tk.StringVar()
        self.product_description = tk.StringVar()
        self.product_price = tk.StringVar()
        self.product_price_shop = tk.StringVar()
        self.product_price_shop_iva = tk.StringVar()
        self.product_inventary = tk.StringVar()

        font_global = ('Roboto', 14)

        ttk.Label(self.product_label, text='Codigo:', font=font_global, anchor='e', background='white').place(x=10, y=10, width=200)
        ttk.Label(self.product_label, text='Descripcion:', font=font_global, anchor='e', background='white').place(x=10, y=50, width=200)
        ttk.Label(self.product_label, text='Precio Costo:', font=font_global, anchor='e', background='white').place(x=10, y=90, width=200)
        ttk.Label(self.product_label, text='Precio Venta(sin IVA):', font=font_global, anchor='e', background='white').place(x=10, y=130, width=200)
        ttk.Label(self.product_label, text='Precio Venta(con IVA):', font=font_global, anchor='e', background='white').place(x=10, y=170, width=200)
        ttk.Label(self.product_label, text='Cantidad:', font=font_global, anchor='e', background='white').place(x=10, y=210, width=200)

        ttk.Entry(self.product_label, textvariable=self.product_code, font=font_global).place(x=220, y=10, width=120)
        ttk.Entry(self.product_label, textvariable=self.product_description, font=font_global).place(x=220, y=50, width=350)
        ttk.Entry(self.product_label, textvariable=self.product_price, font=font_global).place(x=220, y=90, width=100)
        ttk.Entry(self.product_label, textvariable=self.product_price_shop, font=font_global).place(x=220, y=130, width=100)
        ttk.Entry(self.product_label, textvariable=self.product_price_shop_iva, font=font_global).place(x=220, y=170, width=100)
        ttk.Entry(self.product_label, textvariable=self.product_inventary, font=font_global).place(x=220, y=210, width=80)

        ttk.Button(self.product_label, text='Aceptar').place(x=20, y=260, width=120)
        ttk.Button(self.product_label, text='Cancelar', command=lambda:self.__cancel()).place(x=570, y=260, width=120)

    def __save(self):
        pass

    def __cancel(self):
        self.product_label.place_forget()
        self.check_label.place(x=200, y=70, width=290, height=150)

class Configuration(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.window = tk.Toplevel(self, width=720, height=480, background='white')

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('-- PROGRAMA DE FACTURACION --')
        self.geometry('1024x640')
        self.resizable(False, False)
        self.config(background='white')

        #Creacion e incializacion del menubar
        self.menubar = tk.Menu(self, background='white')
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

        self.style = ttk.Style()

        self.style.theme_use('vista')
        self.style.theme_settings('vista', settings={
            'TButton': {
                'configure': {'font': 'roboto 14', 'focuscolor': ''},
            }
        })

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