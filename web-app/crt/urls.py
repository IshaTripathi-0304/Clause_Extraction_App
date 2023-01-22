from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show', views.show, name='show'),
    path('new', views.BookUploadView, name ='BookUploadView'),
]

'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    print(urlpatterns)
'''