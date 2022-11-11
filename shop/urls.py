from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("myshop/", views.myshop, name="myshop"),
    # path("modify/", views.modify, name="modify"),
    path("modifyshop", views.modifyshop, name='modifyshop'),
    # path("uploadshop/", views.uploadshop, name="uploadshop")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)