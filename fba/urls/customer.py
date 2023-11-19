import django.urls as urls
from . import views


urlpatterns = [
    urls.path('/', views.welcome_page, name='welcome_page'),
    urls.path('/profile', views.profile, name='profile'),
    # ...
]
