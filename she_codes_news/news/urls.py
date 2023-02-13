from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name ="story"),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    # path('user_account/', views.UserProfileView.as_view(), name='userAccount'),
    path('<int:pk>/edit/', views.StoryEditView.as_view(), name ="storyEdit"),
    # path('<int:pk>/like', views.like, name ="like"), #change to function view
    path('<int:pk>/delete/', views.StoryDeleteView.as_view(), name ="storyDelete"),



]


# urlpatterns += staticfiles_urlpatterns()
