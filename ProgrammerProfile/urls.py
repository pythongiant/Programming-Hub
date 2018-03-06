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
    url(r'userlogout',views.outlog,name="logout"),
    url(r'^home',views.home,name="home"),
    #action
    url(r'^FormPost',views.formPost,name="post"),
    #form
    url(r'^post',views.post,name="PostForm"),
    
    url(r'^(?P<user_id>[0-9]+)/$',views.user_detail,name="user_detail"),
    url(r'^Post/(?P<article_id>[0-9]+)/$',views.article_detail,name="article_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
