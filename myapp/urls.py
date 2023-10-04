from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

