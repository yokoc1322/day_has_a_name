from django.urls import include, path
from django.contrib.auth import views as auth_views

from rest_framework.routers import DefaultRouter

from . import views, views_api

app_name = 'diary'

api_router = DefaultRouter()
api_router.register(r'record', views_api.RecordViewSet)

api_urlpatterns = [
    path('', include(api_router.urls)),
]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.WriterLoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='diary/logout.html',
        next_page='../',
    ), name='logout'),
    path('write', views.WriteView.as_view(), name='write'),
    path('api/v1/', include(api_urlpatterns)),
]
