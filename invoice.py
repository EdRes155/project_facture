from pathlib import Path
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import MultiColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.canvas.color.color import HexColor, X11Color
from borb.pdf.pdf import PDF
from decimal import Decimal
from datetime import datetime

class Make_Invoice():

    def __init__(self, Table_Bussines, Table_Client, Table_Credit, Table_Product_Information, Table_Product, Table_Total,Table_Observations, Table_DatesAditional):
        doc: Document = Document()

        page: Page = Page()

        doc.append_page(page)

        layout: PageLayout = MultiColumnLayout(page, number_of_columns=1, horizontal_margin=Decimal(5), vertical_margin=Decimal(5))
        layout.add(Table_Bussines)
        layout.add(Table_Client)
        layout.add(Table_Credit)
        layout.add(Table_Product_Information)        
        layout.add(Table_Product)
        layout.add(Table_Total)
        layout.add(Table_Observations)
        layout.add(Table_DatesAditional)

        with open('prueba.pdf', 'wb') as pdf_file_handle:
            PDF.dumps(pdf_file_handle, doc)

    def InformationBussines(name_bussines, information_address, information_general, number_invoice):
        Table_Bussines: FixedColumnWidthTable = FixedColumnWidthTable(number_of_columns=3, number_of_rows=4, column_widths=[Decimal(1), Decimal(2), Decimal(1)])
        Table_Bussines.add(TableCell(Paragraph(number_invoice, font='Helvetica-bold', font_size=Decimal(14), horizontal_alignment=Alignment.CENTERED, padding_bottom=Decimal(5))))
        Table_Bussines.add(TableCell(Paragraph('Remision de Factura', font='Helvetica-bold', font_size=Decimal(14), horizontal_alignment=Alignment.CENTERED, padding_bottom=Decimal(5)), col_span=2, background_color=HexColor('9D9D9D')))
        Table_Bussines.add(TableCell(Image( Path('logo.png'), width=Decimal(128), height=Decimal(48), horizontal_alignment=Alignment.CENTERED), row_span=3))
        Table_Bussines.add(TableCell(Paragraph(name_bussines, font='Helvetica-bold', font_size=Decimal(12), horizontal_alignment=Alignment.CENTERED), col_span=2))
        Table_Bussines.add(TableCell(Paragraph(information_address, font='Helvetica', font_size=Decimal(10), horizontal_alignment=Alignment.CENTERED), col_span=2))
        Table_Bussines.add(TableCell(Paragraph(information_general, font='Helvetica', font_size=Decimal(10), horizontal_alignment=Alignment.CENTERED), col_span=2))
        Table_Bussines.set_padding_on_all_cells(Decimal(1), Decimal(2), Decimal(1), Decimal(2))
        Table_Bussines.no_borders()
        return Table_Bussines

    def InformationClient(info_client=[]):
        Table_Client: FixedColumnWidthTable = FixedColumnWidthTable(number_of_rows=9, number_of_columns=4)
        Table_Client.add(TableCell(Paragraph('Cliente: %s' % info_client[0], font='Helvetica-bold', font_size=Decimal(8), padding_bottom=Decimal(2.5)), col_span=2, background_color=HexColor('9D9D9D')))
        Table_Client.add(TableCell(Paragraph('Destinatario', font='Helvetica-bold', font_size=Decimal(8), padding_bottom=Decimal(2.5)), col_span=2, background_color=HexColor('9D9D9D')))
        Table_Client.add(TableCell(Paragraph(info_client[1], font='Helvetica', font_size=Decimal(8), padding_bottom=False, padding_top=False), col_span=2))
        Table_Client.add(TableCell(Paragraph(info_client[1],  font='Helvetica', font_size=Decimal(8), padding_bottom=False, padding_top=False), col_span=2))
        Table_Client.add(TableCell(Paragraph(info_client[3], font='Helvetica', font_size=Decimal(8)), col_span=2))
        Table_Client.add(TableCell(Paragraph(info_client[3], font='Helvetica', font_size=Decimal(8)), col_span=2))
        Table_Client.add(TableCell(Paragraph(info_client[4], font='Helvetica', font_size=Decimal(8)), col_span=2))
        Table_Client.add(TableCell(Paragraph(info_client[4], font='Helvetica', font_size=Decimal(8)), col_span=2))
        Table_Client.add(TableCell(Paragraph(info_client[5], font='Helvetica', font_size=Decimal(8)), col_span=2))
        Table_Client.add(TableCell(Paragraph(info_client[5], font='Helvetica',  font_size=Decimal(8)), col_span=2))
        Table_Client.add(TableCell(Paragraph('C.P. %s' % info_client[6], font='Helvetica', font_size=Decimal(8)), col_span=2))
        Table_Client.add(TableCell(Paragraph('C.P. %s' % info_client[6], font='Helvetica', font_size=Decimal(8)), col_span=2))
        Table_Client.add(TableCell(Paragraph('RFC: %s' % info_client[2], font='Helvetica', font_size=Decimal(8)), col_span=2))
        Table_Client.add(TableCell(Paragraph(' ', font='Helvetica', font_size=Decimal(8)), col_span=2))
        Table_Client.add(TableCell(Paragraph('Telf. %s' % info_client[7], font='Helvetica', font_size=Decimal(8)), col_span=2))
        Table_Client.add(TableCell(Paragraph(' ', font='Helvetica', font_size=Decimal(8)), col_span=2))
        Table_Client.add(TableCell(Paragraph('Email: %s' % info_client[8], font='Helvetica', font_size=Decimal(8)), col_span=2))
        Table_Client.add(TableCell(Paragraph(' ', font='Helvetica', font_size=Decimal(8)), col_span=2))
        Table_Client.set_padding_on_all_cells(Decimal(0.5), Decimal(0.5), Decimal(0.5), Decimal(0.5))
        Table_Client.no_borders()
        return Table_Client

    def InformationGeneral():
        now = datetime.now()
        Table_Credit: FixedColumnWidthTable = FixedColumnWidthTable(number_of_columns=3, number_of_rows=1, column_widths=(Decimal(1), Decimal(2), Decimal(1)))
        Table_Credit.add(TableCell(Paragraph('Inicio de credito %d/%d/%d' % (now.day, now.month, now.year), font='Helvetica', font_size=Decimal(8), padding_bottom=Decimal(2.5), horizontal_alignment=Alignment.CENTERED), background_color=HexColor('9D9D9D')))
        Table_Credit.add(TableCell(Paragraph('Condicion de pago 10 Dias', font='Helvetica', font_size=Decimal(8), padding_bottom=Decimal(2.5), horizontal_alignment=Alignment.CENTERED), background_color=HexColor('9D9D9D')))
        Table_Credit.add(TableCell(Paragraph('Vencimiento %d/%d/%d' % (now.day+10, now.month, now.year), font='Helvetica', font_size=Decimal(8), padding_bottom=Decimal(2.5), horizontal_alignment=Alignment.CENTERED), background_color=HexColor('9D9D9D')))
        Table_Credit.set_padding_on_all_cells(Decimal(1), Decimal(1), Decimal(1), Decimal(1))
        Table_Credit.no_borders()
        return Table_Credit

    def InformationTableProduct():
        Table_Product_Information: FixedColumnWidthTable = FixedColumnWidthTable(number_of_columns=5, number_of_rows=1, column_widths=(Decimal(0.8), Decimal(2.5), Decimal(0.6), Decimal(0.5), Decimal(0.8)))
        Table_Product_Information.add(Paragraph('Codigo', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED, padding_bottom=Decimal(2.5), padding_top=Decimal(0.02)))
        Table_Product_Information.add(Paragraph('Descripcion', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED, padding_bottom=Decimal(2.5), padding_top=Decimal(0.02)))
        Table_Product_Information.add(Paragraph('Precio Unitario', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED, padding_bottom=Decimal(2.5), padding_top=Decimal(0.02)))
        Table_Product_Information.add(Paragraph('Cantidad', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED, padding_bottom=Decimal(2.5), padding_top=Decimal(0.02)))
        Table_Product_Information.add(Paragraph('Importe', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED, padding_bottom=Decimal(2.5), padding_top=Decimal(0.02)))
        Table_Product_Information.set_padding_on_all_cells(Decimal(1), Decimal(1), Decimal(1), Decimal(1))
        Table_Product_Information.set_background_color_on_all_cells(HexColor('9D9D9D'))
        Table_Product_Information.no_borders()
        return Table_Product_Information

    def InformationProduct(info_product=[]):
        Table_Product: FixedColumnWidthTable = FixedColumnWidthTable(number_of_columns=5, number_of_rows=(len(info_product)), column_widths=(Decimal(0.8), Decimal(2.5), Decimal(0.6), Decimal(0.5), Decimal(0.8)))
        for product in info_product:
            print(product)
            Table_Product.add(Paragraph(product[0], font='Helvetica', font_size=Decimal(8), padding_bottom=Decimal(2.5), horizontal_alignment=Alignment.CENTERED))
            Table_Product.add(Paragraph(product[1], font='Helvetica', font_size=Decimal(8), padding_bottom=Decimal(2.5)))
            Table_Product.add(Paragraph('$ %d.00' % product[2], font='Helvetica', font_size=Decimal(8), padding_bottom=Decimal(2.5), horizontal_alignment=Alignment.RIGHT))
            Table_Product.add(Paragraph(str(product[3]), font='Helvetica', font_size=Decimal(8), padding_bottom=Decimal(2.5), horizontal_alignment=Alignment.CENTERED))
            Table_Product.add(Paragraph('$ %d.00' % product[4], font='Helvetica', font_size=Decimal(8), padding_bottom=Decimal(2.5), horizontal_alignment=Alignment.RIGHT))
        Table_Product.set_padding_on_all_cells(Decimal(1), Decimal(1), Decimal(1), Decimal(1))
        Table_Product.even_odd_row_colors(X11Color('LightGray'), X11Color('White'))
        Table_Product.no_borders()
        return Table_Product

    def Total(subtotal, anticipo):
        Table_Total: FixedColumnWidthTable = FixedColumnWidthTable(number_of_columns=5, number_of_rows=3, column_widths=(Decimal(0.8), Decimal(2), Decimal(0.8), Decimal(0.8), Decimal(0.8)))
        Table_Total.add(TableCell(Paragraph('Banco', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED,), background_color=X11Color('LightGray')))
        Table_Total.add(TableCell(Paragraph('Numero de Cuenta', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED), background_color=X11Color('LightGray')))
        Table_Total.add(TableCell(Paragraph('Referencia', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED), background_color=X11Color('LightGray')))
        Table_Total.add(Paragraph('Subtotal:', font='Helvetica-bold', font_size=Decimal(8), padding_bottom=Decimal(2.5), horizontal_alignment=Alignment.RIGHT))
        Table_Total.add(Paragraph('$ %d.00' % subtotal, font='Helvetica', font_size=Decimal(8), padding_bottom=Decimal(2.5), horizontal_alignment=Alignment.RIGHT))
        Table_Total.add(TableCell(Paragraph('Santander', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED), background_color=X11Color('White')))
        Table_Total.add(TableCell(Paragraph('892376438', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED), background_color=X11Color('White')))
        Table_Total.add(TableCell(Paragraph('Factura', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED), background_color=X11Color('White')))
        Table_Total.add(Paragraph('Anticipo:', font='Helvetica-bold', font_size=Decimal(8), padding_bottom=Decimal(2.5), horizontal_alignment=Alignment.RIGHT))
        Table_Total.add(Paragraph('$ %d.00' % anticipo, font='Helvetica', font_size=Decimal(8), padding_bottom=Decimal(2.5), horizontal_alignment=Alignment.RIGHT))
        Table_Total.add(TableCell(Paragraph('Otros Bancos', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED), background_color=X11Color('LightGray')))
        Table_Total.add(TableCell(Paragraph('242342358723562187', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED), background_color=X11Color('LightGray')))
        Table_Total.add(TableCell(Paragraph('Factura', font='Helvetica-bold', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED), background_color=X11Color('LightGray')))
        Table_Total.add(Paragraph('Total:', font='Helvetica-bold', font_size=Decimal(8), padding_bottom=Decimal(2.5), horizontal_alignment=Alignment.RIGHT))
        Table_Total.add(Paragraph('$ %d.00' % (subtotal-anticipo), font='Helvetica', font_size=Decimal(8), padding_bottom=Decimal(2.5), horizontal_alignment=Alignment.RIGHT))
        Table_Total.set_padding_on_all_cells(Decimal(1), Decimal(1), Decimal(1), Decimal(1))
        Table_Total.no_borders()
        return Table_Total

    def Observations():
        Table_Observations: FixedColumnWidthTable = FixedColumnWidthTable(number_of_columns=1, number_of_rows=2, border_bottom=True, border_left=True, border_right=True, border_top=True)
        Table_Observations.add(Paragraph('Observaciones:', font='Helvetica', font_size=Decimal(8)))
        Table_Observations.add(Paragraph(' ', font='Helvetica', font_size=40))
        Table_Observations.set_padding_on_all_cells(Decimal(1), Decimal(1), Decimal(1), Decimal(1))
        Table_Observations.no_borders()
        return Table_Observations

    def DatesAditional():
        Table_DatesAditional: FixedColumnWidthTable = FixedColumnWidthTable(number_of_columns=3, number_of_rows=3, column_widths=(Decimal(1), Decimal(3), Decimal(1)))
        Table_DatesAditional.add(TableCell(Paragraph('No se aceptan reclamaciones posteriores a la firma de este documento, verificar que su mercancia la recibio completa y en buen estado.', font='Helvetica', font_size=Decimal(8), horizontal_alignment=Alignment.CENTERED), col_span=3))
        Table_DatesAditional.add(Paragraph(' ', font_size=Decimal(20)))
        Table_DatesAditional.add(Paragraph(' ', font_size=Decimal(20), border_bottom=True))
        Table_DatesAditional.add(Paragraph(' ', font_size=Decimal(20)))
        Table_DatesAditional.add(Paragraph(' ', font_size=Decimal(8)))
        Table_DatesAditional.add(Paragraph('Firma del Cliente', font_size=Decimal(8), border_top=True, horizontal_alignment=Alignment.CENTERED))
        Table_DatesAditional.add(Paragraph(' ', font_size=Decimal(8)))
        Table_DatesAditional.set_padding_on_all_cells(Decimal(1), Decimal(1), Decimal(1), Decimal(1))
        Table_DatesAditional.no_borders()
        return Table_DatesAditional