from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterApiView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('destroy/<int:pk>/', UserDestroyAPIView.as_view(), name='user_destroy')
    ]