from django.contrib import admin

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
