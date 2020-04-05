from django.urls import include, path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.WriterLoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='diary/logout.html',
        next_page='../',
    ), name='logout'),
    path('write', views.WriteView.as_view(), name='write'),
]
