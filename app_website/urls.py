from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url('index', views.index, name='index'),
                  url('contact', views.contact, name='contact'),
                  url('product', views.product, name='product'),
                  url('post_comment', views.post_comment, name='post_comment'),
                  url('login', views.login, name='login'),
                  url('check', views.check, name='check'),
                  url('show_pic', views.show_pic, name='show_pic'),
                  url('add_pic', views.add_pic, name='add_pic'),
                  url('delete_pic', views.delete_pic, name='delete_pic'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
