from django.urls import include, path
from rest_framework import routers

from async_app import views

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("lastone/", views.TheLastOnesView.as_view()),
]
