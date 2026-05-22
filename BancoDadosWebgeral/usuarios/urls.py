from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login_view, name='login'),
    path('plataforma/', views.text_plataforma, name='plataforma'),
]