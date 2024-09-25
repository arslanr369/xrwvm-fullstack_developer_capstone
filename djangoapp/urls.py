from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # path for logout
    path('logout/', views.logout_request, name="logout"),
    
    # path for registration
    path('register/', views.registration, name='register'),

    # path for login
    path('login/', views.login_user, name='login'),

    # path for get_dealerships (with trailing slash)
    path('get_dealers/', views.get_dealerships, name='get_dealers'),

    # path for getting dealers by state
    path('get_dealers/<str:state>/', views.get_dealerships, name='get_dealers_by_state'),

    # path for dealer reviews view
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),

    # path for add a review view
    path('add_review/', views.add_review, name='add_review'),

    # path for reviews from dealer_id
    path('reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),

    # path for get_cars view
    path('get_cars/', views.get_cars, name='get_cars'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
