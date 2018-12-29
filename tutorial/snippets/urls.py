from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views


# Create a router and register our viewsets with it.
router = DefaultRouter() # Automatically creates the root '/' view
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now deterined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
