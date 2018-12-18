from django.contrib import admin
from fpdf import FPDF, Template

from cards.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "phone_number",
        "id_number",
        "date_of_birth",
        "sex",
    ]

    actions = [
        'print_card'
    ]

    def print_card(self, request, queryset):
        # pdf = FPDF(unit="mm", format=[85, 50], orientation="p")
        # # pdf.alias_nb_pages()
        # pdf.add_page(orientation="p")
        # pdf.set_margins(0, 0, 0)
        # pdf.set_font('Arial')
        # # pdf.cell(10, 10, 'Hello!')
        # # pdf.cell(20, 20, 'Hello!')
        # # pdf.cell(30, 30, 'Hello!')
        # # pdf.multi_cell(0, 10, "hi\n i'm ibrahim\n yes")
        # # pdf.cell(0, 0, 'Printing line number 1', 1, 0)
        # # pdf.cell(30, 30, 'Printing line number 1', 1, 0)
        # pdf.cell(0, 0, 'Hello World!\n', 1, align="l")
        # pdf.ln()
        # pdf.cell(0, 10, 'Powered by FPDF 123.\n', 1, 1, "l")
        # # pdf.ln()
        # pdf.cell(0, 0, 'erqwe by FPDF 333.\n ', 1, 1, "l")

        # pdf.ln()
        # pdf.cell(0, 0, 'Powered asd FPDF.', 1, 1, "l")

        # pdf.ln()
        # pdf.cell(0, 10, 'Printing line number 2', 1, 1, True)

        elements = [
            {'name': 'company_name', 'type': 'T', 'x1': 17.0, 'y1': 32.5, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial',
             'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
             'text': '', 'priority': 2, },
            {'name': 'box', 'type': 'B', 'x1': 15.0, 'y1': 15.0, 'x2': 185.0, 'y2': 260.0, 'font': 'Arial', 'size': 0.0,
             'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None,
             'priority': 0, },
            {'name': 'box_x', 'type': 'B', 'x1': 95.0, 'y1': 15.0, 'x2': 105.0, 'y2': 25.0, 'font': 'Arial',
             'size': 0.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I',
             'text': None, 'priority': 2, },
            {'name': 'line1', 'type': 'L', 'x1': 100.0, 'y1': 25.0, 'x2': 100.0, 'y2': 57.0, 'font': 'Arial', 'size': 0,
             'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None,
             'priority': 3, },
            {'name': 'barcode', 'type': 'BC', 'x1': 20.0, 'y1': 246.5, 'x2': 140.0, 'y2': 254.0,
             'font': 'Interleaved 2of5 NT', 'size': 0.75, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0,
             'background': 0, 'align': 'I', 'text': '200000000001000159053338016581200810081', 'priority': 3, },
        ]

        # here we instantiate the template and define the HEADER
        f = Template(format="A4", elements=elements,
                     title="Sample Invoice")
        f.add_page()

        # we FILL some of the fields of the template with the information we want
        # note we access the elements treating the template instance as a "dict"
        f["company_name"] = "Sample Company"
        # f["company_logo"] = "pyfpdf/tutorial/logo.png"

        f.render("./template.pdf")

    print_card.short_description = "Print selected card"
