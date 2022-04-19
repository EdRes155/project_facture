from ctypes.wintypes import HWINSTA
import tkinter as tk
from tkinter import ttk

from sqlalchemy import null

class Invoice(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.frame_init = tk.Frame(self, width=1024, height=640, background='red')
        self.frame_init.pack()

class Quotation(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.frame_init = tk.Frame(self, width=1024, height=640, background='black')
        self.frame_init.pack()

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('--PROGRAMA DE FACTURACION--')
        self.geometry('1024x640')
        self.resizable(False, False)

        #Variablas ocultar frames
        self.frame_forget = 3
        self.container_frames = null

        #Creacion e incializacion del menubar
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        #Creacion menubar Facturacion
        self.invoice = tk.Menu(self.menubar, tearoff=0)
        self.invoice.add_command(label='Facturar', command=lambda:self.__invoice())
        self.invoice.add_command(label='Cotizar', command=lambda:self.__quotation())

        #Creacion menubar Clientes
        self.client = tk.Menu(self.menubar, tearoff=0)
        self.client.add_command(label='Agregar Cliente')
        self.client.add_command(label='Modificar Cliente')
        self.client.add_command(label='Eliminar Cliente')

        #Creacion menubar Inventario
        self.inventary = tk.Menu(self.menubar, tearoff=0)
        self.inventary.add_command(label='Agregar Producto')
        self.inventary.add_command(label='Modificar Producto')
        self.inventary.add_command(label='Eliminar Producto')

        #Creacion menubar Configuracion
        self.configuration = tk.Menu(self.menubar, tearoff=0)
        self.configuration.add_command(label='Configuracion')
        self.configuration.add_command(label='Salir')

        #Se añadem todos los menubar
        self.menubar.add_cascade(label='Facturacion', menu=self.invoice)
        self.menubar.add_cascade(label='Clientes', menu=self.client)
        self.menubar.add_cascade(label='Inventario', menu=self.inventary)
        self.menubar.add_cascade(label='Configuracion', menu=self.configuration)

    def __invoice(self):
        frame_invoice = Invoice(self)
        if self.frame_forget == 1 and self.container_frames != frame_invoice:
            self.container_frames.pack_forget()
            frame_invoice.pack()
            self.frame_forget = 2
        elif self.frame_forget == 2:
            self.container_frames.pack_forget()
            frame_invoice.pack()
            self.frame_forget = 3
        else:
            frame_invoice.pack()
            self.container_frames = frame_invoice
            self.frame_forget = 1

    def __quotation(self):
        frame_quotation = Quotation(self)
        if self.frame_forget == 1 and self.container_frames != frame_quotation:
            self.container_frames.pack_forget()
            frame_quotation.pack()
            self.frame_forget = 2
        elif self.frame_forget == 2:
            self.container_frames.pack_forget()
            frame_quotation.pack()
            self.frame_forget = 3
        else:
            frame_quotation.pack()
            self.container_frames = frame_quotation
            self.frame_forget = 1

if __name__ == '__main__':
    app = App()
    frame = Invoice(app)
    app.mainloop()