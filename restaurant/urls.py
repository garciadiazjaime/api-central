from django.urls import path

from restaurant.views import RestaurantList, RestaurantDetails


urlpatterns = [
    path('restaurant/', RestaurantList.as_view()),
    path('restaurant/<str:slug>/', RestaurantDetails.as_view()),
]
