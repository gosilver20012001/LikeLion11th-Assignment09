from django.contrib import admin
from django.urls import path
import diaryapp.views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('new/', diaryapp.views.new, name='new'),
    path('new/create/', diaryapp.views.create, name= 'create'),
    path('notform/', diaryapp.views.notform, name= 'notform'),
    path('detail/<str:id>/',diaryapp.views.detail, name='detail'),
]