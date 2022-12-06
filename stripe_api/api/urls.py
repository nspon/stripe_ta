from django.urls import path
from . import views

urlpatterns = [
    path(
        'item/<int:id>/',
        views.item,
        name='item'
    ),
    path(
        'config/',
        views.stripe_config,
        name='config'
    ),
    path(
        'buy/<int:id>/',
        views.create_checkout_session,
        name='buy'
    ),
    path(
        'success/',
        views.success,
        name='success'
    )
]
