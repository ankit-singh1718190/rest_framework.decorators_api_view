from django.urls import path
from .import views
urlpatterns = [
    path('',views.GetFuncation,name='get')
    
]
