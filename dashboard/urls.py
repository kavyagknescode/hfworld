from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dash_view, name='user-dashboard'),
    path('add-profile/<int:pk>', views.save_user_details, name='add-profile'),

]
