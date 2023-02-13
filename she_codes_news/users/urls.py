from django.urls import path
# from .views import CreateAccountView, EditAccountView, profile_view
from .views import CreateAccountView, EditAccountView, UserProfileView
from . import views
from news.views import StoryView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
    name='createAccount'),
    path('edit-account/', EditAccountView.as_view(), name = 'editAccount'),
    # path('<int:user_id>/', profile_view, name = 'profile'),
    path('<int:pk>/', UserProfileView.as_view(), name='profile'),
    # path('<slug:profile>/', UserProfileView.as_view(), name='profile'),
    path('news/', StoryView.as_view(), name='profile_stories'),
]