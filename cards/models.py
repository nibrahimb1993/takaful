from django.db import models
from django.utils.translation import gettext_lazy as _

from cards import SEX_TYPES_CHOICES


class Card(models.Model):
    full_name = models.CharField(max_length=100, help_text=_("Full name for card holder"), verbose_name=_("Full Name"))
    phone_number = models.CharField(max_length=15, help_text=_("Phone number"), verbose_name=_("Phone number"))
    id_number = models.CharField(max_length=10, help_text=_("ID number"), verbose_name=_("ID number"))
    date_of_birth = models.DateField(help_text=_("Date of birth"), verbose_name=_("Date of birth"))
    sex = models.CharField(max_length=10, choices=SEX_TYPES_CHOICES, help_text=_("Sex type"),
                           verbose_name=_("Sex type"))
    created_at = models.DateTimeField(auto_now_add=True, help_text=_("Created at"), verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, help_text=_("Updated at"), verbose_name=_("Updated at"))

    def __str__(self):
        return "{} - {} - {}".format(_("Card"), self.id, self.full_name)

    class Meta:
        verbose_name = _("Card")
        verbose_name_plural = _("Cards")
