from django.urls import path, include
from django.db import router
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()

router.register("author", views.author)
router.register("category", views.Category)
router.register("book", views.book)


urlpatterns = [
    path("", include(router.urls)),
]
