
from django.urls import path
from teahelper import views


urlpatterns = [
    path('', views.home, name='home'),
    
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_request/', views.create_request, name='create_request'),
    path('request_list/', views.request_list, name='request_list'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('update_request_status/<int:request_id>/', views.update_request_status, name='update_request_status'),
    path('delete_request/<int:request_id>/', views.delete_request, name='delete_request'),
]
