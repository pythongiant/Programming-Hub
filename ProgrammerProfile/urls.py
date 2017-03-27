from django.conf.urls import url
from . import  views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #base url
    url(r'^$', views.index, name="Index_Page"),
    #Sign up page
    url(r'^sign', views.signup, name="Index_Page"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
