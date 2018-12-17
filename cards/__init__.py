from collections import namedtuple
from django.utils.translation import gettext_lazy as _

SexType = namedtuple("SexType", "Male Female")

SEX_TYPES = SexType(Male="Male", Female="Female")

SEX_TYPES_CHOICES = (
    (SEX_TYPES.Male, _("Male")),
    (SEX_TYPES.Female, _("Female")),
)
