
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from chat import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('chating/',views.chatting,name='chatting'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
