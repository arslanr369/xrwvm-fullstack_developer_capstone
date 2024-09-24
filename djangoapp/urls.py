from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Path for registration
    path('register', views.registration, name='register'),

    # Path for login
    path(route='login', view=views.login_user, name='login'),

    # Path for logout
    path(route='logout', view=views.logout_request, name='logout'),

    # Path for getting cars
    path(route='get_cars', view=views.get_cars, name='getcars'),

    # Path for fetching dealerships (all dealers)
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),

    # Path for fetching dealerships by state
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),

    # Path for fetching dealer details by dealer_id
    path(route='get_dealer/<int:dealer_id>', view=views.get_dealer_details, name='get_dealer_details'),

    # Other paths (like dealer reviews, add review, etc.)
    # path('dealer_reviews/', views.get_dealer_reviews, name='dealer_reviews'),
    # path('add_review/', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
