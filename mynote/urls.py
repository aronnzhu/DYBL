"""mynote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin
from note.views import *
from rules.views import *
from dailyreports.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^n/list/', get_note),
    url(r'^n/document/$', read_note),
    url(r'^n/comment/$', submit_comment),
    url(r'^n/download/$', file_download),
    url(r'^n/report/$', report),
    url(r'^n/rules/$', get_all_rules),
    url(r'^n/rules/read/$', view_rules),
    url(r'^n/rules/upload/$', upload_rules),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
