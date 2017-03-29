from django.conf.urls import url
from . import  views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    url(r'^$', views.index, name="Index_Page"),
    url(r'^sign', views.signup, name="Index_Page"),
    url(r'^add',views.SignUpAction , name="auth"),
    url(r'^login',views.loginuser , name="login"),
    url(r'^log',views.log,name="log"),
    url(r'userlogout',views.outlog,name="logout")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
