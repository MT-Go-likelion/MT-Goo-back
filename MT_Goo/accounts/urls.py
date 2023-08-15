from django.urls import path
from .views import UserCreateView, UserRetrieveUpdateDestroyView, LoginView, LogoutView, suggestionView

urlpatterns = [
    path('user/signup/', UserCreateView.as_view(), name='signup'),
    path('user/signin/', LoginView.as_view(), name='signin'),
    path('user/signout/', LogoutView.as_view(), name='signout'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='detail'),
    path('suggestion/create/', suggestionView.as_view(), name='suggestionCreate'),
]
