from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('record/delete/<int:pk>', views.delete_record, name='delete'),
    path('record/add', views.add_record, name='add_record'),
    path('record/update/<int:pk>', views.update_record, name='update'),
]
