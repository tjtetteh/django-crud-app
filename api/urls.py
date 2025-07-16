from django.urls import path
from .views import Users

urlpatterns = [
    path('users', Users.as_view(), name='all_users'),
    path('user/<int:user_id>/', Users.as_view(), name="get_a_user"),
    path('create-user', Users.as_view(), name='create_user'),
    path('update-user/<int:user_id>/', Users.as_view(), name='update_user'),
    path('delete-user/<int:user_id>/', Users.as_view(), name='delete_user')
]

