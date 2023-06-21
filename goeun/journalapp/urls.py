from django.contrib import admin
from django.urls import path
import journalapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/',journalapp.views.write, name='write'),
    path('useform/',journalapp.views.useform, name= 'useform'),
    path('detail02/<str:id>/',journalapp.views.detail02, name='detail02'),
]