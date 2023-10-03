from django.urls import path
from .views import*

urlpatterns = [
    path('', index, name="index"),
    path('home/', home, name="homepage"),
    path('about/', about, name="about"),
    path('notes/', notes, name="notes"),
    path('contact/', contact, name="contact"),
    # path('signup/', signup, name="signup"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', login, name="login"),
    # path('login/', LogInView.as_view(), name="login"),
]
