from django.urls import path
from subscription import views

app_name = 'subscription'

urlpatterns = [
    path('', views.subscription_view, name='subscription-view'),
    path('buy-subscription/<int:amt>', views.buy_subscription, name='buy-subscription'),
    path('view-candidates/', views.view_candidates, name='view-candidates'),
    path('payment-greeting/', views.payment_thanks, name='payment-greeting'),
]
