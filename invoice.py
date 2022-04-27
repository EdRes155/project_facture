from pathlib import Path
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout, MultiColumnLayout
from borb.pdf.canvas.layout.page_layout.page_layout import PageLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable
from borb.pdf.canvas.layout.table.flexible_column_width_table import (FlexibleColumnWidthTable,)
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.image.image import Image
from borb.pdf.canvas.geometry.line_segment import LineSegment
from borb.pdf.canvas.color.color import HexColor, X11Color
from borb.pdf.pdf import PDF
from decimal import Decimal
from datetime import datetime
import random

class Make_Invoice():
    def __init__(self):
        self.doc: Document = Document()

        page: Page = Page()

        self.doc.append_page(page)

        self.layout: PageLayout = MultiColumnLayout(page, number_of_columns=1, horizontal_margin=Decimal(5), vertical_margin=Decimal(5))

    def InformationBussines(self, name_bussines, information_address, information_general, number_invoice):
        self.layout.add(
        FixedColumnWidthTable(number_of_columns=3, number_of_rows=4, column_widths=[Decimal(1), Decimal(2), Decimal(1)])
        .add(TableCell(Paragraph(
            number_invoice,
            font='Helvetica-bold', font_size=Decimal(14),
            horizontal_alignment=Alignment.CENTERED,
            padding_bottom=Decimal(5),
        )))
        .add(TableCell(Paragraph(
            'Remision de Factura',
            font='Helvetica-bold',
            font_size=Decimal(14),
            horizontal_alignment=Alignment.CENTERED,
            padding_bottom=Decimal(5),
            ), col_span=2, background_color=HexColor('9D9D9D')))
        .add(TableCell(Image(
            Path('C:/Users/resen/Documents/fact-1/Sin-fondo.png'),
            width=Decimal(128),
            height=Decimal(48),
            horizontal_alignment=Alignment.CENTERED,
        ), row_span=3))
        .add(TableCell(Paragraph(
            name_bussines,
            font='Helvetica-bold',
            font_size=Decimal(12),
            horizontal_alignment=Alignment.CENTERED
            ), col_span=2))
        .add(TableCell(Paragraph(information_address,
        font='Helvetica',
        font_size=Decimal(10),
        horizontal_alignment=Alignment.CENTERED
        ), col_span=2))
        .add(TableCell(Paragraph(information_general,
        font='Helvetica',
        font_size=Decimal(10),
        horizontal_alignment=Alignment.CENTERED
        ), col_span=2))
        .set_padding_on_all_cells(Decimal(1), Decimal(2), Decimal(1), Decimal(2))
        .no_borders()
        )

    def InformationClient(self, info_client=[]):
        self.layout.add(
        FixedColumnWidthTable(number_of_rows=9, number_of_columns=4)
        .add(TableCell(Paragraph(
            'Cliente: %d' % info_client[0],
            font='Helvetica-bold',
            font_size=Decimal(8),
            padding_bottom=Decimal(2.5)
        ), col_span=2, background_color=HexColor('9D9D9D')))
        .add(TableCell(Paragraph(
            'Destinatario',
            font='Helvetica-bold',
            font_size=Decimal(8),
            padding_bottom=Decimal(2.5)
        ), col_span=2, background_color=HexColor('9D9D9D')))
        .add(TableCell(Paragraph(
            info_client[1],
            font='Helvetica',
            font_size=Decimal(8),
            padding_bottom=False,
            padding_top=False
        ), col_span=2))
        .add(TableCell(Paragraph(
            info_client[1], 
            font='Helvetica',
            font_size=Decimal(8),
            padding_bottom=False,
            padding_top=False
        ), col_span=2))
        .add(TableCell(Paragraph(
            info_client[3],
            font='Helvetica',
            font_size=Decimal(8),
        ), col_span=2))
        .add(TableCell(Paragraph(
            info_client[3],
            font='Helvetica',
            font_size=Decimal(8),
        ), col_span=2))
        .add(TableCell(Paragraph(
            info_client[4],
            font='Helvetica',
            font_size=Decimal(8),
        ), col_span=2))
        .add(TableCell(Paragraph(
            info_client[4],
            font='Helvetica',
            font_size=Decimal(8),
        ), col_span=2))
        .add(TableCell(Paragraph(
            info_client[5],
            font='Helvetica',
            font_size=Decimal(8),
        ), col_span=2))
        .add(TableCell(Paragraph(
            info_client[5],
            font='Helvetica',
            font_size=Decimal(8),
        ), col_span=2))
        .add(TableCell(Paragraph(
            'C.P. %d' % info_client[6],
            font='Helvetica',
            font_size=Decimal(8),
            ), col_span=2))
        .add(TableCell(Paragraph(
            'C.P. %d' % info_client[6],
            font='Helvetica',
            font_size=Decimal(8),
            ), col_span=2))
        .add(TableCell(Paragraph(
            'RFC: %d' % info_client[2],
            font='Helvetica',
            font_size=Decimal(8),
            ), col_span=2))
        .add(TableCell(Paragraph(
            ' ',
            font='Helvetica',
            font_size=Decimal(8),
            ), col_span=2))
        .add(TableCell(Paragraph(
            'Telf. %d' % info_client[7],
            font='Helvetica',
            font_size=Decimal(8),
            ), col_span=2))
        .add(TableCell(Paragraph(
            ' ',
            font='Helvetica',
            font_size=Decimal(8),
            ), col_span=2))
        .add(TableCell(Paragraph(
            'Email: %d' % info_client[8],
            font='Helvetica',
            font_size=Decimal(8),
            ), col_span=2))
        .add(TableCell(Paragraph(
            ' ',
            font='Helvetica',
            font_size=Decimal(8),
            ), col_span=2))
        .set_padding_on_all_cells(Decimal(0.5), Decimal(0.5), Decimal(0.5), Decimal(0.5))
        .no_borders()
    )

    def Save(self):
        with open('prueba.pdf', 'wb') as pdf_file_handle:
            PDF.dumps(pdf_file_handle, self.doc)

#if __name__ == '__main__':
#    Make_Invoice()
#    Make_Invoice().InformationBussines('Ferremas', 'Av. Abasolo 678 El Refugio', 'Tel. 4871146873  Whats. 4871146873', '7252113')
