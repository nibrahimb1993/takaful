from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from cards.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "phone_number",
        "id_number",
        "date_of_birth",
        "sex",
        "_action",
    ]

    def _action(self, card):
        return '<a target="_blank" href="/print_card/{}/">{}</a> / <a href="/download_card/{}/">{}</a>'.format(
            card.id,
            _("Print"),
            card.id,
            _("Download"),
        )

    _action.short_description = _('Action')
    _action.allow_tags = True
