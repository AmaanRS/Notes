"""Notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='Notepad_index'),
    path('Signup/',views.Signup,name='Signup'),
    path('Login/',views.Login,name='Login'),
    path('Logout/',views.Logout,name='Logout'),
    path('Login/Login_verify/',views.Login_verify,name='Login_verify'),
    path('Signup/OTP/',views.OTP,name='OTP'),
    path('Signup/OTP/OTP_verify/',views.OTP_verify,name='OTP_verify'),
    path('notepad/',views.notepad,name='notepad'),
    path('notepad/new_note/',views.new_note,name='new_note'),
    path('notepad/edit_note/',views.edit_note,name='edit_note'),
    path('notepad/new_note/write_note/save_note/',views.save_note,name='save_note'),
    path('notepad/delete_note/',views.delete_note,name='delete_note'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

 # Did it for testing,does not know if it works or not
 # + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

