from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from cards.models import Card

USER_MODEL = get_user_model()


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
    readonly_fields = [
        "created_by",
        "created_at",
        "updated_at",
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

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(created_by=request.user)
        return queryset

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        if not obj.expire_at:
            obj.expire_at = obj.started_at.replace(year=obj.started_at.year + 1)
        return super().save_model(request, obj, form, change)


admin.site.unregister(USER_MODEL)


@admin.register(USER_MODEL)
class CustomUserAdmin(UserAdmin):
    actions = ['reset_password']

    def reset_password(self, request, queryset):
        for user in queryset:
            user.set_password("123")
            user.save()

    reset_password.short_description = _("Reset password")
