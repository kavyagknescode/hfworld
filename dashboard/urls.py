from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='user-dashboard'),
    path('profile/', views.profile_view, name='user-profile'),
    path('add-profile/<int:pk>', views.save_user_details, name='add-profile'),
    path('edit-profile/<int:id>', views.edit_user_details, name='edit-profile'),
    path('save-edited-profile/<int:id>', views.save_edited_details, name='save-edited-profile'),

]
