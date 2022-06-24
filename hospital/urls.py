from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, login_user, register_user,logout_user

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login'),

    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
