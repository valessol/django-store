from django.urls import path
#from cuentas.views import login, registro, editar_perfil, CambiarPassword
from django.contrib.auth.views import LogoutView
from users.views import login, register, profile_edit, profile_view

urlpatterns = [
    path('login/', login, name='login'),
    # path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile_view'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    # path('perfil/editar/password/', CambiarPassword.as_view(), name='cambiar_password')
]