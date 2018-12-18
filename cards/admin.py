from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML

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
        html_template = get_template('card.html')
        rendered_html = html_template.render({'card': queryset.first()})
        pdf_file = HTML(string=rendered_html).write_pdf()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="card.pdf"'
        response.write(pdf_file)
        return response

    print_card.short_description = "Print selected card"
