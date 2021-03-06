"""takaful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from cards.views import print_card, download_card

urlpatterns = i18n_patterns(
    url(r'^dashboard/', admin.site.urls),
    url(r'^print_card/(?P<card_id>.*)/$', print_card),
    url(r'^download_card/(?P<card_id>.*)/$', download_card),
)

admin.site.site_title = _('Takaful Dashboard')
