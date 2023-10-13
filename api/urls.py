from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/', user),
    path('user/<int:pk>/', user_detail),
    path('post/', product),
    path('post/<int:pk>/', product_detail),
    path('rubric/', rubric),
    path('rubric/<int:pk>/', rubric_detail),

    path('auth/', include('dj_rest_auth.urls')),
]