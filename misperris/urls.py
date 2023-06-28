
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name= 'index'),
    path('misperris/gestionPerros/',views.gestionPerros, name='gestionPerros'),
    path('registrarPerros/', views.registrarPerros),
    path('edicionPerros/<codigo>', views.edicionPerros, name='edicionPerros'),
    path('editarPerros/', views.editarPerros),
    path('eliminarPerros/<codigo>', views.eliminarPerros, name='eliminarPerros'),
    path('misperris/formulario/', views.formulario, name='formulario'),
    path('formularioCarga/', views.formularioCarga),
    path('misperris/success/', views.success, name= 'success'),
    path('logout/', views.exit, name='exit'),
    path('register/', views.register, name='register'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)