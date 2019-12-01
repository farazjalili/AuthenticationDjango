from django.urls import path
from . import views
urlpatterns = [
    path('loginJWT', views.login_jwt),
    path('loginSession', views.login_session),
    path('getSessionInfo', views.session_info),
    path('resetPassword', views.reset_password),
]
