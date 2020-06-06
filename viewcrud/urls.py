from django.urls import path
from . import views
import portfolio.views

urlpatterns = [

    path('',views.read, name='home'),
    path('newblog/', views.create, name='newblog'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name= 'delete'),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
]