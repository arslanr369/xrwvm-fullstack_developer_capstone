from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import registration

app_name = 'djangoapp'
urlpatterns = [
    # Path for registration
    path('register', views.registration, name='register'),

    # Path for login
    path(route='login', view=views.login_user, name='login'),

    # Path for logout
    path(route='logout', view=views.logout_request, name='logout'),

    # Path for getting cars
    path(route='get_cars', view=views.get_cars, name='getcars'),  # Updated path

    # Path for dealer reviews view
    # path('dealer_reviews/', views.get_dealer_reviews, name='dealer_reviews'),

    # Path for add a review view
    # path('add_review/', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
