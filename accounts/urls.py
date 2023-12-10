from django.urls import path
from .views import signup , activate , profile

app_name = "accounts"

urlpatterns = [
    path("signup" ,signup ,name="singup"),
    path('<str:username>/activate', activate , name='activate')
]


