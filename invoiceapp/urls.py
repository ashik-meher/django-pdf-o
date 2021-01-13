from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from invoice.views import GeneratePDF


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('invoice.urls')),
    url(r'^pdf/$', GeneratePDF.as_view()),
]
