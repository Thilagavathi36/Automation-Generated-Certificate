"""
URL configuration for network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_panel_view, name='admin_panel'),
    path('new_intern/', views.new_intern_view, name='new_intern'), 
    path('save_form_data/', views.save_form_data, name='save_form_data'),
    path('generate_certificate/', views.generate_certificate, name='generate_certificate'),
    path('database/',views.database,name='database'),
    path('edit_certificate/<int:id>/', views.edit_certificate, name='edit_certificate'),  # Edit URL
    path('delete_certificate/<int:id>/', views.delete_certificate, name='delete_certificate'),  # Delete URL
    path('Existing_intern/',views.Existing_Intern,name='Existing_Intern'),
    path('update-status/<int:certificate_id>/', views.update_status, name='update_status'),
    path('Generate_Completion_Certificate/<int:certificate_id>/',views.Generate_Completion_Certificate,name='Generate_Completion_Certificate'),
    path('generate-certificate/<int:certificate_id>/', views.generate_completion_certificate, name='generate_certificate'),
]


