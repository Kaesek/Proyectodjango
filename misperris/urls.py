from django.contrib.auth.views import LoginView,logout_then_login
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('inicio/', views.home,),
    path('index/', views.index, name= 'index'),
    path('gestionPerros/',views.gestionPerros, name='gestionPerros'),
    path('registrarPerros/', views.registrarPerros),
    path('edicionPerros/<codigo>', views.edicionPerros, name='edicionPerros'),
    path('editarPerros/', views.editarPerros),
    path('eliminarPerros/<codigo>', views.eliminarPerros, name='eliminarPerros'),
    path('formulario/', views.formulario, name='formulario'),
    path('formularioCarga/', views.formularioCarga),
    path('',LoginView.as_view(template_name='login.html'), name = 'login')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)