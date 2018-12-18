from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML

from cards.models import Card


def render_card(card_id):
    """
    to remove duplicate code, this method return rendered html
    :param card_id:
    :return:
    """
    card = Card.objects.get(id=card_id)
    html_template = get_template('card.html')
    return html_template.render({'card': card})


def print_card(request, card_id):
    rendered_html = render_card(card_id)
    return HttpResponse(rendered_html)


def download_card(request, card_id):
    rendered_html = render_card(card_id)
    pdf_file = HTML(string=rendered_html).write_pdf()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="card.pdf"'
    response.write(pdf_file)
    return response
